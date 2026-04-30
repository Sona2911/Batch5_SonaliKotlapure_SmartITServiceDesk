
import json, os

FILE="data/tickets.json"

def load_data():
    if not os.path.exists(FILE): return []
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def save_data(d):
    with open(FILE,"w") as f:
        json.dump(d,f,indent=4)
