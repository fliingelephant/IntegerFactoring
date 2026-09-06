#!/usr/bin/env bash
set -euo pipefail

experiment=F264-D03
work_dir=/root/IntegerFactoring_F264/F264-D03
out_dir="$work_dir/output"
log_dir="$work_dir/logs"
deadline=$((SECONDS + 14400))

mkdir -p "$out_dir" "$log_dir"
cd "$work_dir"

owned_output_bytes() {
  find "$out_dir" "$log_dir" -type f -printf '%s\n' 2>/dev/null \
    | awk '{sum += $1} END {print sum+0}'
}

incompatible_active() {
  local proc pid args cwd identity
  for proc in /proc/[0-9]*; do
    [[ -d "$proc" ]] || continue
    pid=${proc##*/}
    [[ "$pid" == "$$" || "$pid" == "$PPID" ]] && continue
    args=$(tr '\0' ' ' <"$proc/cmdline" 2>/dev/null || true)
    cwd=$(readlink "$proc/cwd" 2>/dev/null || true)
    identity="$args $cwd"
    case "$identity" in
      *F258-D01*|*F258-D02*|*F259-D01*|*F259-D02*|\
      *F260-D01*|*F260-D02*|*F261-D01*|*F261-D02*|\
      *F262-D01*|*F262-D02*|*F263-D01*|*F263-D02*|\
      *F264-D01*|*F264-D02*|\
      *F258_pell_resultant_ticket_scan*|\
      *F259_full_pell_lift_symbolic_search*|\
      *F260_las_vegas_integer_symbolic_search*|\
      *F261_beta2_centered_carry_scaling*|\
      *F262_polynomial_frobenius_lift_symbolic_search*|\
      *F263_hypergeometric_evaluator_symbolic_search*)
        echo "INCOMPATIBLE_PROCESS pid=$pid" >&2
        return 0
        ;;
    esac
  done
  return 1
}

refuse_overlap() {
  local gate=$1
  if incompatible_active; then
    echo "REFUSE_INCOMPATIBLE stage=$gate" >&2
    return 73
  fi
}

resource_gate() {
  local gate=$1
  local cpus available_kib disk_kib load1
  cpus=$(nproc)
  available_kib=$(awk '/MemAvailable:/ {print $2}' /proc/meminfo)
  disk_kib=$(df -Pk "$work_dir" | awk 'NR==2 {print $4}')
  load1=$(awk '{print $1}' /proc/loadavg)
  {
    echo "stage=$gate"
    echo "allowed_cpus=$cpus"
    echo "mem_available_kib=$available_kib"
    echo "disk_available_kib=$disk_kib"
    echo "load1=$load1"
    cat /proc/loadavg
    free -h
    df -h "$work_dir"
    ps -eo pid,ni,psr,pcpu,pmem,rss,etime,args --sort=-pcpu | sed -n '1,40p'
  } >"$log_dir/resource_${gate}.txt"
  (( cpus >= 8 )) || return 76
  (( available_kib >= 8388608 )) || return 76
  (( disk_kib >= 5242880 )) || return 76
  awk -v load="$load1" -v cpus="$cpus" \
    'BEGIN {exit !(load <= 3*cpus)}' || return 76
}

run_monitored() {
  local label=$1 stdout_path=$2 stderr_path=$3
  shift 3
  refuse_overlap "before_$label" || return $?
  resource_gate "before_$label" || return $?
  local bytes
  bytes=$(owned_output_bytes)
  (( bytes <= 1073741824 )) || return 74
  local remaining=$((deadline - SECONDS))
  (( remaining > 0 )) || return 124
  (
    ulimit -v 4194304
    exec timeout --foreground "${remaining}s" nice -n 15 "$@"
  ) >"$stdout_path" 2>"$stderr_path" &
  local run_pid=$! monitor_status=0
  while kill -0 "$run_pid" 2>/dev/null; do
    if incompatible_active; then
      monitor_status=73
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    bytes=$(owned_output_bytes)
    if (( bytes > 1073741824 )); then
      monitor_status=74
      kill -TERM "$run_pid" 2>/dev/null || true
      break
    fi
    sleep 2
  done
  local command_status=0
  if wait "$run_pid"; then command_status=0; else command_status=$?; fi
  (( monitor_status == 0 )) || return "$monitor_status"
  (( command_status == 0 )) || return "$command_status"
  refuse_overlap "after_$label" || return $?
  bytes=$(owned_output_bytes)
  (( bytes <= 1073741824 )) || return 74
  (( SECONDS <= deadline )) || return 124
}

