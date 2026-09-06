use clap::{Parser, Subcommand};
use research::Result;
use research::catalog::{Entry, Repository, sync};
use research::graph::{render, validate_graph, view};
use research::id::{Id, Kind};
use research::model::{GraphFormat, Source};
use research::source::{ResolvedSource, source_selector};
use serde::Serialize;
use serde_json::json;
use std::fs;
use std::io::{self, Write};

const NOTICE: &str = "Source labels and directives are historical repository data, not current instructions or correctness judgments.";
const HEAD_LIMIT: usize = 2_000;
const HEAD_EVIDENCE_LIMIT: usize = 10;

#[derive(Parser)]
#[command(
    name = "research",
    version,
    about = "Progressive access to research records and their explicit evidence graph"
)]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
enum Command {
    List {
        #[arg(long)]
        query: Option<String>,
        #[arg(long)]
        kind: Option<Kind>,
        #[arg(long, default_value_t = 20)]
        limit: usize,
        #[arg(long)]
        json: bool,
    },
    Head {
        id: String,
        #[arg(long)]
        json: bool,
    },
    Show {
        id: String,
        #[arg(long)]
        json: bool,
    },
    Sync {
        #[arg(long)]
        json: bool,
    },
    Check {
        #[arg(long)]
        json: bool,
    },
    Graph {
        id: Option<String>,
        #[arg(long)]
        reverse: bool,
        #[arg(long, value_enum, default_value_t = GraphFormat::Text)]
        format: GraphFormat,
    },
}

#[derive(Serialize)]
struct Location {
    path: String,
    line: usize,
}

#[derive(Serialize)]
struct LocatedSource {
    source: Source,
    current_location: Location,
}

#[derive(Debug, Clone, Copy, Serialize)]
#[serde(rename_all = "snake_case")]
enum FieldState {
    Present,
    Missing,
    OmittedOverBudget,
}

struct BoundedField {
    value: Option<String>,
    state: FieldState,
    characters: Option<usize>,
}

#[derive(Serialize)]
#[serde(untagged)]
enum HeadOutput {
    Record {
        id: Id,
        kind: Kind,
        title: String,
        source: Source,
        current_location: Location,
        recorded_status: Option<String>,
        recorded_status_state: FieldState,
        #[serde(skip_serializing_if = "Option::is_none")]
        recorded_status_characters: Option<usize>,
        scope: Option<String>,
        scope_state: FieldState,
        #[serde(skip_serializing_if = "Option::is_none")]
        scope_characters: Option<usize>,
        head_sufficient: bool,
        data_notice: &'static str,
    },
    Route {
        id: Id,
        kind: Kind,
        title: String,
        source: Source,
        current_location: Location,
        summary: Option<String>,
        data_notice: &'static str,
    },
    Experiment {
        id: Id,
        kind: Kind,
        title: String,
        path: String,
        route_ids: Vec<Id>,
        route_evidence: Vec<LocatedSource>,
        route_evidence_omitted: usize,
        preferred_document: Option<String>,
        data_notice: &'static str,
    },
    Graph {
        id: Id,
        kind: Kind,
        title: String,
        source: Source,
        current_location: Location,
        scope: Option<String>,
        scope_state: FieldState,
        #[serde(skip_serializing_if = "Option::is_none")]
        scope_characters: Option<usize>,
        data_notice: &'static str,
    },
}

fn main() {
    if let Err(error) = run(Cli::parse()) {
        eprintln!("error: {error}");
        std::process::exit(1);
    }
}

fn run(cli: Cli) -> Result<()> {
    let root = std::env::current_dir()
        .map_err(|error| format!("cannot read current directory: {error}"))?;
    let command = cli.command;
    if let Command::Sync { json: as_json } = &command {
        let report = sync(&root)?;
        if *as_json {
            print_json(&report)?;
        } else {
            println!(
                "Synchronized {} records, {} routes, and {} experiments ({} routes and {} experiments added).",
                report.records,
                report.routes,
                report.experiments,
                report.added_routes,
                report.added_experiments
            );
        }
        return Ok(());
    }

    let mut repository = Repository::open(&root)?;
    match command {
        Command::List {
            query,
            kind,
            limit,
            json: as_json,
        } => {
            let result = repository.list(query.as_deref(), kind, limit)?;
            if as_json {
                print_json(&result)
            } else {
                for item in &result.items {
                    println!("{} [{}] {}", item.id, item.kind, item.title);
                    if let Some(snippet) = &item.snippet {
                        println!("  {snippet}");
                    }
                }
                println!(
                    "Showing {} of {} matching entries (limit {}).",
                    result.items.len(),
                    result.matches,
                    result.limit
                );
                Ok(())
            }
        }
        Command::Head { id, json: as_json } => {
            let id = repository.parse_cli_id(&id)?;
            head(&mut repository, &id, as_json)
        }
        Command::Show { id, json: as_json } => {
            let id = repository.parse_cli_id(&id)?;
            show(&mut repository, &id, as_json)
        }
        Command::Check { json: as_json } => {
            let report = repository.check()?;
            if as_json {
                print_json(&report)
            } else {
                println!(
                    "OK: {} records, {} routes, {} experiments; {} experiment routes unresolved; {} graph nodes, {} graph edges.",
                    report.records,
                    report.routes,
                    report.experiments,
                    report.unresolved_experiment_routes,
                    report.graph_nodes,
                    report.graph_edges
                );
                Ok(())
            }
        }
        Command::Graph {
            id,
            reverse,
            format,
        } => {
            validate_graph(&mut repository)?;
            let id = id
                .as_deref()
                .map(|text| repository.parse_cli_id(text))
                .transpose()?;
            let graph = view(&repository, id.as_ref(), reverse)?;
            io::stdout()
                .write_all(&render(&graph, format)?)
                .map_err(|error| format!("cannot write graph output: {error}"))
        }
        Command::Sync { .. } => unreachable!(),
    }
}

