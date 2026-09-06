use crate::Result;
use crate::graph::validate_graph;
use crate::id::{Id, Kind};
use crate::model::{
    ExperimentCatalog, ExperimentMeta, GraphCatalog, GraphNode, RecordCatalog, RecordMeta,
    RouteCatalog, RouteMeta, Source, Table,
};
use crate::source::{
    ParsedRecord, ResolvedSource, Resolver, contains_route_token, source_selector,
};
use serde::{Serialize, de::DeserializeOwned};
use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::path::{Path, PathBuf};
use std::str::FromStr;

const SCHEMA_VERSION: u32 = 3;

#[derive(Debug, Clone)]
pub enum Entry {
    Record(RecordMeta),
    Route(RouteMeta),
    Experiment(ExperimentMeta),
    Graph(GraphNode),
}

impl Entry {
    pub fn id(&self) -> &Id {
        match self {
            Self::Record(item) => &item.id,
            Self::Route(item) => &item.id,
            Self::Experiment(item) => &item.id,
            Self::Graph(item) => &item.id,
        }
    }

    pub fn kind(&self) -> Kind {
        match self {
            Self::Record(item) => item.kind,
            Self::Route(_) => Kind::Route,
            Self::Experiment(_) => Kind::Experiment,
            Self::Graph(item) => item.kind,
        }
    }

    pub fn title(&self) -> &str {
        match self {
            Self::Record(item) => &item.title,
            Self::Route(item) => &item.title,
            Self::Experiment(item) => item.id.experiment_name().unwrap_or(""),
            Self::Graph(item) => &item.title,
        }
    }

    pub fn source(&self) -> Option<&Source> {
        match self {
            Self::Record(item) => Some(&item.source),
            Self::Route(item) => Some(&item.source),
            Self::Experiment(_) => None,
            Self::Graph(item) => Some(&item.source),
        }
    }

    fn search_head(&self) -> String {
        match self {
            Self::Record(item) => format!(
                "{} {} {} {}",
                item.id,
                item.title,
                item.recorded_status.as_deref().unwrap_or(""),
                item.scope.as_deref().unwrap_or("")
            ),
            Self::Route(item) => format!(
                "{} {} {}",
                item.id,
                item.title,
                item.summary.as_deref().unwrap_or("")
            ),
            Self::Experiment(item) => format!(
                "{} {} {}",
                item.id,
                item.path,
                item.route_ids
                    .iter()
                    .map(ToString::to_string)
                    .collect::<Vec<_>>()
                    .join(" ")
            ),
            Self::Graph(item) => format!(
                "{} {} {}",
                item.id,
                item.title,
                item.scope.as_deref().unwrap_or("")
            ),
        }
    }
}

#[derive(Debug, Serialize)]
pub struct ListItem {
    pub id: Id,
    pub kind: Kind,
    pub title: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub snippet: Option<String>,
}

#[derive(Debug, Serialize)]
pub struct ListResult {
    pub matches: usize,
    pub limit: usize,
    pub items: Vec<ListItem>,
}

#[derive(Debug, Serialize)]
pub struct CheckReport {
    pub ok: bool,
    pub records: usize,
    pub routes: usize,
    pub experiments: usize,
    pub unresolved_experiment_routes: usize,
    pub graph_nodes: usize,
    pub graph_edges: usize,
}

#[derive(Debug, Serialize)]
pub struct SyncReport {
    pub records: usize,
    pub routes: usize,
    pub experiments: usize,
    pub added_routes: usize,
    pub added_experiments: usize,
}

pub struct Repository {
    pub root: PathBuf,
    pub resolver: Resolver,
    pub parsed_records: BTreeMap<Id, ParsedRecord>,
    pub record_catalog: RecordCatalog,
    pub route_catalog: RouteCatalog,
    pub experiment_catalog: ExperimentCatalog,
    pub graph: GraphCatalog,
    entries: BTreeMap<Id, Entry>,
}