stage=authenticate
run_monitored authenticate "$log_dir/authenticate.stdout" \
  "$log_dir/authenticate.stderr" sha256sum -c V3_FROZEN.sha256

stage=compile
run_monitored compile "$log_dir/compile.stdout" "$log_dir/compile.stderr" \
  /usr/bin/g++ -std=c++17 -O3 -DNDEBUG -pthread -Wall -Wextra -Wconversion \
  V3_symbolic_search.cpp -o V3_symbolic_search

stage=self_test
run_monitored self_test "$log_dir/self_test.stdout" "$log_dir/self_test.stderr" \
  ./V3_symbolic_search --self-test

stage=validate_self_test
run_monitored validate_self_test "$log_dir/validate_self_test.stdout" \
  "$log_dir/validate_self_test.stderr" python3 -c \
  'import pathlib,sys
t=pathlib.Path(sys.argv[1]).read_text()
assert "SELF_TEST_PASS" in t
assert "assoc_rank=5/6" in t
assert "ternary_nulls=1,1,1,1,1" in t
assert "order_trials=36" in t
assert "root_checks=504" in t
assert "root_index_checks=36x14" in t
print("SELF_TEST_VALIDATION_PASS")' "$log_dir/self_test.stdout"

stage=benchmark
run_monitored benchmark "$log_dir/benchmark.stdout" "$log_dir/benchmark.stderr" \
  ./V3_symbolic_search --benchmark

stage=validate_benchmark
run_monitored validate_benchmark "$log_dir/validate_benchmark.stdout" \
  "$log_dir/validate_benchmark.stderr" python3 -c \
  'import pathlib,re,sys
t=pathlib.Path(sys.argv[1]).read_text()
p=re.fullmatch(r"BENCHMARK_PASS repetitions=1 mean_full_60bit_input_seconds=([0-9.]+) static_atoms=([0-9]+) candidates=([0-9]+) order_trials=36 projected_8thread_seconds_1.75x=([0-9.]+) projected_peak_mib=1024 predicted_output_bytes=([0-9]+) identities=\{.*\}\n?",t)
assert p
assert int(p.group(2))>80000 and int(p.group(3))>11000
assert float(p.group(4))<=14400
assert int(p.group(5))<=1073741824
print("BENCHMARK_VALIDATION_PASS")' "$log_dir/benchmark.stdout"

stage=describe
run_monitored describe "$log_dir/describe.stdout" "$log_dir/describe.stderr" \
  ./V3_symbolic_search --describe

stage=validate_describe
run_monitored validate_describe "$log_dir/validate_describe.stdout" \
  "$log_dir/validate_describe.stderr" python3 -c \
  'import pathlib,re,sys
t=pathlib.Path(sys.argv[1]).read_text()
p=re.fullmatch(r"F264_D03_DESCRIPTION families=30 candidates=([0-9]+) aliases=([0-9]+) words_per_input=8744 p205_words=467 planned_inputs=5280 discovery_inputs=2208 heldout_inputs=3072 tsv_columns=2560 max_threads=8\n?",t)
assert p and int(p.group(1))>11000
print(p.group(1))' "$log_dir/describe.stdout"
read -r candidate_count <"$log_dir/validate_describe.stdout"

for split in discovery heldout; do
  stage=$split
  run_monitored "$split" "$log_dir/${split}.stdout" "$log_dir/${split}.stderr" \
    ./V3_symbolic_search 8 "$split" \
    "$out_dir/F264-D03.${split}.summary.json" \
    "$out_dir/F264-D03.${split}.rows.tsv" \
    "$out_dir/F264-D03.${split}.anomalies.tsv"

  stage="validate_${split}"
  run_monitored "validate_${split}" "$log_dir/validate_${split}.stdout" \
    "$log_dir/validate_${split}.stderr" python3 -c \
    'import csv,json,sys
