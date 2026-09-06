use serde_json::Value;
use std::fs;
use std::path::PathBuf;
use std::process::{Command, Output};
use std::sync::atomic::{AtomicU64, Ordering};

static NEXT_FIXTURE: AtomicU64 = AtomicU64::new(0);
const ROUTE_ROW: &str = "| F12 | Example route |\n";
const RUN_ROW: &str = "| F13-R01 | F12 | Example run |\n";

struct Fixture {
    root: PathBuf,
}

impl Fixture {
    fn new() -> Self {
        let root = std::env::temp_dir().join(format!(
            "integer-factoring-rust-{}-{}",
            std::process::id(),
            NEXT_FIXTURE.fetch_add(1, Ordering::Relaxed)
        ));
        fs::create_dir_all(root.join("research")).unwrap();
        fs::create_dir_all(root.join("notes")).unwrap();
        fs::create_dir_all(root.join("experiments/F13_example")).unwrap();
        fs::write(
            root.join("PROVED.md"),
            "## P01 — Fixture result\n\n**Status:** recorded.\n\nThe hidden Frobenius mechanism appears only in this body.\n",
        )
        .unwrap();
        fs::write(
            root.join("FAILED.md"),
            "## X01 — Fixture closure\n\n**Status:** recorded.\n",
        )
        .unwrap();
        fs::write(
            root.join("notes/Progress.md"),
            "### C00 — Fixture note\n\n**Status:** recorded.\n",
        )
        .unwrap();
        fs::write(root.join("REGISTRY.md"), registry()).unwrap();
        fs::write(
            root.join("experiments/F13_example/RESULT.md"),
            "# Packet\n\n**Family:** F12.\n\n## Result\nFixture only.\n",
        )
        .unwrap();
        fs::write(root.join("research/routes.toml"), routes()).unwrap();
        fs::write(root.join("research/experiments.toml"), experiments()).unwrap();
        let fixture = Self { root };
        fixture.success(&["sync"]);
        fixture
    }

    fn run(&self, arguments: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_research"))
            .args(arguments)
            .current_dir(&self.root)
            .output()
            .unwrap()
    }

    fn success(&self, arguments: &[&str]) -> Output {
        let output = self.run(arguments);
        assert!(
            output.status.success(),
            "{}",
            String::from_utf8_lossy(&output.stderr)
        );
        output
    }

    fn failure(&self, arguments: &[&str]) {
        assert!(!self.run(arguments).status.success());
    }

    fn write(&self, path: &str, content: &str) {
        fs::write(self.root.join(path), content).unwrap();
    }
}

impl Drop for Fixture {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.root);
    }
}

fn registry() -> String {
    format!(
        "# Registry\n\n| ID | Title |\n| --- | --- |\n{ROUTE_ROW}| F01 | Other route |\n\n\
         ## Computation ledger\n\n| Run | Family | Purpose |\n| --- | --- | --- |\n\
         | F12 | F01 | Same key in another table |\n{RUN_ROW}"
    )
}

fn routes() -> &'static str {
    "schema_version = 3\n\n[[routes]]\nid = \"route:F12\"\ntitle = \"Example route\"\n\
     source = { kind = \"row\", path = \"REGISTRY.md\", table = \"routes\", key = \"F12\" }\n"
}

fn experiments() -> &'static str {
    "schema_version = 3\n\n[[experiments]]\nid = \"experiment:F13_example\"\n\
     path = \"experiments/F13_example\"\nroute_ids = [\"route:F12\"]\n\
     route_evidence = [\n\
       { kind = \"row\", path = \"REGISTRY.md\", table = \"runs\", key = \"F13-R01\" },\n\
       { kind = \"field\", path = \"experiments/F13_example/RESULT.md\", field = \"Family\" },\n\
     ]\n"
}

#[test]
fn stable_selectors_survive_insertion_reordering_and_field_reflow() {
    let fixture = Fixture::new();
    fixture.success(&["check"]);
    let before = ["catalog.toml", "routes.toml", "experiments.toml"]
        .map(|name| fs::read(fixture.root.join("research").join(name)).unwrap());
    fixture.success(&["sync"]);
    let after = ["catalog.toml", "routes.toml", "experiments.toml"]
        .map(|name| fs::read(fixture.root.join("research").join(name)).unwrap());
    assert_eq!(before, after);
    for content in after {
        assert!(content.ends_with(b"\n"));
        assert!(!content.ends_with(b"\n\n"));
    }
    assert_eq!(
        fixture.success(&["show", "route:F12"]).stdout,
        ROUTE_ROW.as_bytes()
    );
    let reordered = registry()
        .replace(ROUTE_ROW, "")
        .replace(
            "| F01 | Other route |\n",
            &format!("| F01 | Other route |\n{ROUTE_ROW}"),
        )
        .replace(RUN_ROW, "")
        .replace(
            "| F12 | F01 | Same key in another table |\n",
            &format!("{RUN_ROW}| F12 | F01 | Same key in another table |\n"),
        );
    fixture.write("REGISTRY.md", &("Extra lines.\n\n".to_owned() + &reordered));
    fixture.write(
        "experiments/F13_example/RESULT.md",
        "# Packet\n\n**Family:**\nF12.\nContinuation.\n**Status:** F99 is unrelated.\n",
    );
    fixture.success(&["check"]);
    assert_eq!(
        fixture.success(&["show", "route:F12"]).stdout,
        ROUTE_ROW.as_bytes()
    );
}

