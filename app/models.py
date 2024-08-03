import json
from typing import List, Dict

DATA_PATH = "data/"

def load_data(file_name: str) -> List[Dict]:
    with open(DATA_PATH + file_name, "r") as file:
        return json.load(file)

def save_data(file_name: str, data: List[Dict]):
    with open(DATA_PATH + file_name, "w") as file:
        json.dump(data, file, indent=4)

def get_conferences():
    return load_data("conferences.json")

def get_users():
    return load_data("users.json")

def save_conferences(conferences):
    save_data("conferences.json", conferences)

def save_users(users):
    save_data("users.json", users)
