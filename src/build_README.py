from pathlib import Path
import yaml
import pandas as pd

F_YAML = Path("data").glob("*.yaml")

dfa = pd.read_csv("data/acronyms/agency.csv")
dfd = pd.read_csv("data/acronyms/department.csv")

split_key = "## Project Listing"
with open("README.md") as FIN:
    readme_text = FIN.read()
    readme_text = readme_text.split(split_key)[0].strip()

readme_text += "\n\n" + split_key + "\n\n"

data = []
for f_yaml in F_YAML:
    with open(f_yaml, "r") as stream:
        fdata = yaml.load_all(stream, yaml.FullLoader)
        data.append(pd.DataFrame(fdata))

df = pd.concat(data)
df = df.sort_values(["department", "agency", "title"])

table = []
table.append("| Dept. | Agency  | Title |")
table.append("| ----  | ----    | ----  |")

for _, item in df.iterrows():
    idx = (item.agency == dfa.agency) & (item.department == dfa.department)
    if not idx.sum():
        err = f"{item.agency} at {item.department} unknown"
        raise KeyError(err)
    agency_url = dfa[idx]["homepage"].values[0]

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
print(df)
print(table)

readme_text += table + "\n"

with open("README.md", "w") as FOUT:
    FOUT.write(readme_text)
