# 🧩 Django Middleware Project — ALX Backend

## 📌 Project Title

**Django-Middleware-0x03 — Understanding Middlewares**

This project explores Django middleware by implementing logging, access control, rate-limiting, and role-based authorization inside an existing messaging/chat application.

---

## 📚 Overview

Middleware allows you to intercept and process requests **before** they reach your views, and responses **before** they return to the client.
This project demonstrates core middleware concepts using a chat/messaging API from a previous ALX project.

You will:

* Log incoming user requests
* Restrict chat access during certain hours
* Implement IP-based message rate limiting
* Enforce role-based access permissions

---

## 🏗️ Project Structure

```
Django-Middleware-0x03/
│
├── chats/
│   ├── middleware.py       # <-- All custom middleware
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── messaging_app/
│   ├── settings.py         # <-- Middleware added to MIDDLEWARE list
│   ├── urls.py
│   ├── wsgi.py
│
├── requests.log            # <-- Logs user requests
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/alx-backend-python
cd alx-backend-python/Django-Middleware-0x03
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Apply migrations

```bash
python manage.py migrate
```

### 4️⃣ Run the development server

```bash
python manage.py runserver
```

---

# 🧱 Implemented Middleware

All middleware is located in:
📁 **chats/middleware.py**

---

## 1️⃣ RequestLoggingMiddleware

### ✔ Objective

Logs each incoming request with:

* Timestamp
* User (authenticated or Anonymous)
* Path requested

### ✔ Output

Logged in: **requests.log**

### ✔ Purpose

Helps with debugging, auditing, and tracking user behavior.

---

## 2️⃣ RestrictAccessByTimeMiddleware

### ✔ Objective

Block chat access between:

⛔ **6 PM – 9 PM (18:00–21:00)**

### ✔ Response

Returns **403 Forbidden** if accessed during restricted hours.

### ✔ Purpose

Simulates time-based service availability control.

---

## 3️⃣ OffensiveLanguageMiddleware (Rate Limiting)

### ✔ Objective

Limit number of chat messages per IP:

* **Max 5 messages per minute**
* Only counts **POST** requests to chat endpoints

### ✔ Response

If exceeded → returns:

```json
{ "error": "Rate limit exceeded. Max 5 messages per minute." }
```

### ✔ Purpose

Protects system from message spam or abuse.

---

## 4️⃣ RolePermissionMiddleware

### ✔ Objective

Restrict specific actions to:

* **admin**
* **moderator**

### ✔ Protects paths such as:

* `/chats/admin/`
* `/chats/moderate/`

### ✔ Response

Returns **403 Forbidden** if user lacks required role.

### ✔ Purpose

Implements authorization at middleware level.

---

# 🛠️ MIDDLEWARE Settings

Added in `messaging_app/settings.py`:

```python
MIDDLEWARE += [
    'chats.middleware.RequestLoggingMiddleware',
    'chats.middleware.RestrictAccessByTimeMiddleware',
    'chats.middleware.OffensiveLanguageMiddleware',
    'chats.middleware.RolePermissionMiddleware',
]
```

---

# 🧪 Testing the Middleware

## ✔ Test 1: Request Logging

Visit any page:

```
GET /chats/messages/
```

Check file:

```
cat requests.log
```

You should see timestamps, user, path.

---

## ✔ Test 2: Time-Based Restriction

Change your system time OR temporarily force:

```python
current_hour = 19  # for testing
```

Result → **403 Forbidden**

---

## ✔ Test 3: Rate Limiting

Send 6 POST requests within 60 seconds:

```
POST /chats/messages/
```

6th request → returns:

```
429 Too Many Requests
```

---

## ✔ Test 4: Role Permission

Try accessing:

```
GET /chats/admin/
```

As:

### Normal user → ❌ Forbidden

### Admin or Moderator → ✔ Allowed

---

# 🧾 Requirements Achieved

✔ Project setup
✔ Logging middleware
✔ Time restriction middleware
✔ IP rate limiting
✔ Role-based permission middleware
✔ Correct file paths
✔ Updated settings.py

---

# 🥳 Final Notes

This project strengthens your understanding of:

* Django request lifecycle
* Intercepting & modifying data in middleware
* Designing reusable backend components
* Enforcing application policies centrally

---

# 📧 Support

If you need help improving, debugging, or extending this project → just ask!