impl Repository {
    pub fn open(root: impl AsRef<Path>) -> Result<Self> {
        let mut resolver = Resolver::new(root)?;
        let root = resolver.root().to_path_buf();
        let parsed_records = resolver.parse_records()?;
        let record_catalog: RecordCatalog = read_toml(&root.join("research/catalog.toml"))?;
        let route_catalog: RouteCatalog = read_toml(&root.join("research/routes.toml"))?;
        let experiment_catalog: ExperimentCatalog =
            read_toml(&root.join("research/experiments.toml"))?;
        let graph_path = root.join("research/graph.toml");
        let graph = if graph_path.exists() {
            read_toml(&graph_path)?
        } else {
            GraphCatalog::default()
        };
        for (name, version) in [
            ("catalog.toml", record_catalog.schema_version),
            ("routes.toml", route_catalog.schema_version),
            ("experiments.toml", experiment_catalog.schema_version),
        ] {
            if version != SCHEMA_VERSION {
                return Err(format!(
                    "research/{name} has schema_version {version}; expected {SCHEMA_VERSION}"
                ));
            }
        }
        if graph.schema_version != 1 {
            return Err(format!(
                "research/graph.toml has schema_version {}; expected 1",
                graph.schema_version
            ));
        }
        let mut entries = BTreeMap::new();
        for entry in record_catalog
            .records
            .iter()
            .cloned()
            .map(Entry::Record)
            .chain(route_catalog.routes.iter().cloned().map(Entry::Route))
            .chain(
                experiment_catalog
                    .experiments
                    .iter()
                    .cloned()
                    .map(Entry::Experiment),
            )
            .chain(graph.nodes.iter().cloned().map(Entry::Graph))
        {
            let id = entry.id().clone();
            if entries.insert(id.clone(), entry).is_some() {
                return Err(format!("duplicate catalog or graph ID: {id}"));
            }
        }
        Ok(Self {
            root,
            resolver,
            parsed_records,
            record_catalog,
            route_catalog,
            experiment_catalog,
            graph,
            entries,
        })
    }

    pub fn entries(&self) -> &BTreeMap<Id, Entry> {
        &self.entries
    }

    pub fn parse_cli_id(&self, text: &str) -> Result<Id> {
        if let Ok(id) = Id::from_str(text) {
            if self.entries.contains_key(&id) {
                return Ok(id);
            }
            return Err(format!("unknown ID: {id}"));
        }
        if is_bare_route_code(text) {
            let mut candidates = Vec::new();
            if let Ok(route) = Id::from_str(&format!("route:{text}"))
                && self.entries.contains_key(&route)
            {
                candidates.push(route.to_string());
            }
            let prefix = format!("experiment:{text}");
            let descendant_prefix = format!("{prefix}_");
            candidates.extend(self.entries.keys().filter_map(|id| {
                let shown = id.to_string();
                (shown == prefix || shown.starts_with(&descendant_prefix)).then_some(shown)
            }));
            let shown = if candidates.is_empty() {
                "no exact scoped candidates".to_owned()
            } else {
                candidates
                    .into_iter()
                    .take(8)
                    .collect::<Vec<_>>()
                    .join(", ")
            };
            return Err(format!(
                "ambiguous legacy F ID: {text}; use a scoped ID. Candidates: {shown}"
            ));
        }
        Err(format!("invalid ID: {text}"))
    }

    pub fn entry(&self, id: &Id) -> Result<Entry> {
        self.entries
            .get(id)
            .cloned()
            .ok_or_else(|| format!("unknown ID: {id}"))
    }

    pub fn resolve(&mut self, source: &Source) -> Result<ResolvedSource> {
        self.resolver.resolve(source, &self.parsed_records)
    }

    pub fn preferred_experiment_doc(&self, experiment: &ExperimentMeta) -> Option<String> {
        ["RESULT.md", "STATEMENT.md", "README.md"]
            .into_iter()
            .map(|name| format!("{}/{name}", experiment.path))
            .find(|path| self.root.join(path).is_file())
    }

