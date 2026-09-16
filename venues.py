import streamlit as st
from database import create_connection

st.title("📍 Venue Management")

# -------------------------------
# Display Venues
# -------------------------------

st.subheader("All Venues")

connection = create_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM Venues")
venues = cursor.fetchall()

cursor.close()
connection.close()

st.dataframe(venues, use_container_width=True)

# -------------------------------
# Add New Venue
# -------------------------------

st.subheader("➕ Add New Venue")

venue_name = st.text_input("Venue Name")
city = st.text_input("City")
capacity = st.number_input(
    "Capacity",
    min_value=1,
    step=1
)

if st.button("Add Venue"):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COALESCE(MAX(venue_id), 0) + 1 FROM Venues"
    )

    venue_id = cursor.fetchone()[0]

    query = """
        INSERT INTO Venues
        (venue_id, venue_name, city, capacity)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        venue_id,
        venue_name,
        city,
        capacity
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success(
        f"Venue added successfully! Venue ID: {venue_id}"
    )

    st.rerun()