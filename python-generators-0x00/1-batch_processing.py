#!/usr/bin/python3
"""Batch processing using Python generators"""
import seed


def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows  # ✅ yield batch (not return)

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Generator that filters and yields users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user["age"]) > 25:
                yield user  # ✅ yield user (generator compliance)
