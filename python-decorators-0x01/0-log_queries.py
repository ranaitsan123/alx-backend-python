#!/usr/bin/env python3
"""
A script that demonstrates logging SQL queries with timestamps
using a Python decorator.
"""

import sqlite3
import functools
from datetime import datetime  # used to add timestamps to logs


def log_queries(func):
    """Decorator that logs SQL queries before executing them."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Retrieve the SQL query argument
        query = kwargs.get('query') or (args[0] if args else None)

        # Add timestamp for logging
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log the query
        if query:
            print(f"[{timestamp}] Executing SQL Query: {query}")
        else:
            print(f"[{timestamp}] No SQL query provided.")

        # Execute the original function
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    """Fetch all users from the database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
