from pathlib import Path
import yaml
import pandas as pd

F_YAML = Path("data/datasets").glob("*.yaml")

dfa = pd.read_csv("data/acronyms/agency.csv")
dfd = pd.read_csv("data/acronyms/department.csv")

data = []
for f_yaml in F_YAML:
    with open(f_yaml, "r") as stream:
        item = yaml.load(stream, yaml.Loader)
        data.append(item)

df = pd.DataFrame(data)
df = df.sort_values(["department", "agency", "title"])

table = []
table.append("| Dept. | Agency  | Title |")
table.append("| ----  | ----    | ----  |")

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
    row.append(f"[{item.department}]({department_url})")
    row.append(f"[{item.agency}]({agency_url})")

    # row.append(f"[:house:]({item.homepage}) {item.title}")
    row.append(f"[{item.title}]({item.homepage})")

    row = " | ".join([""] + row + [""])
    table.append(row)

table = "\n".join(table)

f_header = "data/assets/README_header.md"
f_footer = "data/assets/README_footer.md"
header = open(f_header).read()
footer = open(f_footer).read()

readme_text = "\n\n".join([header, table, footer])

with open("README.md", "w") as FOUT:
    FOUT.write(readme_text)