    pub fn body(&mut self, entry: &Entry) -> Result<Option<Vec<u8>>> {
        if let Some(source) = entry.source() {
            return self.resolve(source).map(|resolved| Some(resolved.raw));
        }
        let Entry::Experiment(experiment) = entry else {
            return Ok(None);
        };
        let Some(path) = self.preferred_experiment_doc(experiment) else {
            return Ok(None);
        };
        self.resolve(&Source::File { path })
            .map(|resolved| Some(resolved.raw))
    }

    pub fn list(
        &mut self,
        query: Option<&str>,
        kind: Option<Kind>,
        limit: usize,
    ) -> Result<ListResult> {
        if limit == 0 {
            return Err("--limit must be positive".to_owned());
        }
        let query = query.map(str::to_lowercase);
        let entries: Vec<_> = self.entries.values().cloned().collect();
        let mut matches = Vec::new();
        for entry in entries {
            if kind.is_some_and(|wanted| entry.kind() != wanted) {
                continue;
            }
            let head = entry.search_head();
            let mut matched = query
                .as_ref()
                .is_none_or(|needle| head.to_lowercase().contains(needle));
            let mut snippet = None;
            if let Some(needle) = &query
                && let Some(raw) = self.body(&entry)?
            {
                let body = std::str::from_utf8(&raw)
                    .map_err(|error| format!("{} body is not UTF-8: {error}", entry.id()))?;
                if body.to_lowercase().contains(needle) {
                    matched = true;
                    snippet = Some(make_snippet(body, needle));
                }
            }
            if matched {
                matches.push(ListItem {
                    id: entry.id().clone(),
                    kind: entry.kind(),
                    title: entry.title().to_owned(),
                    snippet,
                });
            }
        }
        let count = matches.len();
        matches.truncate(limit);
        Ok(ListResult {
            matches: count,
            limit,
            items: matches,
        })
    }

