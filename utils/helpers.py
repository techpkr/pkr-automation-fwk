import json
import os

def load_json_data(file_name: str):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    file_path = os.path.join(base_path, file_name)
    with open(file_path, "r") as f:
        return json.load(f)
