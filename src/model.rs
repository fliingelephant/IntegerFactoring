use crate::id::{Id, Kind};
use clap::ValueEnum;
use serde::{Deserialize, Serialize};
use std::fmt::{self, Display};

#[derive(
    Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize, ValueEnum,
)]
#[serde(rename_all = "lowercase")]
#[clap(rename_all = "lowercase")]
pub enum Table {
    Routes,
    Runs,
}

impl Display for Table {
    fn fmt(&self, output: &mut fmt::Formatter<'_>) -> fmt::Result {
        output.write_str(match self {
            Self::Routes => "routes",
            Self::Runs => "runs",
        })
    }
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(tag = "kind", rename_all = "lowercase", deny_unknown_fields)]
pub enum Source {
    Record {
        path: String,
        id: Id,
    },
    Row {
        path: String,
        table: Table,
        key: String,
    },
    Field {
        path: String,
        field: String,
    },
    File {
        path: String,
    },
}

impl Source {
    pub fn path(&self) -> &str {
        match self {
            Self::Record { path, .. }
            | Self::Row { path, .. }
            | Self::Field { path, .. }
            | Self::File { path } => path,
        }
    }
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct RecordMeta {
    pub id: Id,
    pub kind: Kind,
    pub title: String,
    pub source: Source,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub recorded_status: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub scope: Option<String>,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct RecordCatalog {
    pub schema_version: u32,
    #[serde(default)]
    pub records: Vec<RecordMeta>,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct RouteMeta {
    pub id: Id,
    pub title: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub summary: Option<String>,
    pub source: Source,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct RouteCatalog {
    pub schema_version: u32,
    #[serde(default)]
    pub routes: Vec<RouteMeta>,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ExperimentMeta {
    pub id: Id,
    pub path: String,
    #[serde(default)]
    pub route_ids: Vec<Id>,
    #[serde(default)]
    pub route_evidence: Vec<Source>,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ExperimentCatalog {
    pub schema_version: u32,
    #[serde(default)]
    pub experiments: Vec<ExperimentMeta>,
}

#[derive(
    Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize, ValueEnum,
)]
#[serde(rename_all = "lowercase")]
#[clap(rename_all = "lowercase")]
pub enum Relation {
    Uses,
    Requires,
    Supports,
    Refutes,
}

impl Relation {
    pub fn is_dependency(self) -> bool {
        matches!(self, Self::Uses | Self::Requires)
    }
}

impl Display for Relation {
    fn fmt(&self, output: &mut fmt::Formatter<'_>) -> fmt::Result {
        output.write_str(match self {
            Self::Uses => "uses",
            Self::Requires => "requires",
            Self::Supports => "supports",
            Self::Refutes => "refutes",
        })
    }
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct GraphNode {
    pub id: Id,
    pub kind: Kind,
    pub title: String,
    pub source: Source,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub scope: Option<String>,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct GraphEdge {
    pub from: Id,
    pub to: Id,
    pub relation: Relation,
    pub evidence: Vec<Source>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub note: Option<String>,
}

#[derive(Debug, Clone, Eq, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct GraphCatalog {
    pub schema_version: u32,
    #[serde(default)]
    pub nodes: Vec<GraphNode>,
    #[serde(default)]
    pub edges: Vec<GraphEdge>,
}

impl Default for GraphCatalog {
    fn default() -> Self {
        Self {
            schema_version: 1,
            nodes: Vec::new(),
            edges: Vec::new(),
        }
    }
}

#[derive(Debug, Clone, Copy, Eq, PartialEq, ValueEnum)]
#[clap(rename_all = "lowercase")]
pub enum GraphFormat {
    Text,
    Json,
    Mermaid,
}

impl Display for GraphFormat {
    fn fmt(&self, output: &mut fmt::Formatter<'_>) -> fmt::Result {
        output.write_str(match self {
            Self::Text => "text",
            Self::Json => "json",
            Self::Mermaid => "mermaid",
        })
    }
}