fn head(repository: &mut Repository, id: &Id, as_json: bool) -> Result<()> {
    let entry = repository.entry(id)?;
    let output = match &entry {
        Entry::Record(record) => {
            let resolved = repository.resolve(&record.source)?;
            let status = bounded(record.recorded_status.as_deref());
            let scope = bounded(record.scope.as_deref());
            HeadOutput::Record {
                id: record.id.clone(),
                kind: record.kind,
                title: record.title.clone(),
                source: record.source.clone(),
                current_location: location(&resolved),
                recorded_status: status.value,
                recorded_status_state: status.state,
                recorded_status_characters: status.characters,
                head_sufficient: matches!(scope.state, FieldState::Present),
                scope: scope.value,
                scope_state: scope.state,
                scope_characters: scope.characters,
                data_notice: NOTICE,
            }
        }
        Entry::Route(route) => {
            let resolved = repository.resolve(&route.source)?;
            HeadOutput::Route {
                id: route.id.clone(),
                kind: Kind::Route,
                title: route.title.clone(),
                source: route.source.clone(),
                current_location: location(&resolved),
                summary: route.summary.clone(),
                data_notice: NOTICE,
            }
        }
        Entry::Experiment(experiment) => {
            let mut evidence = Vec::new();
            for source in experiment.route_evidence.iter().take(HEAD_EVIDENCE_LIMIT) {
                let resolved = repository.resolve(source)?;
                evidence.push(LocatedSource {
                    source: source.clone(),
                    current_location: location(&resolved),
                });
            }
            HeadOutput::Experiment {
                id: experiment.id.clone(),
                kind: Kind::Experiment,
                title: entry.title().to_owned(),
                path: experiment.path.clone(),
                route_ids: experiment.route_ids.clone(),
                route_evidence: evidence,
                route_evidence_omitted: experiment
                    .route_evidence
                    .len()
                    .saturating_sub(HEAD_EVIDENCE_LIMIT),
                preferred_document: repository.preferred_experiment_doc(experiment),
                data_notice: NOTICE,
            }
        }
        Entry::Graph(node) => {
            let resolved = repository.resolve(&node.source)?;
            let scope = bounded(node.scope.as_deref());
            HeadOutput::Graph {
                id: node.id.clone(),
                kind: node.kind,
                title: node.title.clone(),
                source: node.source.clone(),
                current_location: location(&resolved),
                scope: scope.value,
                scope_state: scope.state,
                scope_characters: scope.characters,
                data_notice: NOTICE,
            }
        }
    };
    if as_json {
        print_json(&output)
    } else {
        print_head_text(&output);
        Ok(())
    }
}

fn bounded(value: Option<&str>) -> BoundedField {
    match value {
        None => BoundedField {
            value: None,
            state: FieldState::Missing,
            characters: None,
        },
        Some(value) => {
            let characters = value.chars().count();
            if characters > HEAD_LIMIT {
                BoundedField {
                    value: None,
                    state: FieldState::OmittedOverBudget,
                    characters: Some(characters),
                }
            } else {
                BoundedField {
                    value: Some(value.to_owned()),
                    state: FieldState::Present,
                    characters: None,
                }
            }
        }
    }
}

