import streamlit as st
from database import create_connection

st.title("💳 Payment Management")

# -------------------------------
# Display Payments
# -------------------------------

st.subheader("All Payments")

connection = create_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM Payments")
payments = cursor.fetchall()

cursor.close()
connection.close()

st.dataframe(payments, use_container_width=True)

# -------------------------------
# Add New Payment
# -------------------------------

st.subheader("➕ Add New Payment")

booking_id = st.number_input(
    "Booking ID",
    min_value=1,
    step=1
)

amount = st.number_input(
    "Amount",
    min_value=0.0,
    step=100.0
)

payment_date = st.date_input("Payment Date")

payment_method = st.selectbox(
    "Payment Method",
    ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"]
)

status = st.selectbox(
    "Payment Status",
    ["Paid", "Pending", "Failed"]
)

if st.button("Add Payment"):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COALESCE(MAX(payment_id), 0) + 1 FROM Payments"
    )

    payment_id = cursor.fetchone()[0]

    query = """
        INSERT INTO Payments
        (payment_id, booking_id, amount, payment_date,
         payment_method, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        payment_id,
        booking_id,
        amount,
        payment_date,
        payment_method,
        status
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success(
        f"Payment added successfully! Payment ID: {payment_id}"
    )

    st.rerun()