use clap::ValueEnum;
use serde::{Deserialize, Deserializer, Serialize, Serializer};
use std::fmt::{self, Display};
use std::str::FromStr;

#[derive(Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub enum RecordClass {
    Result,
    Closure,
    Note,
}

impl RecordClass {
    pub fn prefix(self) -> char {
        match self {
            Self::Result => 'P',
            Self::Closure => 'X',
            Self::Note => 'C',
        }
    }
}

#[derive(Debug, Clone, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct RecordId {
    pub class: RecordClass,
    pub number: u32,
}

#[derive(Debug, Clone, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub struct RouteId {
    pub number: u32,
    pub branch: Option<char>,
}

impl RouteId {
    pub fn code(&self) -> String {
        match self.branch {
            Some(branch) => format!("F{:02}-{branch}", self.number),
            None => format!("F{:02}", self.number),
        }
    }
}

#[derive(Debug, Clone, Eq, PartialEq, Ord, PartialOrd, Hash)]
pub enum Id {
    Record(RecordId),
    Route(RouteId),
    Experiment(String),
    Goal(String),
    Question(String),
}

impl Id {
    pub fn kind(&self) -> Kind {
        match self {
            Self::Record(record) => match record.class {
                RecordClass::Result => Kind::Result,
                RecordClass::Closure => Kind::Closure,
                RecordClass::Note => Kind::Note,
            },
            Self::Route(_) => Kind::Route,
            Self::Experiment(_) => Kind::Experiment,
            Self::Goal(_) => Kind::Goal,
            Self::Question(_) => Kind::Question,
        }
    }

    pub fn as_route(&self) -> Option<&RouteId> {
        match self {
            Self::Route(route) => Some(route),
            _ => None,
        }
    }

    pub fn experiment_name(&self) -> Option<&str> {
        match self {
            Self::Experiment(name) => Some(name),
            _ => None,
        }
    }
}

impl Display for Id {
    fn fmt(&self, output: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Record(record) => write!(output, "{}{:02}", record.class.prefix(), record.number),
            Self::Route(route) => write!(output, "route:{}", route.code()),
            Self::Experiment(name) => write!(output, "experiment:{name}"),
            Self::Goal(slug) => write!(output, "goal:{slug}"),
            Self::Question(slug) => write!(output, "question:{slug}"),
        }
    }
}

fn valid_slug(value: &str) -> bool {
    !value.is_empty()
        && value.bytes().all(|byte| {
            byte.is_ascii_lowercase() || byte.is_ascii_digit() || byte == b'-' || byte == b'_'
        })
        && value.as_bytes()[0].is_ascii_alphanumeric()
        && value.as_bytes()[value.len() - 1].is_ascii_alphanumeric()
}

fn parse_route(value: &str) -> Result<RouteId, String> {
    let code = value
        .strip_prefix("route:F")
        .ok_or_else(|| format!("invalid route ID: {value}"))?;
    let (number, branch) = match code.split_once('-') {
        Some((number, branch)) if branch.len() == 1 => {
            let branch = branch.chars().next().unwrap();
            if !branch.is_ascii_uppercase() {
                return Err(format!("invalid route branch: {value}"));
            }
            (number, Some(branch))
        }
        Some(_) => return Err(format!("invalid route ID: {value}")),
        None => (code, None),
    };
    if number.len() < 2 || !number.bytes().all(|byte| byte.is_ascii_digit()) {
        return Err(format!("invalid route ID: {value}"));
    }
    let route = RouteId {
        number: number
            .parse()
            .map_err(|_| format!("invalid route ID: {value}"))?,
        branch,
    };
    if format!("route:{}", route.code()) != value {
        return Err(format!("noncanonical route ID: {value}"));
    }
    Ok(route)
}

impl FromStr for Id {
    type Err = String;

    fn from_str(value: &str) -> Result<Self, Self::Err> {
        if let Some(name) = value.strip_prefix("experiment:") {
            let valid = name.starts_with('F')
                && name
                    .as_bytes()
                    .get(1)
                    .copied()
                    .is_some_and(|byte| byte.is_ascii_digit())
                && name
                    .bytes()
                    .all(|byte| byte.is_ascii_alphanumeric() || byte == b'_' || byte == b'-');
            return valid
                .then(|| Self::Experiment(name.to_owned()))
                .ok_or_else(|| format!("invalid experiment ID: {value}"));
        }
        if value.starts_with("route:") {
            return parse_route(value).map(Self::Route);
        }
        for (prefix, class) in [
            ('P', RecordClass::Result),
            ('X', RecordClass::Closure),
            ('C', RecordClass::Note),
        ] {
            if let Some(number) = value.strip_prefix(prefix) {
                if number.len() < 2 || !number.bytes().all(|byte| byte.is_ascii_digit()) {
                    return Err(format!("invalid record ID: {value}"));
                }
                let id = Self::Record(RecordId {
                    class,
                    number: number
                        .parse()
                        .map_err(|_| format!("invalid record ID: {value}"))?,
                });
                return (id.to_string() == value)
                    .then_some(id)
                    .ok_or_else(|| format!("noncanonical record ID: {value}"));
            }
        }
        for (prefix, constructor) in [
            ("goal:", Self::Goal as fn(String) -> Self),
            ("question:", Self::Question as fn(String) -> Self),
        ] {
            if let Some(slug) = value.strip_prefix(prefix) {
                return valid_slug(slug)
                    .then(|| constructor(slug.to_owned()))
                    .ok_or_else(|| format!("invalid {prefix} ID: {value}"));
            }
        }
        Err(format!("unknown ID syntax: {value}"))
    }
}

impl Serialize for Id {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        serializer.serialize_str(&self.to_string())
    }
}

impl<'de> Deserialize<'de> for Id {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        String::deserialize(deserializer)?
            .parse()
            .map_err(serde::de::Error::custom)
    }
}

#[derive(
    Debug, Clone, Copy, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize, ValueEnum,
)]
#[serde(rename_all = "kebab-case")]
#[clap(rename_all = "kebab-case")]
pub enum Kind {
    Result,
    Closure,
    Note,
    Route,
    Experiment,
    Goal,
    Question,
}

impl Display for Kind {
    fn fmt(&self, output: &mut fmt::Formatter<'_>) -> fmt::Result {
        let name = match self {
            Self::Result => "result",
            Self::Closure => "closure",
            Self::Note => "note",
            Self::Route => "route",
            Self::Experiment => "experiment",
            Self::Goal => "goal",
            Self::Question => "question",
        };
        output.write_str(name)
    }
}