    pub fn check(&mut self) -> Result<CheckReport> {
        let generated: Vec<_> = self.parsed_records.values().map(record_meta).collect();
        if self.record_catalog.records != generated {
            return Err("research/catalog.toml is stale; run research sync".to_owned());
        }
        let registry_routes = self.resolver.rows(Table::Routes)?;
        let registry_ids: BTreeSet<_> = registry_routes
            .iter()
            .map(|(key, _)| Id::from_str(&format!("route:{key}")))
            .collect::<std::result::Result<_, _>>()?;
        let catalog_ids: BTreeSet<_> = self
            .route_catalog
            .routes
            .iter()
            .map(|route| route.id.clone())
            .collect();
        if registry_ids != catalog_ids {
            return Err(set_difference("route catalog", &registry_ids, &catalog_ids));
        }
        for route in &self.route_catalog.routes {
            if route.id.kind() != Kind::Route {
                return Err(format!("route catalog contains non-route ID: {}", route.id));
            }
            let code = route.id.as_route().unwrap().code();
            match &route.source {
                Source::Row {
                    path,
                    table: Table::Routes,
                    key,
                } if path == "REGISTRY.md" && key == &code => {}
                _ => return Err(format!("route source selector mismatch: {}", route.id)),
            }
            self.resolver.resolve(&route.source, &self.parsed_records)?;
        }

        let mut actual_experiments = BTreeSet::new();
        for entry in fs::read_dir(self.root.join("experiments"))
            .map_err(|error| format!("cannot list experiments: {error}"))?
        {
            let entry = entry.map_err(|error| format!("cannot read experiment entry: {error}"))?;
            if entry.path().is_dir() {
                actual_experiments.insert(format!(
                    "experiments/{}",
                    entry.file_name().to_string_lossy()
                ));
            }
        }
        let catalog_experiments: BTreeSet<_> = self
            .experiment_catalog
            .experiments
            .iter()
            .map(|experiment| experiment.path.clone())
            .collect();
        if catalog_experiments.len() != self.experiment_catalog.experiments.len() {
            return Err("experiment catalog contains duplicate paths".to_owned());
        }
        if actual_experiments != catalog_experiments {
            return Err(set_difference(
                "experiment catalog",
                &actual_experiments,
                &catalog_experiments,
            ));
        }
        let known_routes: BTreeSet<_> = self
            .route_catalog
            .routes
            .iter()
            .map(|route| route.id.clone())
            .collect();
        for experiment in &self.experiment_catalog.experiments {
            let name = experiment.id.experiment_name().ok_or_else(|| {
                format!(
                    "experiment catalog contains non-experiment ID: {}",
                    experiment.id
                )
            })?;
            if experiment.path != format!("experiments/{name}") {
                return Err(format!("experiment ID/path mismatch: {}", experiment.id));
            }
            if !experiment.route_ids.is_empty() && experiment.route_evidence.is_empty() {
                return Err(format!(
                    "mapped experiment lacks evidence: {}",
                    experiment.id
                ));
            }
            let evidence: Vec<_> = experiment
                .route_evidence
                .iter()
                .map(|source| {
                    self.resolver
                        .resolve(source, &self.parsed_records)
                        .map(|resolved| (source, resolved))
                })
                .collect::<Result<_>>()?;
            for route_id in &experiment.route_ids {
                if !known_routes.contains(route_id) {
                    return Err(format!("unknown route {route_id} in {}", experiment.id));
                }
                let code = route_id.as_route().unwrap().code();
                let supported = evidence.iter().any(|(source, resolved)| match source {
                    Source::Row {
                        table: Table::Routes,
                        key,
                        ..
                    } => key == &code,
                    Source::Row {
                        table: Table::Runs, ..
                    } => resolved
                        .cells
                        .as_ref()
                        .and_then(|cells| cells.get(1))
                        .is_some_and(|family| contains_route_token(family, &code)),
                    Source::Field { .. } | Source::File { .. } | Source::Record { .. } => {
                        std::str::from_utf8(&resolved.raw)
                            .is_ok_and(|text| contains_route_token(text, &code))
                    }
                });
                if !supported {
                    return Err(format!(
                        "route evidence does not support {route_id}: {}",
                        experiment.id
                    ));
                }
            }
        }
        validate_graph(self)?;
        Ok(CheckReport {
            ok: true,
            records: self.record_catalog.records.len(),
            routes: self.route_catalog.routes.len(),
            experiments: self.experiment_catalog.experiments.len(),
            unresolved_experiment_routes: self
                .experiment_catalog
                .experiments
                .iter()
                .filter(|experiment| experiment.route_ids.is_empty())
                .count(),
            graph_nodes: self.graph.nodes.len(),
            graph_edges: self.graph.edges.len(),
        })
    }
}