split,rows_path,summary_path,anomaly_path,candidate_arg=sys.argv[1:]
candidate_count=int(candidate_arg)
bits=[16,24,32] if split=="discovery" else [40,48,56,60]
cohorts=["random","consecutive","safe_safe"]
families=[
"low_entry_control","lift_entry","lift_trace","lift_antitrace",
"determinant_N2_quotient","cayley_hamilton_N2_quotient","step_carry_K",
"step_carry_digit","step_second_carry_H","step_cross_minors",
"commutator_low","commutator_lift","commutator_trace_lift",
"fricke_N2_quotient","fricke_pair_difference","trace_collision",
"commutator_trace_collision","lift_collision","low_entry_minors",
"lift_minors","mixed_low_lift_minors","digit_associator_quotient",
"associator_second_carry","word_finite_difference","word_second_difference",
"trace_hankel_minor","lift_hankel_minor","character_discriminant",
"split_root_residual","conjugacy_coordinate_control"]
decoys=["matrix_associativity","associator_quotient","trace_cyclicity",
"inverse_trace","fricke_mod_N2","cayley_hamilton_mod_N2",
"determinant_multiplicativity","determinant_unit","conjugacy_trace",
"conjugacy_determinant"]
features=["low","lift","K","k","H"]
base=["factor_bits","split","cohort","index","p","q","N","cleanup",
"source_gcd_hits","noncommutative_profiles","decoys","atom_hash",
"candidate_hits","candidate_hash","order_trials","order_gcd_hits",
"order_initial_returns","order_split_returns","certified_blocks",
"noncyclic_blocks","certified_lcm","certified_lcm_bits",
"certified_new_bits","cyclic_lcm","cyclic_lcm_bits",
"root_proposals_checked","root_square_matches","root_unit_matches",
"root_proper_matches","root_transcript_hash","first_certificate"]
header=base+[f"root_proposal_{i}_checks" for i in range(14)]
for f in features:
 header += [f"basis_original_{f}_count",f"basis_original_{f}_hash",
            f"basis_conjugate_{f}_count",f"basis_conjugate_{f}_hash"]
header += [f"{d}_zeros" for d in decoys]
for f in families:
 header += [f"{f}_atoms",f"{f}_zeros",f"{f}_units",f"{f}_N_powers",f"{f}_hits"]
for w in range(467):
 header += [f"W{w}_gp",f"W{w}_gq",f"W{w}_loss_bits",
            f"W{w}_improvement_p",f"W{w}_improvement_q"]
assert len(header)==2560
def prime(n):
 if n<2:return False
 small=(2,3,5,7,11,13,17,19,23,29,31,37)
 for p in small:
  if n%p==0:return n==p
 d=n-1;s=0
 while d%2==0:d//=2;s+=1
 for a in (2,325,9375,28178,450775,9780504,1795265022):
  if a%n==0:continue
  x=pow(a,d,n)
  if x in (1,n-1):continue
  for _ in range(1,s):
   x=x*x%n
   if x==n-1:break
  else:return False
 return True
