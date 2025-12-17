import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "routes.json")

def load_routes():
    with open(FILE_PATH, "r") as f:
        return json.load(f)
