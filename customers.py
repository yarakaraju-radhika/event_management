import streamlit as st
from database import create_connection

st.title("👥 Customer Management")


# -------------------------------
# Display Customers
# -------------------------------

st.subheader("All Customers")

connection = create_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM Customers")
customers = cursor.fetchall()

cursor.close()
connection.close()

st.dataframe(customers, use_container_width=True)


# -------------------------------
# Add Customer
# -------------------------------

st.subheader("➕ Add New Customer")

name = st.text_input("Customer Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
registration_date = st.date_input("Registration Date")

if st.button("Add Customer"):

    connection = create_connection()
    cursor = connection.cursor()

    # Find the next customer ID
    cursor.execute(
        "SELECT COALESCE(MAX(customer_id), 0) + 1 FROM Customers"
    )

    customer_id = cursor.fetchone()[0]

    query = """
        INSERT INTO Customers
        (customer_id, name, email, phone, registration_date)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        customer_id,
        name,
        email,
        phone,
        registration_date
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success(
        f"Customer added successfully! Customer ID: {customer_id}"
    )

    st.rerun()