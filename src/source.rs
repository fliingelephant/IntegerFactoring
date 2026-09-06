use crate::Result;
use crate::id::{Id, Kind, RecordClass};
use crate::model::{Source, Table};
use serde::Serialize;
use std::collections::{BTreeMap, HashMap};
use std::fs;
use std::path::{Component, Path, PathBuf};

const LEDGERS: [(&str, RecordClass, usize); 3] = [
    ("PROVED.md", RecordClass::Result, 2),
    ("FAILED.md", RecordClass::Closure, 2),
    ("notes/Progress.md", RecordClass::Note, 3),
];

#[derive(Debug, Clone)]
struct Line {
    start: usize,
    text_end: usize,
}

#[derive(Debug, Clone)]
struct Document {
    bytes: Vec<u8>,
    lines: Vec<Line>,
}

impl Document {
    fn new(bytes: Vec<u8>, path: &str) -> Result<Self> {
        let text =
            std::str::from_utf8(&bytes).map_err(|error| format!("{path} is not UTF-8: {error}"))?;
        let mut lines = Vec::new();
        let mut start = 0;
        for part in text.split_inclusive('\n') {
            let end = start + part.len();
            let without_newline = part.strip_suffix('\n').unwrap_or(part);
            let content = without_newline
                .strip_suffix('\r')
                .unwrap_or(without_newline);
            lines.push(Line {
                start,
                text_end: start + content.len(),
            });
            start = end;
        }
        if start < bytes.len() {
            lines.push(Line {
                start,
                text_end: bytes.len(),
            });
        }
        Ok(Self { bytes, lines })
    }

    fn text(&self, index: usize) -> &str {
        std::str::from_utf8(&self.bytes[self.lines[index].start..self.lines[index].text_end])
            .unwrap()
    }

    fn bytes(&self, start: usize, end: usize) -> Vec<u8> {
        let byte_start = self.lines[start].start;
        let byte_end = if end < self.lines.len() {
            self.lines[end].start
        } else {
            self.bytes.len()
        };
        self.bytes[byte_start..byte_end].to_vec()
    }
}

#[derive(Debug, Clone, Eq, PartialEq)]
pub struct ParsedRecord {
    pub id: Id,
    pub kind: Kind,
    pub title: String,
    pub path: String,
    pub line: usize,
    pub raw: Vec<u8>,
    pub recorded_status: Option<String>,
    pub scope: Option<String>,
}

impl ParsedRecord {
    pub fn source(&self) -> Source {
        Source::Record {
            path: self.path.clone(),
            id: self.id.clone(),
        }
    }
}

#[derive(Debug, Clone)]
struct Located {
    line: usize,
    raw: Vec<u8>,
    cells: Option<Vec<String>>,
}

type RowIndex = BTreeMap<String, Vec<Located>>;
type TableIndex = BTreeMap<Table, (usize, RowIndex)>;

#[derive(Debug, Clone, Serialize)]
pub struct ResolvedSource {
    pub path: String,
    pub line: usize,
    #[serde(skip)]
    pub raw: Vec<u8>,
    #[serde(skip)]
    pub cells: Option<Vec<String>>,
}

pub struct Resolver {
    root: PathBuf,
    documents: HashMap<String, Document>,
    tables: HashMap<String, TableIndex>,
    fields: HashMap<String, BTreeMap<String, Vec<Located>>>,
}

impl Resolver {
    pub fn new(root: impl AsRef<Path>) -> Result<Self> {
        let root = fs::canonicalize(root.as_ref())
            .map_err(|error| format!("cannot resolve repository root: {error}"))?;
        Ok(Self {
            root,
            documents: HashMap::new(),
            tables: HashMap::new(),
            fields: HashMap::new(),
        })
    }

    pub fn root(&self) -> &Path {
        &self.root
    }

