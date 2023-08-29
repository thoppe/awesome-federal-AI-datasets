from slugify import slugify
from pathlib import Path
import yaml
import requests
import bs4

item = {}
item["agency"] = input("Agency: ").upper().strip()
item["department"] = input("Department: ").upper().strip()
item["homepage"] = input("URL: ").strip()

# TO DO: check if they are in the agency list

# Debug code
# item["agency"] = "CMS"
# item["department"] = "HHS"
# item["homepage"] = "https://www.cms.gov/OpenPayments/Data/Dataset-Downloads"

r = requests.get(item["homepage"])

if not r.ok:
    raise ValueError(f'{item["homepage"]} returned {r.status_code}')

soup = bs4.BeautifulSoup(r.content, "lxml")
title = soup.find("title")
if title is not None:
    title = title.get_text()

print("** Suggested title from URL: ", title)

item["title"] = input("Title: ").strip()
item["description"] = ""

save_dest = Path("data/datasets")
keys = [item["department"], item["agency"], slugify(item["title"])]
name = "_".join(keys)
f_yaml = save_dest / (name + ".yaml")

with open(f_yaml, "w") as FOUT:
    yaml.dump(item, FOUT)

print(f"Saved to {f_yaml}")
