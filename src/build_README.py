from pathlib import Path
import yaml
import pandas as pd

F_YAML = Path("data").glob("*.yaml")

dfa = pd.read_csv("data/acronyms/agency.csv")
#df_department = pd.read_csv("data/acronyms/departments.csv")

split_key = "## Project Listing"
with open("README.md") as FIN:
    readme_text = FIN.read()
    readme_text = readme_text.split(split_key)[0].strip()

readme_text += '\n\n' + split_key + '\n\n'

for f_yaml in F_YAML:

    table = []
    with open(f_yaml, "r") as stream:
        data = yaml.load_all(stream, yaml.FullLoader)
        df = pd.DataFrame(data)

    table.append("|       | Agency  | Title |")
    table.append("| ----- | ----    | ---- |")
    for _, item in df.iterrows():
        row = []

        idx = (
            (item.agency == dfa.abbreviation) &
            (item.department == dfa.department)
        )
        if not idx.sum():
            err = f"{item.agency} at {item.department} unknown"
            raise KeyError(err)
        agency_url = dfa[idx]['homepage'].values[0]
        
        row.append(f"[:house:]({item.homepage})")
        row.append(f"[{item.agency}]({agency_url})")
        row.append(f"{item.title}")
        row = ' | '.join([''] + row + [''])
        table.append(row)

    table = '\n'.join(table)
    print(df)
    print(table)

    readme_text += table + '\n'

with open("README.md", 'w') as FOUT:
    FOUT.write(readme_text)

