import streamlit as st

st.title("Smart IT Service Desk Automation System")

st.subheader("Project Overview")

st.write("""
This project automates IT helpdesk processes like:
- Ticket Creation
- Incident Handling
- SLA Tracking
- System Monitoring
- Reporting
""")

issue = st.text_input("Enter Issue")

if st.button("Create Ticket"):
    st.success(f"Ticket Created Successfully for: {issue}")

st.subheader("Features")

st.write("""
✔ Ticket Management  
✔ Priority Management  
✔ SLA Monitoring  
✔ CPU/Memory Monitoring  
✔ Reports Generation  
✔ Logging System  
""")