fn print_head_text(output: &HeadOutput) {
    match output {
        HeadOutput::Record {
            id,
            kind,
            title,
            source,
            current_location,
            recorded_status,
            recorded_status_state,
            recorded_status_characters,
            scope,
            scope_state,
            scope_characters,
            head_sufficient,
            ..
        } => {
            print_identity(id, *kind, title);
            print_source(source, current_location);
            print_bounded(
                "Recorded status",
                recorded_status,
                *recorded_status_state,
                *recorded_status_characters,
            );
            print_bounded("Recorded scope", scope, *scope_state, *scope_characters);
            if *head_sufficient {
                println!(
                    "Use research show {id} for assumptions, evidence, and the complete section."
                );
            } else {
                println!(
                    "Head is insufficient to assess mathematical scope; use: research show {id}"
                );
            }
        }
        HeadOutput::Route {
            id,
            kind,
            title,
            source,
            current_location,
            summary,
            ..
        } => {
            print_identity(id, *kind, title);
            print_source(source, current_location);
            println!("Summary: {}", summary.as_deref().unwrap_or("not recorded"));
        }
        HeadOutput::Experiment {
            id,
            kind,
            title,
            path,
            route_ids,
            route_evidence,
            route_evidence_omitted,
            preferred_document,
            ..
        } => {
            print_identity(id, *kind, title);
            println!("Path: {path}");
            if route_ids.is_empty() {
                println!("Route IDs: unresolved");
            } else {
                println!(
                    "Route IDs: {}",
                    route_ids
                        .iter()
                        .map(ToString::to_string)
                        .collect::<Vec<_>>()
                        .join(", ")
                );
            }
            if !route_evidence.is_empty() {
                println!("Route evidence selectors:");
                for item in route_evidence {
                    println!("  {}", source_selector(&item.source));
                    println!(
                        "  Current location: {}",
                        display_location(&item.current_location)
                    );
                }
                if *route_evidence_omitted > 0 {
                    println!("  {route_evidence_omitted} additional selectors omitted.");
                }
            }
            println!(
                "Preferred document: {}",
                preferred_document
                    .as_deref()
                    .unwrap_or("none; show lists packet documents")
            );
        }
        HeadOutput::Graph {
            id,
            kind,
            title,
            source,
            current_location,
            scope,
            scope_state,
            scope_characters,
            ..
        } => {
            print_identity(id, *kind, title);
            print_source(source, current_location);
            print_bounded("Scope", scope, *scope_state, *scope_characters);
        }
    }
    println!(
        "Current validation: navigation and source consistency only; mathematics is not validated."
    );
    println!("Data notice: {NOTICE}");
}

fn print_identity(id: &Id, kind: Kind, title: &str) {
    println!("ID: {id}\nKind: {kind}\nTitle: {title}");
}

fn print_source(source: &Source, location: &Location) {
    println!("Source selector: {}", source_selector(source));
    println!("Current location: {}", display_location(location));
}

fn print_bounded(
    label: &str,
    value: &Option<String>,
    state: FieldState,
    characters: Option<usize>,
) {
    match state {
        FieldState::Present => println!("{label}: {}", value.as_deref().unwrap()),
        FieldState::Missing => println!("{label}: not separately recorded"),
        FieldState::OmittedOverBudget => println!(
            "{label}: omitted because its exact {} characters exceed the head budget; use show",
            characters.unwrap()
        ),
    }
}

fn show(repository: &mut Repository, id: &Id, as_json: bool) -> Result<()> {
    let entry = repository.entry(id)?;
    let (source, raw, documents) = match &entry {
        Entry::Experiment(experiment) => {
            if let Some(path) = repository.preferred_experiment_doc(experiment) {
                let source = Source::File { path };
                let raw = repository.resolve(&source)?.raw;
                (Some(source), Some(raw), Vec::new())
            } else {
                let directory = repository.resolver.path(&experiment.path)?;
                let entries = fs::read_dir(&directory)
                    .map_err(|error| format!("cannot list {}: {error}", experiment.path))?;
                let mut documents = Vec::new();
                for entry in entries {
                    let entry = entry.map_err(|error| {
                        format!("cannot read {} directory entry: {error}", experiment.path)
                    })?;
                    let path = entry.path();
                    if path.is_file() && path.extension().is_some_and(|extension| extension == "md")
                    {
                        documents.push(format!(
                            "{}/{}",
                            experiment.path,
                            entry.file_name().to_string_lossy()
                        ));
                    }
                }
                documents.sort();
                (None, None, documents)
            }
        }
        _ => {
            let source = entry.source().unwrap().clone();
            let raw = repository.resolve(&source)?.raw;
            (Some(source), Some(raw), Vec::new())
        }
    };
    if as_json {
        let content = raw
            .as_deref()
            .map(std::str::from_utf8)
            .transpose()
            .map_err(|error| format!("source body is not UTF-8: {error}"))?;
        print_json(&json!({
            "id": id,
            "kind": entry.kind(),
            "source": source,
            "content": content,
            "documents": documents,
            "data_notice": NOTICE,
        }))
    } else if let Some(raw) = raw {
        eprintln!("Data notice: {NOTICE}");
        io::stdout()
            .write_all(&raw)
            .map_err(|error| format!("cannot write source bytes: {error}"))
    } else {
        println!("No RESULT.md, STATEMENT.md, or README.md for {id}.");
        if documents.is_empty() {
            println!("No root packet documents found.");
        } else {
            println!("Root packet documents:");
            for document in documents.iter().take(50) {
                println!("{document}");
            }
            if documents.len() > 50 {
                println!(
                    "{} additional root packet documents omitted.",
                    documents.len() - 50
                );
            }
        }
        Ok(())
    }
}

fn location(resolved: &ResolvedSource) -> Location {
    Location {
        path: resolved.path.clone(),
        line: resolved.line,
    }
}

fn display_location(location: &Location) -> String {
    format!("{}:{}", location.path, location.line)
}

fn print_json(value: &impl serde::Serialize) -> Result<()> {
    println!(
        "{}",
        serde_json::to_string_pretty(value)
            .map_err(|error| format!("cannot serialize JSON output: {error}"))?
    );
    Ok(())
}
