import streamlit as st
from database import create_connection

st.set_page_config(
    page_title="Event Management System",
    page_icon="🎉",
    layout="wide"
)

# Title
st.title("🎉 Event Management System")
st.write("Manage customers, events, bookings, payments and reports.")

st.divider()

# Connect to MySQL
connection = create_connection()

# Get dashboard numbers
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM Customers")
total_customers = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Events")
total_events = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Bookings")
total_bookings = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM Payments")
total_payments = cursor.fetchone()[0]

cursor.close()
connection.close()

# Dashboard cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Customers", total_customers)

with col2:
    st.metric("🎪 Events", total_events)

with col3:
    st.metric("🎟️ Bookings", total_bookings)

with col4:
    st.metric("💳 Payments", total_payments)

st.divider()

st.subheader("Welcome to the Event Management System")

st.write(
    """
    This system allows you to manage:

    - 👥 Customers
    - 🎪 Events
    - 🧑‍💼 Organizers
    - 📍 Venues
    - 🎟️ Bookings
    - 💳 Payments
    - 📊 Reports and Analytics
    """
)