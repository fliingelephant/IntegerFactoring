use crate::Result;
use crate::catalog::{Entry, Repository};
use crate::id::{Id, Kind};
use crate::model::{GraphEdge, GraphFormat};
use crate::source::source_selector;
use serde::Serialize;
use std::collections::{BTreeMap, BTreeSet, VecDeque};

#[derive(Debug, Clone, Serialize)]
pub struct ViewNode {
    pub id: Id,
    pub kind: Kind,
    pub title: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub scope: Option<String>,
}

#[derive(Debug, Clone, Serialize)]
pub struct GraphView {
    pub partial: bool,
    pub reverse: bool,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub root: Option<Id>,
    pub nodes: Vec<ViewNode>,
    pub edges: Vec<GraphEdge>,
}

pub fn validate_graph(repository: &mut Repository) -> Result<()> {
    let mut node_ids = BTreeSet::new();
    for node in &repository.graph.nodes {
        if !matches!(node.kind, Kind::Goal | Kind::Question) || node.kind != node.id.kind() {
            return Err(format!(
                "graph node {} must have matching goal or question kind",
                node.id
            ));
        }
        if !node_ids.insert(node.id.clone()) {
            return Err(format!("duplicate graph node ID: {}", node.id));
        }
        repository
            .resolver
            .resolve(&node.source, &repository.parsed_records)?;
    }
    let mut edge_keys = BTreeSet::new();
    for edge in &repository.graph.edges {
        if !repository.entries().contains_key(&edge.from)
            || !repository.entries().contains_key(&edge.to)
        {
            return Err(format!(
                "graph edge has missing endpoint: {} {} {}",
                edge.from, edge.relation, edge.to
            ));
        }
        if !edge_keys.insert((edge.from.clone(), edge.to.clone(), edge.relation)) {
            return Err(format!(
                "duplicate graph edge: {} {} {}",
                edge.from, edge.relation, edge.to
            ));
        }
        if edge.evidence.is_empty() {
            return Err(format!(
                "graph edge has no evidence selectors: {} {} {}",
                edge.from, edge.relation, edge.to
            ));
        }
        for source in &edge.evidence {
            repository
                .resolver
                .resolve(source, &repository.parsed_records)?;
        }
    }
    reject_dependency_cycles(&repository.graph.edges)
}

fn reject_dependency_cycles(edges: &[GraphEdge]) -> Result<()> {
    let mut indegree = BTreeMap::<Id, usize>::new();
    let mut outgoing = BTreeMap::<Id, Vec<Id>>::new();
    for edge in edges.iter().filter(|edge| edge.relation.is_dependency()) {
        *indegree.entry(edge.to.clone()).or_default() += 1;
        indegree.entry(edge.from.clone()).or_default();
        outgoing
            .entry(edge.from.clone())
            .or_default()
            .push(edge.to.clone());
    }
    let mut queue: VecDeque<_> = indegree
        .iter()
        .filter(|(_, degree)| **degree == 0)
        .map(|(id, _)| id.clone())
        .collect();
    let mut visited = 0;
    while let Some(id) = queue.pop_front() {
        visited += 1;
        for next in outgoing.get(&id).into_iter().flatten() {
            let degree = indegree.get_mut(next).unwrap();
            *degree -= 1;
            if *degree == 0 {
                queue.push_back(next.clone());
            }
        }
    }
    if visited != indegree.len() {
        return Err("uses/requires dependency graph contains a cycle".to_owned());
    }
    Ok(())
}

