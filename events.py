import streamlit as st
from database import create_connection

st.title("🎪 Event Management")

# -------------------------------
# Display Events
# -------------------------------

st.subheader("All Events")

connection = create_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM Events")
events = cursor.fetchall()

cursor.close()
connection.close()

st.dataframe(events, use_container_width=True)

# -------------------------------
# Add New Event
# -------------------------------

st.subheader("➕ Add New Event")

event_name = st.text_input("Event Name")

event_type = st.text_input("Event Type")

event_date = st.date_input("Event Date")

location = st.text_input("Location")

total_seats = st.number_input(
    "Total Seats",
    min_value=1,
    step=1
)

if st.button("Add Event"):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COALESCE(MAX(event_id), 0) + 1 FROM Events"
    )

    event_id = cursor.fetchone()[0]

    query = """
        INSERT INTO Events
        (event_id, event_name, event_type, event_date,
         location, total_seats)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        event_id,
        event_name,
        event_type,
        event_date,
        location,
        total_seats
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success(
        f"Event added successfully! Event ID: {event_id}"
    )

    st.rerun()

