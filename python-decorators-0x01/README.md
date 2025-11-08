# Python Decorators — Advanced Backend Operations

### 📁 Project: `python-decorators-0x01`

### 💻 Repository: `alx-backend-python`

---

## 📘 Project Overview

This project focuses on **Python decorators** and their use in enhancing **database operations** for backend applications.
You’ll implement decorators that **log queries**, **manage connections**, **handle transactions**, **retry failed operations**, and **cache results** — all while building resilience and maintainability into your code.

Each decorator adds a layer of automation and reliability, similar to middleware in production-grade backend systems.

---

## 🎯 Learning Objectives

By completing this project, you will:

* Deepen your understanding of **Python decorators** and how they modify or extend function behavior.
* Automate common database tasks such as connection handling, logging, and caching.
* Learn how to ensure **data consistency** using transaction management.
* Implement **resilient retry mechanisms** for transient database errors.
* Optimize performance using **query caching**.
* Understand the importance of **timestamped logging** in real-world applications.

---

## ⚙️ Concepts Covered

### 1. **Decorators in Python**

A **decorator** is a higher-order function that takes another function as input and extends or modifies its behavior without changing its code.

Example:

```python
@decorator_name
def function_to_enhance():
    pass
```

Decorators are widely used for **logging**, **authentication**, **performance monitoring**, and **error handling**.

---

### 2. **Logging Database Queries**

The first decorator `@log_queries` logs every SQL query before it executes.
This improves **observability** and helps developers see what’s happening in their database layer.

**Added Enhancement:**
Each log message includes a **timestamp** using:

```python
from datetime import datetime
```

so you can know *when* each query was executed.

Example Log:

```
[2025-11-08 15:14:22] Executing SQL Query: SELECT * FROM users
```

---

### 3. **Automatic Connection Handling**

`@with_db_connection` simplifies database access by automatically:

* Opening the connection before function execution.
* Closing the connection afterward (even if an error occurs).

This reduces boilerplate code and prevents **connection leaks** — a common issue in backend systems.

---

### 4. **Transaction Management**

`@transactional` ensures that a function runs inside a **transactional context**:

* If the operation succeeds → **commit** changes.
* If an error occurs → **rollback** to maintain data integrity.

Timestamped logs show when transactions start, commit, or rollback:

```
[2025-11-08 15:15:03] Starting transaction.
[2025-11-08 15:15:03] Transaction committed.
```

---

### 5. **Retry on Failure**

`@retry_on_failure` makes database operations more resilient by automatically retrying failed operations (for example, if the database is temporarily locked or unavailable).

It logs each attempt with timestamps for clear tracking:

```
[2025-11-08 15:15:40] Attempt 1 failed: database is locked. Retrying in 1s...
```

Retries prevent minor errors from breaking entire workflows.

---

### 6. **Query Caching**

`@cache_query` avoids running the same query multiple times unnecessarily.
The first result is stored in memory (`query_cache` dictionary), and subsequent calls return the cached result — reducing load and improving performance.

Example:

```
[2025-11-08 15:16:10] Caching new result for query: SELECT * FROM users
[2025-11-08 15:16:12] Using cached result for query: SELECT * FROM users
```

---

## 🧾 The Importance of Tracking Logs (with Timestamps)

Logging is one of the most **critical practices in backend development**.

### Why It Matters:

1. **Debugging:**
   Logs with timestamps help identify when an issue started and trace its cause.

2. **Auditing:**
   Database queries, commits, and rollbacks can be reviewed later for security or compliance.

3. **Performance Monitoring:**
   By comparing timestamps, you can measure query execution times and identify bottlenecks.

4. **System Resilience:**
   Timestamped logs make retry behavior and transaction failures transparent — essential for diagnosing intermittent issues in production systems.

5. **Accountability:**
   A clear, timestamped log trail shows *who did what and when*, which is crucial in multi-user environments.

### Example of Good Log Flow:

```
[2025-11-08 15:18:22] Opening database connection.
[2025-11-08 15:18:22] Executing SQL Query: SELECT * FROM users
[2025-11-08 15:18:22] Caching new result for query: SELECT * FROM users
[2025-11-08 15:18:22] Closed database connection.
```

This type of **structured, timestamped logging** turns raw code into a **reliable, traceable backend system**.

---

## 🧪 Project Files

| File                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `0-log_queries.py`        | Logs SQL queries with timestamps.                |
| `1-with_db_connection.py` | Manages opening/closing of database connections. |
| `2-transactional.py`      | Handles commit/rollback transactions safely.     |
| `3-retry_on_failure.py`   | Retries database operations when errors occur.   |
| `4-cache_query.py`        | Implements caching for query results.            |

---

## ⚡ Example Database Setup

To test your decorators, create a simple SQLite database:

```python
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
''')
cursor.executemany(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com')
    ]
)
conn.commit()
conn.close()
```

Then run:

```bash
python3 0-log_queries.py
```

---

## 🧩 Key Takeaways

* **Decorators** make your code cleaner and reusable.
* **Logging with timestamps** turns simple print statements into powerful diagnostic tools.
* **Database resilience** comes from handling failures gracefully (transactions, retries, caching).
* These patterns mirror **real-world backend engineering practices**.

---

## 👥 Author

**ALX Backend Python Project — Decorators (0x01)**
Copyright © 2025
All rights reserved.
