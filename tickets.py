
from datetime import datetime
from utils import load_data, save_data
from logger import log_info

class Ticket:
    def __init__(self, emp, dept, issue, category="General"):
        self.id = int(datetime.now().timestamp())
        self.employee = emp
        self.department = dept
        self.issue = issue
        self.category = category
        self.priority = self.set_priority(issue)
        self.status = "OPEN"
        self.created = str(datetime.now())

    def set_priority(self, issue):
        rules = {"server":"P1","internet":"P2","slow":"P3","password":"P4"}
        for k,v in rules.items():
            if k in issue.lower():
                return v
        return "P4"

    def to_dict(self):
        return self.__dict__

class TicketManager:
    def create_ticket(self):
        emp = input("Employee:")
        dept = input("Dept:")
        issue = input("Issue:")
        t = Ticket(emp,dept,issue)
        data = load_data()
        data.append(t.to_dict())
        save_data(data)
        log_info("Created")
        print("Created:", t.id)

    def view_tickets(self):
        for t in load_data():
            print(t)

    def search_ticket(self):
        tid = int(input("ID:"))
        for t in load_data():
            if t['id']==tid:
                print(t)

    def update_ticket(self):
        tid = int(input("ID:"))
        data = load_data()
        for t in data:
            if t['id']==tid:
                t['status']="IN_PROGRESS"
        save_data(data)

    def close_ticket(self):
        tid = int(input("ID:"))
        data = load_data()
        for t in data:
            if t['id']==tid:
                t['status']="CLOSED"
        save_data(data)

    def delete_ticket(self):
        tid = int(input("ID:"))
        data = [t for t in load_data() if t['id']!=tid]
        save_data(data)
