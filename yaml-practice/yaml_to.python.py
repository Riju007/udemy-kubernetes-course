import yaml
from pathlib import Path
from typing import Any
from pprint import pprint
BASE_DIR = Path.cwd()


def convert_yaml_to_python_dict(yaml_file_name: str) -> dict[Any, Any]:
    yaml_file_path = BASE_DIR.joinpath(yaml_file_name)
    with yaml_file_path.open("r") as file_obj:
        data: dict[Any, Any] = yaml.safe_load(file_obj)
        return data


if __name__ == "__main__":
    yaml_file_name = "03-anchor-and-alias.yaml"
    result = convert_yaml_to_python_dict(yaml_file_name)
    pprint(result, sort_dicts=False, width=120)
