
from collections import Counter
from utils import load_data
import json

class ITILManager:
    def detect_problems(self):
        data = load_data()
        issues = [t['issue'] for t in data]
        count = Counter(issues)
        probs = [ {"issue":i,"count":c} for i,c in count.items() if c>=5 ]
        with open("data/problems.json","w") as f:
            json.dump(probs,f,indent=4)
        print("Updated")
