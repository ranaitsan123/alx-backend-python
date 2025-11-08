# 📘 Advanced Python: Context Managers and Asynchronous Programming

### **Repository:** `alx-backend-python`

### **Directory:** `python-context-async-perations-0x02`

---

## 🧭 Overview

This project demonstrates **advanced Python techniques** for managing database connections and executing queries efficiently using **Context Managers** and **Asynchronous Programming**.

You’ll learn how to:

* Implement **class-based context managers** using `__enter__` and `__exit__`
* Manage **database connections** automatically and safely
* Execute **queries concurrently** using `asyncio` and `aiosqlite`
* Write clean, readable, and efficient backend code

---

## 🧠 Key Concepts

### 1. Context Managers

#### 🔍 What Are Context Managers?

A **context manager** in Python is a construct that **handles resource setup and teardown automatically**.

It’s commonly used with the `with` statement to manage resources like:

* File I/O (`open()`)
* Database connections
* Network sockets

The main idea is that a context manager **ensures proper cleanup**, even when an exception occurs.

#### 🔧 How They Work

A context manager class implements two special methods:

```python
class Example:
    def __enter__(self):
        # Setup code (acquire resource)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup code (release resource)
        pass
```

When you use it:

```python
with Example() as resource:
    # use resource safely
```

* `__enter__` runs first — it *sets up* the resource and returns it.
* `__exit__` runs at the end — it *cleans up*, even if an error occurs.

This ensures **no resource leaks** (like unclosed files or database connections).

---

### 2. Database Connection Management

When working with databases, it’s critical to:

* Open connections when needed
* Close them after use
* Handle exceptions safely

Context managers automate this pattern:

```python
with sqlite3.connect('users.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
```

If anything goes wrong inside the `with` block, Python **still closes** the connection automatically.

---

### 3. Asynchronous Programming in Python

#### ⚡ What Is Asynchronous Programming?

Asynchronous programming allows multiple operations to run **concurrently**, without blocking each other.

Traditional (synchronous) code runs *one task at a time* — waiting for each to finish.
Async code, on the other hand, **starts multiple tasks and switches** between them efficiently.

This is ideal for:

* Web servers
* Database queries
* I/O-heavy operations

#### 🧩 The `async` and `await` Syntax

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(greet())
```

* `async def` declares a coroutine.
* `await` pauses execution until the awaited task completes.

---

### 4. `aiosqlite` — Async SQLite Library

`aiosqlite` provides **asynchronous** access to SQLite databases.

Instead of blocking operations, it allows multiple queries to run concurrently using `await`.

Example:

```python
import aiosqlite

async with aiosqlite.connect("users.db") as db:
    async with db.execute("SELECT * FROM users") as cursor:
        rows = await cursor.fetchall()
```

This is non-blocking and can run alongside other async tasks.

---

### 5. Concurrent Execution with `asyncio.gather()`

To run multiple async tasks **at the same time**, use `asyncio.gather()`:

```python
users, older_users = await asyncio.gather(
    async_fetch_users(),
    async_fetch_older_users()
)
```

This runs both queries concurrently — much faster than waiting for one to finish before starting the next.

---

## 🧱 Project Structure

```
python-context-async-perations-0x02/
├── 0-databaseconnection.py   # Custom class-based context manager
├── 1-execute.py              # Reusable query context manager
└── 3-concurrent.py           # Asynchronous concurrent database operations
```

---

## 🧩 Task Summaries

### **Task 0 — `0-databaseconnection.py`**

Create a custom class-based context manager for managing database connections.

```python
with DatabaseConnection("users.db") as cursor:
    cursor.execute("SELECT * FROM users;")
```

Automatically:

* Opens a connection on entry
* Closes it on exit

---

### **Task 1 — `1-execute.py`**

Reusable context manager for executing queries safely.

```python
with ExecuteQuery("users.db", "SELECT * FROM users WHERE age > ?", [25]) as results:
    print(results)
```

Encapsulates both connection handling and query execution logic.

---

### **Task 2 — `3-concurrent.py`**

Run multiple database queries concurrently using `aiosqlite` and `asyncio.gather()`.

```python
asyncio.run(fetch_concurrently())
```

Fetches:

* All users
* Users older than 40
  simultaneously for better performance.

---

## 🧪 Example SQLite Setup

To test your code, create a simple database:

```sql
CREATE TABLE users(
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);

INSERT INTO users (name, age)
VALUES ('Alice', 30), ('Bob', 45), ('Carol', 22);
```

Save as `users.db` in the same directory.

---

## 🚀 Running the Project

```bash
# Task 0
python3 0-databaseconnection.py

# Task 1
python3 1-execute.py

# Task 2
python3 3-concurrent.py
```

---

## 🧩 Real-World Use Cases

| Scenario       | How Context Managers/Async Help                       |
| -------------- | ----------------------------------------------------- |
| Web Backends   | Automatically close DB connections after each request |
| Data Pipelines | Simplify repetitive queries and ensure cleanup        |
| Dashboards     | Fetch multiple datasets concurrently                  |
| Testing        | Ensure databases reset after each test case           |
| Microservices  | Handle concurrent I/O efficiently                     |

---

## 🧾 Author & Credits

**Project by:** ALX Africa — *Backend Development (Python)*
**Contributor:** Aicha Lahnite
**Date:** November 2025

