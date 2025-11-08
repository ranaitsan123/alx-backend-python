#!/usr/bin/env python3
"""
Decorator that caches database query results to avoid redundant calls,
with timestamped logging for improved observability.
"""

import sqlite3
import functools
from datetime import datetime  # for timestamped logging

query_cache = {}  # simple in-memory cache


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


def cache_query(func):
    """Decorator to cache SQL query results based on the query string."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Extract query argument
        query = kwargs.get('query') or (args[0] if args else None)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check if the query result is already cached
        if query in query_cache:
            print(f"[{timestamp}] Using cached result for query: {query}")
            return query_cache[query]

        # Execute and cache the result
        print(f"[{timestamp}] Caching new result for query: {query}")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """Fetch users and cache query results."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