#[test]
fn malformed_headings_and_invalid_selectors_fail() {
    let fixture = Fixture::new();
    fixture.write("PROVED.md", "## P01: malformed\n");
    fixture.failure(&["sync"]);

    for changed in [
        registry().replace(ROUTE_ROW, ""),
        registry().replace(ROUTE_ROW, &(ROUTE_ROW.to_owned() + ROUTE_ROW)),
        registry().replace(RUN_ROW, ""),
        registry() + RUN_ROW,
    ] {
        let case = Fixture::new();
        case.write("REGISTRY.md", &changed);
        case.failure(&["check"]);
    }

    let positional = Fixture::new();
    positional.write(
        "research/routes.toml",
        &routes().replace(
            "{ kind = \"row\", path = \"REGISTRY.md\", table = \"routes\", key = \"F12\" }",
            "\"REGISTRY.md:5\"",
        ),
    );
    positional.failure(&["check"]);

    let duplicate_field = Fixture::new();
    duplicate_field.write(
        "experiments/F13_example/RESULT.md",
        "**Family:** F12.\n\n**Family:** F12.\n",
    );
    duplicate_field.failure(&["check"]);
}

#[test]
fn full_text_query_finds_body_only_terms() {
    let fixture = Fixture::new();
    let bare = fixture.run(&["head", "F13"]);
    assert!(!bare.status.success());
    let error = String::from_utf8_lossy(&bare.stderr);
    assert!(error.contains("experiment:F13_example"));
    assert!(!error.contains("route:F13"));
    let output = fixture.success(&["list", "--query", "Frobenius", "--kind", "result", "--json"]);
    let value: Value = serde_json::from_slice(&output.stdout).unwrap();
    assert_eq!(value["matches"], 1);
    assert_eq!(value["items"][0]["id"], "P01");
    assert!(
        value["items"][0]["snippet"]
            .as_str()
            .unwrap()
            .contains("Frobenius")
    );
    let head: Value =
        serde_json::from_slice(&fixture.success(&["head", "P01", "--json"]).stdout).unwrap();
    assert_eq!(head["recorded_status_state"], "present");
    let shown: Value =
        serde_json::from_slice(&fixture.success(&["show", "P01", "--json"]).stdout).unwrap();
    assert!(shown["content"].as_str().unwrap().contains("Frobenius"));
}

#[test]
fn empty_repository_syncs_and_checks() {
    let fixture = Fixture::new();
    fixture.write("PROVED.md", "");
    fixture.write("FAILED.md", "");
    fixture.write("notes/Progress.md", "");
    fixture.write(
        "REGISTRY.md",
        "| ID | Title |\n| --- | --- |\n\n## Computation ledger\n\n| Run | Family |\n| --- | --- |\n",
    );
    fs::remove_dir_all(fixture.root.join("experiments/F13_example")).unwrap();
    fixture.write("research/routes.toml", "schema_version = 3\n");
    fixture.write("research/experiments.toml", "schema_version = 3\n");
    let synced: Value =
        serde_json::from_slice(&fixture.success(&["sync", "--json"]).stdout).unwrap();
    assert_eq!(synced["records"], 0);
    let output = fixture.success(&["check", "--json"]);
    let value: Value = serde_json::from_slice(&output.stdout).unwrap();
    assert_eq!(value["records"], 0);
    assert_eq!(value["routes"], 0);
    assert_eq!(value["experiments"], 0);
}