    pub fn path(&self, relative: &str) -> Result<PathBuf> {
        let relative_path = Path::new(relative);
        if relative_path.is_absolute()
            || relative_path
                .components()
                .any(|part| !matches!(part, Component::Normal(_)))
        {
            return Err(format!("path must be repository-relative: {relative}"));
        }
        let joined = self.root.join(relative_path);
        let resolved = fs::canonicalize(&joined)
            .map_err(|error| format!("cannot resolve {relative}: {error}"))?;
        if !resolved.starts_with(&self.root) {
            return Err(format!("path leaves repository: {relative}"));
        }
        Ok(resolved)
    }

    fn document(&mut self, relative: &str) -> Result<&Document> {
        if !self.documents.contains_key(relative) {
            let path = self.path(relative)?;
            if !path.is_file() {
                return Err(format!("source is not a file: {relative}"));
            }
            let bytes =
                fs::read(&path).map_err(|error| format!("cannot read {relative}: {error}"))?;
            self.documents
                .insert(relative.to_owned(), Document::new(bytes, relative)?);
        }
        Ok(&self.documents[relative])
    }

    pub fn parse_records(&mut self) -> Result<BTreeMap<Id, ParsedRecord>> {
        let mut records = BTreeMap::new();
        for (path, class, level) in LEDGERS {
            let parsed = {
                let document = self.document(path)?;
                parse_ledger(document, path, class, level)?
            };
            for record in parsed {
                let id = record.id.clone();
                if records.insert(id.clone(), record).is_some() {
                    return Err(format!("duplicate record ID: {id}"));
                }
            }
        }
        Ok(records)
    }

    fn table_index(&mut self, path: &str, table: Table) -> Result<&BTreeMap<String, Vec<Located>>> {
        if path != "REGISTRY.md" {
            return Err(format!("row selectors require REGISTRY.md, found {path}"));
        }
        if !self.tables.contains_key(path) {
            let parsed = {
                let document = self.document(path)?;
                parse_tables(document)
            };
            self.tables.insert(path.to_owned(), parsed);
        }
        let (headers, rows) = self.tables[path]
            .get(&table)
            .ok_or_else(|| format!("missing {table} table index"))?;
        if *headers != 1 {
            return Err(format!(
                "expected exactly one {table} table header, found {headers}"
            ));
        }
        Ok(rows)
    }

    pub fn rows(&mut self, table: Table) -> Result<Vec<(String, Vec<String>)>> {
        let rows = self.table_index("REGISTRY.md", table)?;
        let mut result = Vec::new();
        for (key, matches) in rows {
            if matches.len() != 1 {
                return Err(format!(
                    "REGISTRY.md {table} key {key} must occur exactly once, found {}",
                    matches.len()
                ));
            }
            result.push((key.clone(), matches[0].cells.clone().unwrap_or_default()));
        }
        Ok(result)
    }

    fn field_index(&mut self, path: &str) -> Result<&BTreeMap<String, Vec<Located>>> {
        if !self.fields.contains_key(path) {
            let parsed = {
                let document = self.document(path)?;
                parse_fields(document)
            };
            self.fields.insert(path.to_owned(), parsed);
        }
        Ok(&self.fields[path])
    }

    pub fn resolve(
        &mut self,
        source: &Source,
        records: &BTreeMap<Id, ParsedRecord>,
    ) -> Result<ResolvedSource> {
        match source {
            Source::Record { path, id } => {
                let record = records
                    .get(id)
                    .ok_or_else(|| format!("record source does not exist: {id}"))?;
                if record.path != *path {
                    return Err(format!("record source path mismatch for {id}: {path}"));
                }
                Ok(ResolvedSource {
                    path: path.clone(),
                    line: record.line,
                    raw: record.raw.clone(),
                    cells: None,
                })
            }
            Source::Row { path, table, key } => {
                let matches = self
                    .table_index(path, *table)?
                    .get(key)
                    .map(Vec::as_slice)
                    .unwrap_or_default();
                exact_match(path, &format!("{table} row {key}"), matches)
            }
            Source::Field { path, field } => {
                let matches = self
                    .field_index(path)?
                    .get(field)
                    .map(Vec::as_slice)
                    .unwrap_or_default();
                exact_match(path, &format!("field {field}"), matches)
            }
            Source::File { path } => {
                let raw = self.document(path)?.bytes.clone();
                Ok(ResolvedSource {
                    path: path.clone(),
                    line: 1,
                    raw,
                    cells: None,
                })
            }
        }
    }
}

