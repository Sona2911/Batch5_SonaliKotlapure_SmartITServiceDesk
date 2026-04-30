# 🚀 Smart IT Service Desk Automation System

## 📌 Project Overview

This project is a Python-based backend automation system designed to replace manual IT helpdesk processes. It automates ticket creation, incident handling, system monitoring, logging, and reporting.

The system follows ITIL concepts and uses core Python, OOP, file handling, and system monitoring techniques.

---

## 🎯 Features

### 🎫 Ticket Management

* Create Ticket
* View All Tickets
* Search Ticket by ID
* Update Ticket Status
* Close Ticket
* Delete Ticket

### ⚡ Priority Management

| Issue Type     | Priority |
| -------------- | -------- |
| Server Down    | P1       |
| Internet Down  | P2       |
| Laptop Slow    | P3       |
| Password Reset | P4       |

---

### ⏱ SLA Tracking

| Priority | SLA Time |
| -------- | -------- |
| P1       | 1 Hour   |
| P2       | 4 Hours  |
| P3       | 8 Hours  |
| P4       | 24 Hours |

---

### 🖥 System Monitoring

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* Automatic Ticket Creation when threshold exceeds

---

### 📊 Reports

* Total Tickets
* Open Tickets
* Closed Tickets
* High Priority Tickets
* Most Common Issues

---

### 🧠 ITIL Concepts Implemented

* Incident Management
* Service Request Management
* Problem Management
* Change Management (basic tracking)
* SLA Monitoring

---

### 📝 Logging System

Logs are maintained for:

* Ticket creation
* Ticket updates
* Ticket closure
* Monitoring alerts
* Errors

---

## 🛠 Technologies Used

* Python
* JSON (Data Storage)
* CSV (Backup)
* psutil (System Monitoring)

---

## 📁 Project Structure

```
smart_it_service_desk/
│── main.py
│── tickets.py
│── monitor.py
│── reports.py
│── itil.py
│── utils.py
│── logger.py
│── requirements.txt
│── README.md
│── data/
│   ├── tickets.json
│   ├── logs.txt
│   ├── backup.csv
│   └── problems.json
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/Sona2911/Batch5_SonaliKotlapure_SmartITServiceDesk.git
cd smart_it_service_desk
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Application

```
python main.py
```

---

## 🧪 Sample Workflow

1. Create a ticket (e.g., "Server down")
2. View all tickets
3. Search ticket by ID
4. Update or close ticket
5. Monitor system (auto ticket generation)
6. Generate reports
7. Detect repeated problems

---

## ⚠️ Exception Handling

* Handles file errors
* Invalid input handling
* Missing data protection

---

## 🔍 Key Concepts Used

* Core Python (loops, conditions, functions)
* OOP (classes, inheritance, encapsulation)
* File Handling (JSON, CSV)
* Exception Handling
* System Monitoring using psutil

---

## 📌 Future Enhancements

* GUI Interface (Tkinter / Web)
* Database Integration (MySQL)
* Email Notifications
* Advanced SLA tracking
* Dashboard Analytics

---

## 👩‍💻 Author

Sonali Kotlapure


