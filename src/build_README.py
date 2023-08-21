from pathlib import Path
import yaml
import pandas as pd

F_YAML = Path("data").glob("*.yaml")

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

    table.append("| Agency | Title | Homepage |")
    table.append("| ----- | ---- | ---- |")
    for _, row in df.iterrows():
        table.append(f"| {row.agency} | {row.title} | [:house:]({row.homepage}) ")

    table = '\n'.join(table)
    print(df)
    print(table)

    readme_text += table + '\n'

with open("README.md", 'w') as FOUT:
    FOUT.write(readme_text)

