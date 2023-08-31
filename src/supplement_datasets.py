from pathlib import Path
import yaml
import questionary
from questionary import print as qprint

main_question_key = "AI_ready_questions"

f_questions = "src/AI_ready_questions.yaml"
questions = yaml.load(open(f_questions, "r"), yaml.Loader)
questions = questions[main_question_key]

F_YAML = Path("data/datasets").glob("*.yaml")

data = []
for f_yaml in F_YAML:
    with open(f_yaml, "r") as stream:
        item = yaml.load(stream, yaml.Loader)
        is_modified = False

        print(item)
        if main_question_key not in item:
            item[main_question_key] = {}
        print(item)

        qprint(item["title"], style="fg:ansiyellow bg:black bold underline")
        qprint(item["homepage"], style="fg:ansiwhite bg:black italic")

        for question in questions:
            qitem = item[main_question_key]
            key = question["id"]
            val = qitem[key] if key in qitem else None

            print(key, val)

            if val is None:
                responses = question["responses"] + ["Unknown"]
                val = questionary.select(
                    question["query"], choices=responses
                ).ask()
                qitem[key] = val

                if val is not None:
                    is_modified = True

        if is_modified:
            print(f"Saving {f_yaml}")
            with open(f_yaml, "w") as FOUT:
                yaml.dump(item, FOUT)