pub fn sync(root: impl AsRef<Path>) -> Result<SyncReport> {
    let mut resolver = Resolver::new(root)?;
    let root = resolver.root().to_path_buf();
    let parsed_records = resolver.parse_records()?;
    let records: Vec<_> = parsed_records.values().map(record_meta).collect();

    let routes_path = root.join("research/routes.toml");
    let mut routes = read_optional::<RouteCatalog>(&routes_path)?.unwrap_or(RouteCatalog {
        schema_version: SCHEMA_VERSION,
        routes: Vec::new(),
    });
    require_schema("routes.toml", routes.schema_version)?;
    let mut route_map = BTreeMap::new();
    for item in routes.routes.drain(..) {
        if route_map.insert(item.id.clone(), item).is_some() {
            return Err("routes.toml contains duplicate IDs".to_owned());
        }
    }
    let before_routes = route_map.len();
    for (key, cells) in resolver.rows(Table::Routes)? {
        let id = Id::from_str(&format!("route:{key}"))?;
        route_map.entry(id.clone()).or_insert_with(|| RouteMeta {
            id,
            title: cells.get(1).cloned().unwrap_or_else(|| key.clone()),
            summary: None,
            source: Source::Row {
                path: "REGISTRY.md".to_owned(),
                table: Table::Routes,
                key,
            },
        });
    }
    routes.routes = route_map.into_values().collect();

    let experiments_path = root.join("research/experiments.toml");
    let mut experiments =
        read_optional::<ExperimentCatalog>(&experiments_path)?.unwrap_or(ExperimentCatalog {
            schema_version: SCHEMA_VERSION,
            experiments: Vec::new(),
        });
    require_schema("experiments.toml", experiments.schema_version)?;
    let mut experiment_map = BTreeMap::new();
    for item in experiments.experiments.drain(..) {
        if experiment_map.insert(item.id.clone(), item).is_some() {
            return Err("experiments.toml contains duplicate IDs".to_owned());
        }
    }
    let before_experiments = experiment_map.len();
    for entry in fs::read_dir(root.join("experiments"))
        .map_err(|error| format!("cannot list experiments: {error}"))?
    {
        let entry = entry.map_err(|error| format!("cannot read experiment entry: {error}"))?;
        if !entry.path().is_dir() {
            continue;
        }
        let name = entry.file_name().to_string_lossy().into_owned();
        let id = Id::from_str(&format!("experiment:{name}"))?;
        experiment_map.entry(id.clone()).or_insert(ExperimentMeta {
            id,
            path: format!("experiments/{name}"),
            route_ids: Vec::new(),
            route_evidence: Vec::new(),
        });
    }
    experiments.experiments = experiment_map.into_values().collect();

    let catalog = RecordCatalog {
        schema_version: SCHEMA_VERSION,
        records,
    };
    write_atomic(
        &root.join("research/catalog.toml"),
        &write_records(&catalog),
    )?;
    write_atomic(&routes_path, &write_routes(&routes))?;
    write_atomic(&experiments_path, &write_experiments(&experiments))?;
    Ok(SyncReport {
        records: catalog.records.len(),
        routes: routes.routes.len(),
        experiments: experiments.experiments.len(),
        added_routes: routes.routes.len() - before_routes,
        added_experiments: experiments.experiments.len() - before_experiments,
    })
}

fn record_meta(record: &ParsedRecord) -> RecordMeta {
    RecordMeta {
        id: record.id.clone(),
        kind: record.kind,
        title: record.title.clone(),
        source: record.source(),
        recorded_status: record.recorded_status.clone(),
        scope: record.scope.clone(),
    }
}

fn read_toml<T: DeserializeOwned>(path: &Path) -> Result<T> {
    let text = fs::read_to_string(path)
        .map_err(|error| format!("cannot read {}: {error}", path.display()))?;
    toml::from_str(&text).map_err(|error| format!("invalid {}: {error}", path.display()))
}

fn read_optional<T: DeserializeOwned>(path: &Path) -> Result<Option<T>> {
    path.exists().then(|| read_toml(path)).transpose()
}

fn require_schema(name: &str, version: u32) -> Result<()> {
    (version == SCHEMA_VERSION).then_some(()).ok_or_else(|| {
        format!("research/{name} has schema_version {version}; expected {SCHEMA_VERSION}")
    })
}

fn is_bare_route_code(text: &str) -> bool {
    let Some(rest) = text.strip_prefix('F') else {
        return false;
    };
    let (number, branch) = rest
        .split_once('-')
        .map_or((rest, None), |(number, branch)| (number, Some(branch)));
    number.len() >= 2
        && number.bytes().all(|byte| byte.is_ascii_digit())
        && branch.is_none_or(|value| value.len() == 1 && value.as_bytes()[0].is_ascii_uppercase())
}

