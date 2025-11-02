#!/usr/bin/python3
import seed

def stream_users_in_batches(batch_size):
    """Generator that fetches users in batches from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows  # ✅ yield a batch of rows

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Generator that filters and yields users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user["age"]) > 25:
                yield user  # ✅ yield each processed user
