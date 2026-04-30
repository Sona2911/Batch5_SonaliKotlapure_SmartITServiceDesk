
from tickets import TicketManager
from monitor import Monitor
from reports import ReportGenerator
from itil import ITILManager

tm = TicketManager()
monitor = Monitor()
report = ReportGenerator()
itil = ITILManager()

while True:
    print("\n1.Create Ticket\n2.View\n3.Search\n4.Update\n5.Close\n6.Delete\n7.Monitor\n8.Report\n9.ITIL\n10.Exit")
    ch = input("Choice: ")

    if ch=='1': tm.create_ticket()
    elif ch=='2': tm.view_tickets()
    elif ch=='3': tm.search_ticket()
    elif ch=='4': tm.update_ticket()
    elif ch=='5': tm.close_ticket()
    elif ch=='6': tm.delete_ticket()
    elif ch=='7': monitor.monitor_system()
    elif ch=='8': report.generate_report()
    elif ch=='9': itil.detect_problems()
    elif ch=='10': break