fn make_snippet(body: &str, needle: &str) -> String {
    let normalized = body.split_whitespace().collect::<Vec<_>>().join(" ");
    let lower = normalized.to_lowercase();
    let byte = lower.find(needle).unwrap_or(0);
    let char_index = lower[..byte].chars().count();
    let chars: Vec<_> = normalized.chars().collect();
    let start = char_index.saturating_sub(60);
    let end = (char_index + needle.chars().count() + 120).min(chars.len());
    let mut snippet: String = chars[start..end].iter().collect();
    if start > 0 {
        snippet.insert(0, '…');
    }
    if end < chars.len() {
        snippet.push('…');
    }
    snippet
}

fn set_difference<T: Ord + ToString>(
    label: &str,
    actual: &BTreeSet<T>,
    stored: &BTreeSet<T>,
) -> String {
    let missing = actual
        .difference(stored)
        .take(8)
        .map(ToString::to_string)
        .collect::<Vec<_>>()
        .join(", ");
    let extra = stored
        .difference(actual)
        .take(8)
        .map(ToString::to_string)
        .collect::<Vec<_>>()
        .join(", ");
    format!("{label} mismatch; missing [{missing}], extra [{extra}]")
}

fn quote(value: &str) -> String {
    serde_json::to_string(value).unwrap()
}

fn write_records(catalog: &RecordCatalog) -> String {
    let mut output = format!(
        "# Generated by `research sync`. Do not edit by hand.\n\
         # Historical labels and directives are data, not current instructions.\n\
         schema_version = {}\n\n",
        catalog.schema_version
    );
    for record in &catalog.records {
        output.push_str("[[records]]\n");
        output.push_str(&format!(
            "id = {}\nkind = {}\ntitle = {}\nsource = {}\n",
            quote(&record.id.to_string()),
            quote(&record.kind.to_string()),
            quote(&record.title),
            source_selector(&record.source)
        ));
        if let Some(status) = &record.recorded_status {
            output.push_str(&format!("recorded_status = {}\n", quote(status)));
        }
        if let Some(scope) = &record.scope {
            output.push_str(&format!("scope = {}\n", quote(scope)));
        }
        output.push('\n');
    }
    final_newline(output)
}

fn write_routes(catalog: &RouteCatalog) -> String {
    let mut output = format!("schema_version = {}\n\n", catalog.schema_version);
    for route in &catalog.routes {
        output.push_str("[[routes]]\n");
        output.push_str(&format!(
            "id = {}\ntitle = {}\n",
            quote(&route.id.to_string()),
            quote(&route.title)
        ));
        if let Some(summary) = &route.summary {
            output.push_str(&format!("summary = {}\n", quote(summary)));
        }
        output.push_str(&format!("source = {}\n\n", source_selector(&route.source)));
    }
    final_newline(output)
}

fn write_experiments(catalog: &ExperimentCatalog) -> String {
    let mut output = format!("schema_version = {}\n\n", catalog.schema_version);
    for experiment in &catalog.experiments {
        output.push_str("[[experiments]]\n");
        output.push_str(&format!(
            "id = {}\npath = {}\n",
            quote(&experiment.id.to_string()),
            quote(&experiment.path)
        ));
        let route_ids = experiment
            .route_ids
            .iter()
            .map(|id| quote(&id.to_string()))
            .collect::<Vec<_>>()
            .join(", ");
        output.push_str(&format!("route_ids = [{route_ids}]\n"));
        let evidence = experiment
            .route_evidence
            .iter()
            .map(source_selector)
            .collect::<Vec<_>>()
            .join(", ");
        output.push_str(&format!("route_evidence = [{evidence}]\n\n"));
    }
    final_newline(output)
}

fn final_newline(mut output: String) -> String {
    while output.ends_with("\n\n") {
        output.pop();
    }
    if !output.ends_with('\n') {
        output.push('\n');
    }
    output
}

fn write_atomic(path: &Path, content: &str) -> Result<()> {
    let temporary = path.with_extension("toml.tmp");
    fs::write(&temporary, content)
        .map_err(|error| format!("cannot write {}: {error}", temporary.display()))?;
    fs::rename(&temporary, path)
        .map_err(|error| format!("cannot replace {}: {error}", path.display()))
}
