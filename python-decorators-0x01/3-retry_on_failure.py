#!/usr/bin/env python3
"""
Decorator that retries database operations if they fail,
with timestamped logging for resilience and traceability.
"""

import time
import sqlite3
import functools
from datetime import datetime  # for logging timestamps


def with_db_connection(func):
    """Decorator to manage DB connection lifecycle."""
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


def retry_on_failure(retries=3, delay=2):
    """Decorator that retries a function if it raises an exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    print(f"[{timestamp}] Attempt {attempt} to execute function...")
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[{timestamp}] Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] All {retries} retries failed.")
            raise last_exception
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """Fetch all users, retrying if a transient error occurs."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


if __name__ == "__main__":
    users = fetch_users_with_retry()
    print(users)