fn exact_match(path: &str, selector: &str, matches: &[Located]) -> Result<ResolvedSource> {
    if matches.len() != 1 {
        return Err(format!(
            "source must resolve exactly once: {path} {selector} ({} matches)",
            matches.len()
        ));
    }
    let found = &matches[0];
    Ok(ResolvedSource {
        path: path.to_owned(),
        line: found.line,
        raw: found.raw.clone(),
        cells: found.cells.clone(),
    })
}

fn heading_candidate(line: &str) -> Option<(usize, char)> {
    let level = line.bytes().take_while(|byte| *byte == b'#').count();
    let rest = line.get(level..)?.strip_prefix(' ')?;
    let mut bytes = rest.bytes();
    let prefix = bytes.next()? as char;
    (matches!(prefix, 'P' | 'X' | 'C') && bytes.next().is_some_and(|byte| byte.is_ascii_digit()))
        .then_some((level, prefix))
}

fn parse_heading(line: &str, class: RecordClass, level: usize) -> Result<Option<(Id, String)>> {
    let Some((found_level, prefix)) = heading_candidate(line) else {
        return Ok(None);
    };
    if found_level != level || prefix != class.prefix() {
        return Err(format!("malformed or misplaced record heading: {line}"));
    }
    let rest = line
        .strip_prefix(&format!("{} ", "#".repeat(level)))
        .ok_or_else(|| format!("malformed record heading: {line}"))?;
    let id_end = rest
        .find(char::is_whitespace)
        .ok_or_else(|| format!("record heading has no title: {line}"))?;
    let id: Id = rest[..id_end].parse()?;
    let tail = &rest[id_end..];
    let title = [" — ", " -- ", " - "]
        .into_iter()
        .find_map(|delimiter| tail.strip_prefix(delimiter))
        .ok_or_else(|| format!("record heading must use a supported dash separator: {line}"))?;
    Ok(Some((id, title.trim().to_owned())))
}

fn parse_ledger(
    document: &Document,
    path: &str,
    class: RecordClass,
    level: usize,
) -> Result<Vec<ParsedRecord>> {
    let mut starts = Vec::new();
    for index in 0..document.lines.len() {
        if let Some((id, title)) = parse_heading(document.text(index), class, level)? {
            starts.push((index, id, title));
        }
    }
    let mut records = Vec::new();
    for position in 0..starts.len() {
        let (start, id, first_title) = &starts[position];
        let start = *start;
        let end = starts
            .get(position + 1)
            .map(|next| next.0)
            .unwrap_or(document.lines.len());
        let mut title = vec![first_title.clone()];
        for index in start + 1..end {
            let continuation = document.text(index);
            if continuation.trim().is_empty() || continuation.starts_with("**") {
                break;
            }
            title.push(continuation.trim().to_owned());
        }
        records.push(ParsedRecord {
            id: id.clone(),
            kind: id.kind(),
            title: title.join(" "),
            path: path.to_owned(),
            line: start + 1,
            raw: document.bytes(start, end),
            recorded_status: labeled_value(document, start, end, "Status", false),
            scope: labeled_value(document, start, end, "Scope", true),
        });
    }
    Ok(records)
}

fn bold_label(line: &str) -> Option<(&str, &str)> {
    let rest = line.strip_prefix("**")?;
    for separator in [":**", ".**"] {
        if let Some(index) = rest.find(separator) {
            let label = &rest[..index];
            let value = rest[index + separator.len()..].trim_start();
            return Some((label, value));
        }
    }
    None
}

