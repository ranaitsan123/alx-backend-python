#!/usr/bin/env python3
import sqlite3
import functools
from datetime import datetime  # used to add timestamps to query logs for better tracking

def log_queries(func):
    """Decorator to log SQL queries before executing"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the SQL query from arguments
        query = kwargs.get('query') or (args[0] if args else None)

        # Add timestamp to the log message using datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log the query with the current timestamp
        if query:
            print(f"[{timestamp}] Executing SQL Query: {query}")
        else:
            print(f"[{timestamp}] No SQL query provided.")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
