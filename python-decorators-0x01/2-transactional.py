#!/usr/bin/env python3
"""
Decorator that manages database transactions by automatically
committing or rolling back with timestamped logging.
"""

import sqlite3
import functools
from datetime import datetime  # for logging timestamps


def with_db_connection(func):
    """Decorator to open and close a DB connection automatically."""
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


def transactional(func):
    """Decorator that wraps DB operations in a transaction."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{start_time}] Starting transaction.")
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Transaction committed.")
            return result
        except Exception as e:
            conn.rollback()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Transaction rolled back due to: {e}")
            raise
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """Update a user's email with automatic transaction handling."""
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


if __name__ == "__main__":
    update_user_email(user_id=1, new_email="updated_email@example.com")