fn labeled_value(
    document: &Document,
    start: usize,
    end: usize,
    wanted: &str,
    complete: bool,
) -> Option<String> {
    for index in start..end {
        let Some((label, first)) = bold_label(document.text(index)) else {
            continue;
        };
        if label != wanted {
            continue;
        }
        let mut value = if first.is_empty() {
            Vec::new()
        } else {
            vec![first.to_owned()]
        };
        for more in index + 1..end {
            let text = document.text(more);
            if (!complete && text.trim().is_empty()) || (complete && bold_label(text).is_some()) {
                break;
            }
            value.push(text.to_owned());
        }
        let joined = value.join("\n");
        let trimmed = joined.trim();
        return (!trimmed.is_empty()).then(|| trimmed.to_owned());
    }
    None
}

fn markdown_cells(line: &str) -> Option<Vec<String>> {
    if !line.starts_with('|') || !line.ends_with('|') {
        return None;
    }
    Some(
        line[1..line.len() - 1]
            .split('|')
            .map(|cell| cell.trim().to_owned())
            .collect(),
    )
}

fn parse_tables(document: &Document) -> TableIndex {
    let parsed: Vec<_> = (0..document.lines.len())
        .map(|index| markdown_cells(document.text(index)))
        .collect();
    let mut result = BTreeMap::new();
    for (table, header) in [(Table::Routes, "ID"), (Table::Runs, "Run")] {
        let headers: Vec<_> = parsed
            .iter()
            .enumerate()
            .filter_map(|(index, cells)| {
                (cells.as_ref()?.first()?.as_str() == header).then_some(index)
            })
            .collect();
        let mut rows = BTreeMap::<String, Vec<Located>>::new();
        if headers.len() == 1 {
            let start = headers[0] + 1;
            let end = (start..document.lines.len())
                .find(|index| document.text(*index).starts_with("## "))
                .unwrap_or(document.lines.len());
            for (index, cells) in parsed.iter().enumerate().take(end).skip(start) {
                let Some(cells) = cells else {
                    continue;
                };
                let Some(key) = cells.first() else {
                    continue;
                };
                if key.is_empty() || key.bytes().all(|byte| byte == b'-') {
                    continue;
                }
                rows.entry(key.clone()).or_default().push(Located {
                    line: index + 1,
                    raw: document.bytes(index, index + 1),
                    cells: Some(cells.clone()),
                });
            }
        }
        result.insert(table, (headers.len(), rows));
    }
    result
}

fn parse_fields(document: &Document) -> BTreeMap<String, Vec<Located>> {
    let mut fields = BTreeMap::<String, Vec<Located>>::new();
    for start in 0..document.lines.len() {
        let Some((label, _)) = bold_label(document.text(start)) else {
            continue;
        };
        let mut end = start + 1;
        while end < document.lines.len() {
            let line = document.text(end);
            if line.trim().is_empty() || bold_label(line).is_some() || line.starts_with('#') {
                break;
            }
            end += 1;
        }
        fields.entry(label.to_owned()).or_default().push(Located {
            line: start + 1,
            raw: document.bytes(start, end),
            cells: None,
        });
    }
    fields
}

pub fn source_selector(source: &Source) -> String {
    fn quoted(value: &str) -> String {
        serde_json::to_string(value).unwrap()
    }
    match source {
        Source::Record { path, id } => format!(
            "{{ kind = \"record\", path = {}, id = {} }}",
            quoted(path),
            quoted(&id.to_string())
        ),
        Source::Row { path, table, key } => format!(
            "{{ kind = \"row\", path = {}, table = \"{}\", key = {} }}",
            quoted(path),
            table,
            quoted(key)
        ),
        Source::Field { path, field } => format!(
            "{{ kind = \"field\", path = {}, field = {} }}",
            quoted(path),
            quoted(field)
        ),
        Source::File { path } => format!("{{ kind = \"file\", path = {} }}", quoted(path)),
    }
}

pub fn contains_route_token(text: &str, token: &str) -> bool {
    text.match_indices(token).any(|(start, _)| {
        let before = text[..start].bytes().next_back();
        let after = text[start + token.len()..].bytes().next();
        let part = |byte: Option<u8>| {
            byte.is_some_and(|value| value.is_ascii_alphanumeric() || value == b'-')
        };
        !part(before) && !part(after)
    })
}