pub fn view(repository: &Repository, root: Option<&Id>, reverse: bool) -> Result<GraphView> {
    if reverse && root.is_none() {
        return Err("--reverse requires an ID".to_owned());
    }
    let entries = repository.entries();
    if let Some(id) = root
        && !entries.contains_key(id)
    {
        return Err(format!("unknown graph ID: {id}"));
    }
    let mut selected = BTreeSet::new();
    if let Some(id) = root {
        let mut adjacency = BTreeMap::<Id, Vec<Id>>::new();
        for edge in repository
            .graph
            .edges
            .iter()
            .filter(|edge| edge.relation.is_dependency())
        {
            let (from, to) = if reverse {
                (&edge.to, &edge.from)
            } else {
                (&edge.from, &edge.to)
            };
            adjacency.entry(from.clone()).or_default().push(to.clone());
        }
        selected.insert(id.clone());
        let mut queue = VecDeque::from([id.clone()]);
        while let Some(current) = queue.pop_front() {
            for next in adjacency.get(&current).into_iter().flatten() {
                if selected.insert(next.clone()) {
                    queue.push_back(next.clone());
                }
            }
        }
    } else {
        selected.extend(repository.graph.nodes.iter().map(|node| node.id.clone()));
        for edge in &repository.graph.edges {
            selected.insert(edge.from.clone());
            selected.insert(edge.to.clone());
        }
    }

    let dependency_nodes = selected.clone();
    let mut edges = Vec::new();
    for edge in &repository.graph.edges {
        let include = if root.is_none() {
            true
        } else if edge.relation.is_dependency() {
            dependency_nodes.contains(&edge.from) && dependency_nodes.contains(&edge.to)
        } else {
            dependency_nodes.contains(&edge.from) || dependency_nodes.contains(&edge.to)
        };
        if include {
            selected.insert(edge.from.clone());
            selected.insert(edge.to.clone());
            edges.push(edge.clone());
        }
    }
    let nodes = selected
        .into_iter()
        .map(|id| view_node(entries.get(&id).unwrap()))
        .collect();
    Ok(GraphView {
        partial: true,
        reverse,
        root: root.cloned(),
        nodes,
        edges,
    })
}

fn view_node(entry: &Entry) -> ViewNode {
    let scope = match entry {
        Entry::Record(record) => record.scope.clone(),
        Entry::Graph(node) => node.scope.clone(),
        _ => None,
    };
    ViewNode {
        id: entry.id().clone(),
        kind: entry.kind(),
        title: entry.title().to_owned(),
        scope,
    }
}

pub fn render(view: &GraphView, format: GraphFormat) -> Result<Vec<u8>> {
    match format {
        GraphFormat::Json => serde_json::to_vec_pretty(view)
            .map_err(|error| format!("cannot serialize graph JSON: {error}")),
        GraphFormat::Text => Ok(render_text(view).into_bytes()),
        GraphFormat::Mermaid => Ok(render_mermaid(view).into_bytes()),
    }
}

fn render_text(view: &GraphView) -> String {
    let mut output = String::from(
        "This graph is explicitly partial. A missing edge does not mean there is no dependency.\n",
    );
    for node in &view.nodes {
        output.push_str(&format!("{} [{}] {}\n", node.id, node.kind, node.title));
    }
    for edge in &view.edges {
        output.push_str(&format!(
            "{} -[{}]-> {}\n",
            edge.from, edge.relation, edge.to
        ));
        for evidence in &edge.evidence {
            output.push_str(&format!("  evidence: {}\n", source_selector(evidence)));
        }
        if let Some(note) = &edge.note {
            output.push_str(&format!("  note: {note}\n"));
        }
    }
    output
}

fn render_mermaid(view: &GraphView) -> String {
    let mut output = String::from(
        "%% This graph is explicitly partial; a missing edge does not mean no dependency.\nflowchart LR\n",
    );
    let names: BTreeMap<_, _> = view
        .nodes
        .iter()
        .enumerate()
        .map(|(index, node)| (node.id.clone(), format!("n{index}")))
        .collect();
    for node in &view.nodes {
        let label = format!("{}\\n{}", node.id, node.title)
            .replace('"', "'")
            .replace(']', ")");
        output.push_str(&format!("  {}[\"{}\"]\n", names[&node.id], label));
    }
    for edge in &view.edges {
        output.push_str(&format!(
            "  {} -->|{}| {}\n",
            names[&edge.from], edge.relation, names[&edge.to]
        ));
    }
    output
}