expected_cell={(b,c):(384 if c=="random" else 192 if c=="consecutive" else 96 if b==16 else 192) for b in bits for c in cohorts}
cell_indices={key:set() for key in expected_cell}; seen=set(); n=0
root_totals=[0,0,0,0]
with open(rows_path,newline="") as f:
 r=csv.reader(f,delimiter="\t"); actual=next(r); assert actual==header
 pos={name:i for i,name in enumerate(header)}
 for row in r:
  assert len(row)==2560 and row[pos["split"]]==split
  b=int(row[pos["factor_bits"]]); c=row[pos["cohort"]]; i=int(row[pos["index"]])
  assert (b,c) in expected_cell and i not in cell_indices[(b,c)]
  cell_indices[(b,c)].add(i)
  p=int(row[pos["p"]]);q=int(row[pos["q"]]);N=int(row[pos["N"]])
  assert p.bit_length()==b and q.bit_length()==b and p<q<2*p and N==p*q
  assert prime(p) and prime(q) and (p,q) not in seen;seen.add((p,q))
  if c=="safe_safe":assert prime((p-1)//2) and prime((q-1)//2)
  if c=="consecutive":
   assert all(not prime(x) for x in range(p+2,q,2))
  assert int(row[pos["noncommutative_profiles"]])==2
  assert int(row[pos["order_trials"]])==36
  checks=int(row[pos["root_proposals_checked"]]);square=int(row[pos["root_square_matches"]])
  unit=int(row[pos["root_unit_matches"]]);proper=int(row[pos["root_proper_matches"]])
  assert checks==504 and 0<=unit+proper<=square<=checks
  root_totals[0]+=checks;root_totals[1]+=square;root_totals[2]+=unit;root_totals[3]+=proper
  assert all(int(row[pos[f"root_proposal_{j}_checks"]])==36 for j in range(14))
  n+=1
for key,count in expected_cell.items():assert cell_indices[key]==set(range(count))
expected=sum(expected_cell.values());assert n==expected==({"discovery":2208,"heldout":3072}[split])
with open(anomaly_path,newline="") as f:
 r=csv.reader(f,delimiter="\t");assert next(r)==["factor_bits","split","cohort","index","type","detail"]
 anomaly_rows=0
 for row in r:
  assert len(row)==6 and row[1]==split and row[4] in {"factor","common_order","candidate_gcd"}
  anomaly_rows+=1
 assert anomaly_rows<=expected*258
d=json.load(open(summary_path))
top={"experiment","split","inputs","threads","elapsed_seconds","families",
"candidates","candidate_aliases","identity_mining","selection_uses_hidden_labels",
"executes_factor_bank","cohort_builds","decoy_summaries","family_summaries",
"direct_family_leads","order_summary","p205_score","p205_summaries",
"p205_finite_leads","candidate_summary"}
assert set(d)==top and d["experiment"]=="F264-D03" and d["split"]==split
assert d["inputs"]==expected and d["threads"]==8 and d["families"]==30
assert d["candidates"]==candidate_count and d["candidate_aliases"]>=0
assert d["selection_uses_hidden_labels"] is False and d["executes_factor_bank"] is False
assert "assoc_rank=5/6" in d["identity_mining"] and "ternary_nulls=1,1,1,1,1" in d["identity_mining"]
expected_cells=[(b,c) for b in bits for c in cohorts]
assert len(d["cohort_builds"])==len(expected_cells)
for obj,(b,c) in zip(d["cohort_builds"],expected_cells):
 assert set(obj)=={"factor_bits","cohort","attempts","accepted"}
 assert (obj["factor_bits"],obj["cohort"])==(b,c)
 assert obj["accepted"]==expected_cell[(b,c)] and obj["accepted"]<=obj["attempts"]<=2**22
assert [x["decoy"] for x in d["decoy_summaries"]]==decoys
for x in d["decoy_summaries"]:
 assert set(x)=={"decoy","exact_zero_count"} and x["exact_zero_count"]>0
expected_family=[(b,c,f) for b in bits for c in cohorts for f in families]
assert len(d["family_summaries"])==len(expected_family)
for obj,(b,c,f) in zip(d["family_summaries"],expected_family):
 assert set(obj)=={"factor_bits","cohort","family","count","atoms","zeros","units","N_powers","proper_gcd_events","proper_gcd_inputs"}
 assert (obj["factor_bits"],obj["cohort"],obj["family"])==(b,c,f)
 assert obj["count"]==expected_cell[(b,c)]
assert len(d["direct_family_leads"])==30
for obj,f in zip(d["direct_family_leads"],families):
 assert set(obj)=={"family","heldout_hit_inputs","heldout_safe_hit_inputs","heldout_size_mask","finite_lead"}
 assert obj["family"]==f
order=d["order_summary"]
assert set(order)=={"heldout_noncyclic_rows","heldout_safe_rows","heldout_size_mask",
"accumulated_exact_lcm","new_bits","root_proposals_checked","root_square_matches",
"root_unit_matches","root_proper_matches","root_transcript_hash","root_index_checks",
"finite_lead"}
assert order["root_proposals_checked"]==expected*504
assert order["root_index_checks"]==[expected*36]*14
assert [order["root_proposals_checked"],order["root_square_matches"],
        order["root_unit_matches"],order["root_proper_matches"]]==root_totals
assert d["p205_score"]=="min(ceil_log2(sp/gp),ceil_log2(sq/gq))"
expected_p205=[(b,c,w) for b in bits for c in cohorts for w in range(467)]
assert len(d["p205_summaries"])==len(expected_p205)
for obj,(b,c,w) in zip(d["p205_summaries"],expected_p205):
 assert set(obj)=={"factor_bits","cohort","word","count","median_loss_bits","baseline_median_loss_bits","improved_inputs","saturated_inputs"}
 assert (obj["factor_bits"],obj["cohort"],obj["word"])==(b,c,w)
 assert obj["count"]==expected_cell[(b,c)]
assert d["p205_finite_leads"]==sorted(set(d["p205_finite_leads"]))
assert all(isinstance(w,int) and 0<=w<467 for w in d["p205_finite_leads"])
assert len(d["candidate_summary"])==candidate_count
for i,obj in enumerate(d["candidate_summary"]):
 assert set(obj)=={"id","syntax","aliases","tested","proper_gcd_hits","safe_hits","size_mask","finite_lead"}
 assert obj["id"]==i and obj["aliases"]>=1 and obj["tested"]==expected
print("EXACT_REPORT_VALIDATION_PASS")' \
    "$split" "$out_dir/F264-D03.${split}.rows.tsv" \
    "$out_dir/F264-D03.${split}.summary.json" \
    "$out_dir/F264-D03.${split}.anomalies.tsv" "$candidate_count"
done

stage=compression
run_monitored compression "$log_dir/compression.stdout" \
  "$log_dir/compression.stderr" gzip -9 \
  "$out_dir/F264-D03.discovery.rows.tsv" \
  "$out_dir/F264-D03.discovery.anomalies.tsv" \
  "$out_dir/F264-D03.heldout.rows.tsv" \
  "$out_dir/F264-D03.heldout.anomalies.tsv"

stage=manifest
run_monitored manifest "$log_dir/manifest.stdout" "$log_dir/manifest.stderr" \
  python3 -c \
  'import datetime,hashlib,pathlib,sys
work=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);logs=pathlib.Path(sys.argv[3])
manifest=logs/"F264-D03.manifest"
core=["V3_ALGEBRA.md","V3_PREREGISTRATION.md","V3_symbolic_search.cpp",
"V3_remote_run.sh","V3_VALIDATION_PENDING.md","V3_AUDIT_REQUEST.md",
"V3_STATIC_VALIDATION.md","V3_PRELAUNCH_MANIFEST.md","V3_FROZEN.sha256",
"V3_symbolic_search"]
audit=work/"V3_HOSTILE_PRERUN_AUDIT.md"
if audit.is_file():core.append(audit.name)
paths=[work/x for x in core]
for root in (out,logs):
 paths += [p for p in root.rglob("*") if p.is_file() and p!=manifest and not p.name.endswith(".manifest.tmp")]
