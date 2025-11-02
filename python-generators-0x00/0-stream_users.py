import seed

def stream_users():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row  # ✅ yields one user at a time

    cursor.close()
    connection.close()