#[test]
fn graph_distinguishes_dependencies_from_support_and_checks_cycles() {
    let fixture = Fixture::new();
    fixture.write("EVIDENCE.md", "Exact fixture evidence.\n");
    fixture.write(
        "research/graph.toml",
        "schema_version = 1\n\n\
         [[nodes]]\nid = \"goal:main\"\nkind = \"goal\"\ntitle = \"Main goal\"\n\
         source = { kind = \"file\", path = \"EVIDENCE.md\" }\n\n\
         [[nodes]]\nid = \"question:gap\"\nkind = \"question\"\ntitle = \"Open gap\"\n\
         source = { kind = \"file\", path = \"EVIDENCE.md\" }\n\n\
         [[edges]]\nfrom = \"goal:main\"\nto = \"question:gap\"\nrelation = \"requires\"\n\
         evidence = [{ kind = \"file\", path = \"EVIDENCE.md\" }]\n\n\
         [[edges]]\nfrom = \"P01\"\nto = \"goal:main\"\nrelation = \"supports\"\n\
         evidence = [{ kind = \"record\", path = \"PROVED.md\", id = \"P01\" }]\n\n\
         [[edges]]\nfrom = \"goal:main\"\nto = \"P01\"\nrelation = \"refutes\"\n\
         evidence = [{ kind = \"file\", path = \"EVIDENCE.md\" }]\n\n\
         [[edges]]\nfrom = \"P01\"\nto = \"X01\"\nrelation = \"uses\"\n\
         evidence = [{ kind = \"file\", path = \"EVIDENCE.md\" }]\n\n\
         [[edges]]\nfrom = \"experiment:F13_example\"\nto = \"P01\"\nrelation = \"supports\"\n\
         evidence = [{ kind = \"file\", path = \"EVIDENCE.md\" }]\n",
    );
    fixture.success(&["check"]);
    let output = fixture.success(&["graph", "goal:main", "--format", "json"]);
    let value: Value = serde_json::from_slice(&output.stdout).unwrap();
    let ids: Vec<_> = value["nodes"]
        .as_array()
        .unwrap()
        .iter()
        .map(|node| node["id"].as_str().unwrap())
        .collect();
    assert!(ids.contains(&"goal:main"));
    assert!(ids.contains(&"question:gap"));
    assert!(ids.contains(&"P01"));
    assert!(!ids.contains(&"X01"));
    let source_view: Value = serde_json::from_slice(
        &fixture
            .success(&["graph", "experiment:F13_example", "--format", "json"])
            .stdout,
    )
    .unwrap();
    assert!(source_view["edges"].as_array().unwrap().iter().any(|edge| {
        edge["from"] == "experiment:F13_example"
            && edge["to"] == "P01"
            && edge["relation"] == "supports"
    }));
    assert!(
        !source_view["nodes"]
            .as_array()
            .unwrap()
            .iter()
            .any(|node| node["id"] == "X01")
    );

    let mut reordered_graph = fs::read_to_string(fixture.root.join("research/graph.toml")).unwrap();
    let support_start = reordered_graph
        .rfind("[[edges]]\nfrom = \"experiment:F13_example\"")
        .unwrap();
    let support_block = reordered_graph.split_off(support_start);
    let first_edge = reordered_graph.find("[[edges]]").unwrap();
    reordered_graph.insert_str(first_edge, &support_block);
    fixture.write("research/graph.toml", &reordered_graph);
    let reordered_view: Value = serde_json::from_slice(
        &fixture
            .success(&["graph", "goal:main", "--format", "json"])
            .stdout,
    )
    .unwrap();
    let edge_keys = |graph: &Value| {
        let mut keys = graph["edges"]
            .as_array()
            .unwrap()
            .iter()
            .map(|edge| {
                format!(
                    "{}:{}:{}",
                    edge["from"].as_str().unwrap(),
                    edge["relation"].as_str().unwrap(),
                    edge["to"].as_str().unwrap()
                )
            })
            .collect::<Vec<_>>();
        keys.sort();
        keys
    };
    assert_eq!(edge_keys(&value), edge_keys(&reordered_view));

    fixture.write(
        "research/graph.toml",
        &fs::read_to_string(fixture.root.join("research/graph.toml"))
            .unwrap()
            .replace(
                "[[edges]]\nfrom = \"P01\"\nto = \"X01\"",
                "[[edges]]\nfrom = \"question:gap\"\nto = \"goal:main\"",
            )
            .replace("relation = \"uses\"", "relation = \"requires\""),
    );
    fixture.failure(&["check"]);
}

#[test]
fn parent_route_does_not_match_subroute_and_missing_graph_nodes_fail() {
    let fixture = Fixture::new();
    fixture.write("research/routes.toml", &routes().replace("F12", "F26"));
    fixture.write(
        "research/experiments.toml",
        &experiments().replace("route:F12", "route:F26"),
    );
    fixture.write(
        "REGISTRY.md",
        &registry()
            .replace(ROUTE_ROW, &ROUTE_ROW.replace("F12", "F26"))
            .replace(RUN_ROW, &RUN_ROW.replace("| F12 |", "| F26-Q |")),
    );
    fixture.write("experiments/F13_example/RESULT.md", "**Family:** F26-Q.\n");
    fixture.failure(&["check"]);

    let missing = Fixture::new();
    missing.write(
        "research/graph.toml",
        "schema_version = 1\n[[edges]]\nfrom = \"P01\"\nto = \"question:missing\"\n\
         relation = \"supports\"\nevidence = [{ kind = \"record\", path = \"PROVED.md\", id = \"P01\" }]\n",
    );
    missing.failure(&["check"]);
}
