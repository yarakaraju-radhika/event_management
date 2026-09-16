import streamlit as st
from database import create_connection

st.title("🎟️ Booking Management")

# -------------------------------
# Display Bookings
# -------------------------------

st.subheader("All Bookings")

connection = create_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM Bookings")
bookings = cursor.fetchall()

cursor.close()
connection.close()

st.dataframe(bookings, use_container_width=True)

# -------------------------------
# Add New Booking
# -------------------------------

st.subheader("➕ Add New Booking")

customer_id = st.number_input(
    "Customer ID",
    min_value=1,
    step=1
)

event_id = st.number_input(
    "Event ID",
    min_value=1,
    step=1
)

booking_date = st.date_input("Booking Date")

tickets = st.number_input(
    "Number of Tickets",
    min_value=1,
    step=1
)

total_amount = st.number_input(
    "Total Amount",
    min_value=0.0,
    step=100.0
)

status = st.selectbox(
    "Booking Status",
    ["Confirmed", "Pending", "Cancelled"]
)

if st.button("Add Booking"):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COALESCE(MAX(booking_id), 0) + 1 FROM Bookings"
    )

    booking_id = cursor.fetchone()[0]

    query = """
        INSERT INTO Bookings
        (booking_id, customer_id, event_id, booking_date,
         tickets, total_amount, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        booking_id,
        customer_id,
        event_id,
        booking_date,
        tickets,
        total_amount,
        status
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success(
        f"Booking added successfully! Booking ID: {booking_id}"
    )

    st.rerun()