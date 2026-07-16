import argparse
from pathlib import Path
import sys
import yaml
import pandas as pd

F_YAML = sorted(Path("data/datasets").glob("*.yaml"))

dfa = pd.read_csv("data/acronyms/agency.csv")
dfd = pd.read_csv("data/acronyms/department.csv")

f_questions = "src/AI_ready_questions.yaml"
question_key = "AI_ready_questions"
score_sheet = yaml.safe_load(open(f_questions, "r"))
questions = pd.DataFrame(score_sheet[question_key]).set_index("id")
ranking = pd.DataFrame(score_sheet["Ranking"])

data = []
for f_yaml in F_YAML:
    with open(f_yaml, "r") as stream:
        item = yaml.safe_load(stream)
        item["f_yaml"] = f_yaml
        data.append(item)


df = pd.DataFrame(data)

# Compute the dataset scores
col_scores, col_icons = [], []
for _, item in df.iterrows():
    dataset_score = 0
    is_unknown = False
    if question_key in item:
        scores = item[question_key]
        for k, v in scores.items():
            q = questions.loc[k]
            if v == "Unknown":
                is_unknown = True
            if v == q["responses"][0]:
                dataset_score += q["score"]

    # Get the highest ranking from the scores
    row = ranking[ranking.score <= dataset_score].sort_values("rank").iloc[0]
    icon = row["icon"]

    if is_unknown:
        icon = ":question:"
    col_scores.append(dataset_score)
    col_icons.append(icon)

df["dataset_score"] = col_scores
df["dataset_icon"] = col_icons
sort_cols = ["dataset_score", "department", "agency", "title"]
df = df.sort_values(sort_cols, ascending=False)

##########################################################################
# Build the table
##########################################################################

table = []
table.append("| Status| Dept. | Agency  | Title |")
table.append("| ----  | ----  | ----    | ----- |")

for _, item in df.iterrows():
    if item.agency:
        idx = (item.agency == dfa.agency) & (item.department == dfa.department)
        if not idx.sum():
            err = (
                f"{item.agency} at {item.department} unknown. "
                f"Edit data/acronyms/agency.csv"
            )
            raise KeyError(err)
        agency_url = dfa[idx]["homepage"].values[0]
    else:
        agency_url = ""

    idx = item.department == dfd.department
    department_url = dfd[idx]["homepage"].values[0]

    row = []
    row.append(f"[{item.dataset_icon}]({item.f_yaml})")
    row.append(f"[{item.department}]({department_url})")
    row.append(f"[{item.agency}]({agency_url})")

    # row.append(f"[:house:]({item.homepage}) {item.title}")
    row.append(f"[{item.title}]({item.homepage})")

    row = "| " + " | ".join(row) + " |"
    table.append(row)

table = "\n".join(table)

print(table)

f_header = "data/assets/README_header.md"
f_footer = "data/assets/README_footer.md"
header = open(f_header).read()
footer = open(f_footer).read()

readme_text = "\n\n".join([header, table, footer])

parser = argparse.ArgumentParser(
    description="Build the generated catalog README."
)
parser.add_argument(
    "--check", action="store_true", help="fail if README.md is not current"
)
args = parser.parse_args()

if args.check:
    if Path("README.md").read_text() != readme_text:
        print("README.md is not current; run make build", file=sys.stderr)
        raise SystemExit(1)
else:
    with open("README.md", "w") as FOUT:
        FOUT.write(readme_text)