paths=sorted(set(paths),key=lambda p:str(p))
def digest(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for block in iter(lambda:f.read(1<<20),b""):h.update(block)
 return h.hexdigest()
lines=["experiment=F264-D03","created_utc="+datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")]
for p in paths:
 assert p.is_file();lines.append(f"{digest(p)}  {p}")
tmp=logs/".F264-D03.manifest.tmp";tmp.write_text("\n".join(lines)+"\n");tmp.replace(manifest)' \
  "$work_dir" "$out_dir" "$log_dir"

stage=final_output_gate
run_monitored final_output_gate "$log_dir/final_output_gate.stdout" \
  "$log_dir/final_output_gate.stderr" python3 -c \
  'import pathlib,sys
out=pathlib.Path(sys.argv[1]);logs=pathlib.Path(sys.argv[2])
for split in ("discovery","heldout"):
 for suffix in ("summary.json","rows.tsv.gz","anomalies.tsv.gz"):
  p=out/f"F264-D03.{split}.{suffix}";assert p.is_file() and p.stat().st_size>0
 assert not (out/f"F264-D03.{split}.rows.tsv").exists()
 assert not (out/f"F264-D03.{split}.anomalies.tsv").exists()
manifest=logs/"F264-D03.manifest";assert manifest.is_file() and manifest.stat().st_size>0
total=sum(p.stat().st_size for root in (out,logs) for p in root.rglob("*") if p.is_file())
assert total<=1073741824
print(f"FINAL_OUTPUT_GATE_PASS bytes={total}")' "$out_dir" "$log_dir"

stage=complete
echo "F264_D03_RUNNER_PASS"
