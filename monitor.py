
import psutil
from tickets import Ticket
from utils import load_data, save_data

class Monitor:
    def monitor_system(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        if cpu>90 or ram>95 or disk>90:
            print("ALERT")
            t = Ticket("SYSTEM","IT","High Usage")
            t.priority="P1"
            data = load_data()
            data.append(t.to_dict())
            save_data(data)
