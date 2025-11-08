#!/usr/bin/env python3
"""
Decorator that automatically manages opening and closing
database connections with timestamped logging.
"""

import sqlite3
import functools
from datetime import datetime  # for timestamped logging


def with_db_connection(func):
    """Decorator to handle opening and closing DB connections."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Opening database connection.")
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Closed database connection.")
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """Retrieve a user by ID."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print(user)
