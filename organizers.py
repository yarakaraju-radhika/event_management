import streamlit as st
from database import create_connection

st.title("🧑‍💼 Organizer Management")

# -------------------------------
# Display Organizers
# -------------------------------

st.subheader("All Organizers")

connection = create_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM Organizers")
organizers = cursor.fetchall()

cursor.close()
connection.close()

st.dataframe(organizers, use_container_width=True)


    # -------------------------------
# Add New Organizer
# -------------------------------

st.subheader("➕ Add New Organizer")

organizer_name = st.text_input("Organizer Name")

phone = st.text_input("Phone")

email = st.text_input("Email")

if st.button("Add Organizer"):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COALESCE(MAX(organizer_id), 0) + 1 FROM Organizers"
    )

    organizer_id = cursor.fetchone()[0]

    query = """
        INSERT INTO Organizers
        (organizer_id, organizer_name, phone, email)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        organizer_id,
        organizer_name,
        phone,
        email
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    st.success(
        f"Organizer added successfully! Organizer ID: {organizer_id}"
    )

    st.rerun()