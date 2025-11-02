# Python Generators – ALX Backend Project

## 📘 Project Overview

This project explores **advanced usage of Python generators** to build memory-efficient, scalable backend systems.  
You’ll use generators to process large datasets, stream SQL query results, handle pagination, and compute aggregate statistics — all without loading the entire dataset into memory.

By leveraging Python’s `yield` keyword, these scripts demonstrate how to work efficiently with live or large data sources, a critical skill in backend development.

---

## 🎯 Learning Objectives

By completing this project, you will:

- Master the use of **Python Generators** for iterative and lazy data loading.
- Build memory-efficient applications capable of handling large datasets.
- Use **batch processing** and **pagination** to optimize performance.
- Simulate **real-world streaming data** scenarios.
- Integrate **Python with MySQL** to fetch and process data dynamically.
- Compute aggregate metrics (e.g., average age) using generators instead of SQL functions.

---

## 🧠 Concepts Covered

- `yield` and generator functions  
- Lazy iteration over SQL query results  
- Batch and paginated data processing  
- Context management with database connections  
- Memory-efficient aggregation

---

## ⚙️ Project Structure

| File | Description |
|------|--------------|
| `seed.py` | Sets up the MySQL database, creates the `user_data` table, and seeds data from `user_data.csv`. |
| `0-stream_users.py` | Streams user data row by row using a generator. |
| `1-batch_processing.py` | Implements batch processing and filters users over a certain age. |
| `2-lazy_paginate.py` | Implements lazy pagination to load each page only when needed. |
| `4-stream_ages.py` | Streams user ages one by one and computes the average age efficiently. |

---

## 🧩 Example: Memory-Efficient Aggregation

The following code from `4-stream_ages.py` shows how to use generators to compute an average value without loading all records into memory.

```python
import seed

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield float(age)

    cursor.close()
    connection.close()


def compute_average_age():
    """Computes the average age of users efficiently using a generator."""
    total, count = 0, 0
    for age in stream_user_ages():
        total += age
        count += 1

    if count > 0:
        avg = total / count
        print(f"Average age of users: {avg:.2f}")
    else:
        print("No data available.")
