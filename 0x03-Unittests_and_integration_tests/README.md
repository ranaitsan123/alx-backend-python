# 📘 0x03. Unittests and Integration Tests

## 📖 Description

This project is part of the **ALX Backend Python** curriculum.
It focuses on **unit testing** and **integration testing** — two essential techniques for building reliable and maintainable Python code.

You’ll learn how to:

* Write and run unit tests with `unittest`
* Use `parameterized` to test multiple cases efficiently
* Mock dependencies with `unittest.mock`
* Understand memoization and test cached functions
* Create integration tests that validate interactions between components

All tests cover functions and classes in **`utils.py`** and **`client.py`**, using **fixtures** from `fixtures.py`.

---

## 🧰 Resources

Before you begin, make sure to review:

* [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
* [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
* [parameterized](https://pypi.org/project/parameterized/)
* [Memoization concept](https://en.wikipedia.org/wiki/Memoization)

---

## 🧠 Learning Objectives

By the end of this project, you should be able to explain:

* The **difference between unit tests and integration tests**
* How to use **mocking** to isolate external dependencies
* What **parameterization** and **fixtures** are, and how to use them
* How to use the **unittest framework** for testing Python code
* How to test **memoized** (cached) functions
* How to build robust, isolated, and reliable test suites

---

## ⚙️ Requirements

* All files are interpreted/compiled on **Ubuntu 18.04 LTS** using **Python 3.7**
* All files should end with a new line
* First line of every file: `#!/usr/bin/env python3`
* Code must follow **pycodestyle** (version 2.5)
* All files must be **executable**
* All modules, classes, and functions must have **docstrings**
* All functions must be **type-annotated**
* Tests must use **`unittest`** (with `parameterized` and `mock`)

---

## 🧩 Project Structure

```
0x03-Unittests_and_integration_tests/
│
├── utils.py
├── client.py
├── fixtures.py
│
├── test_utils.py
├── test_client.py
│
└── README.md
```

---

## 🧪 Running the Tests

To run all tests:

```bash
$ python3 -m unittest discover
```

To run a specific test file:

```bash
$ python3 -m unittest test_utils.py
$ python3 -m unittest test_client.py
```

To check code style:

```bash
$ pycodestyle .
```

---

## 🧭 Tasks Overview

### **0. Parameterize a unit test**

Create parameterized unit tests for `utils.access_nested_map()`
Check that the function returns the correct values for different map-path combinations.

### **1. Exception parameterization**

Extend the tests to ensure that `access_nested_map()` raises a `KeyError` when the key path is invalid.

### **2. Mock HTTP calls**

Test `utils.get_json()` by mocking `requests.get()` so no real HTTP requests are made.

### **3. Memoization testing**

Test the `utils.memoize` decorator to verify that results are cached and the wrapped method is called only once.

### **4. Patch as decorators**

Test `GithubOrgClient.org` from `client.py`.
Use `@patch` to replace external calls with mocks and `@parameterized.expand` for multiple orgs.

### **5. Mocking a property**

Mock the `GithubOrgClient.org` property to test that `_public_repos_url` returns the expected value.

### **6. More patching**

Mock both `get_json()` and `_public_repos_url` to test `GithubOrgClient.public_repos()`.

### **7. Parameterized license check**

Parameterize tests for `GithubOrgClient.has_license()` to check if repositories have the given license.

### **8. Integration tests with fixtures**

Use real fixture data from `fixtures.py` and mock only external HTTP requests.
Test setup with `setUpClass()` and cleanup with `tearDownClass()`.

### **9. Advanced integration tests**

Run end-to-end tests to verify `GithubOrgClient.public_repos()` both with and without license filters.

---

## 🧱 Example Output

Running all tests should show:

```
$ python3 -m unittest discover
................................................................
----------------------------------------------------------------------
Ran XX tests in 0.XXXs

OK
```

---

## 🧑‍💻 Author

**ALX Backend Python - Unit & Integration Tests**
Created by [ALX Software Engineering Program](https://www.alxafrica.com/)

