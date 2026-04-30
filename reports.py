
from utils import load_data
from collections import Counter

class ReportGenerator:
    def generate_report(self):
        data = load_data()
        print("Total:", len(data))
        print("Open:", len([t for t in data if t['status']=="OPEN"]))
        issues = [t['issue'] for t in data]
        print("Common:", Counter(issues).most_common(1))
