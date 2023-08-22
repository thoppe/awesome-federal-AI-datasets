import yaml
import requests
import bs4

f_yaml = "data/datasets.yaml"
with open(f_yaml, "r") as stream:
    data = list(yaml.load_all(stream, yaml.FullLoader))


item = {}
item["agency"] = input("Agency: ").upper().strip()
item["department"] = input("Department: ").upper().strip()
item["url"] = input("URL: ").strip()

# TO DO: check if they are in the agency list

# Debug code
# item["agency"] = "CMS"
# item["department"] = "HHS"
# item["url"] = "https://www.cms.gov/OpenPayments/Data/Dataset-Downloads"

r = requests.get(item["url"])

if not r.ok:
    raise ValueError(f'{item["url"]} returned {r.status_code}')

soup = bs4.BeautifulSoup(r.content, "lxml")
title = soup.find("title")
if title is not None:
    title = title.get_text()
item["title"] = title
print(f'Extracted "{title}" from URL')
item["description"] = ""

data.append(item)

with open(f_yaml, "w") as FOUT:
    yaml.dump_all(data, FOUT)

print(f"Saved to {f_yaml}")
