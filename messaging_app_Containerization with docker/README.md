# Messaging App API

A Django REST Framework (DRF) project for managing users, conversations, and messages. Designed to provide a robust backend for chat applications with modular architecture, authentication, and API endpoints.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Setup & Installation](#setup--installation)
6. [Docker Setup](#docker-setup)
7. [Database & Migrations](#database--migrations)
8. [API Endpoints](#api-endpoints)
9. [Testing](#testing)
10. [Contributing](#contributing)
11. [License](#license)

---

## Project Overview

This project is a backend service for messaging applications. Users can participate in conversations, send messages, and retrieve message histories. Built with Django REST Framework for scalable and maintainable API design.

Key focus:

* Modular Django apps (`chats`)
* RESTful endpoints
* Authentication using Django’s default User model (extended)
* Filtering and querying for conversations and messages

---

## Features

* **User Management:** Create, list, and manage users.
* **Conversations:** Create conversations involving multiple users.
* **Messages:** Send messages to existing conversations.
* **Filtering:** Query conversations by participant email and messages by sender or conversation ID.
* **Authentication:** API access protected using token or session-based authentication.
* **Dockerized:** Run the app in Docker containers for consistent development and deployment.

---

## Tech Stack

* Python 3.11
* Django 4.x
* Django REST Framework
* SQLite (development, can swap for Postgres in production)
* Docker & Docker Compose

---

## Project Structure

```
messaging_app/
│
├── chats/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── messaging_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── db.sqlite3
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/alx-backend-python.git
cd messaging_app
```

### 2. Install Python dependencies (without Docker)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Docker Setup

### 1. Build Docker containers

```bash
docker-compose build
```

### 2. Start containers

```bash
docker-compose up -d
```

### 3. Access the web container

```bash
docker-compose exec web bash
```

### 4. Run Django commands inside container

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver 0.0.0.0:8000
```

### 5. Stop and remove containers

```bash
docker-compose down
```

---

## Database & Migrations

* The project uses **SQLite** by default.
* All migrations are located in `chats/migrations/`.
* To reset the database (e.g., during development):

```bash
docker-compose down --volumes
rm db.sqlite3
docker-compose up -d
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

---

## API Endpoints

### Conversations

* `GET /api/conversations/` — List all conversations
* `POST /api/conversations/` — Create a new conversation
* `POST /api/conversations/{id}/send-message/` — Send message in a conversation

### Messages

* `GET /api/messages/` — List all messages
* `POST /api/messages/` — Create a message
* Filter messages: `?sender=email` or `?conversation=id`

> **Note:** You can filter conversations by participant email: `/api/conversations/?participant=user@example.com`

---

## Testing

* Unit and integration tests are located in `chats/tests/`.
* Run tests with:

```bash
docker-compose exec web python manage.py test
```

---

## Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make changes and commit (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature/your-feature`)
5. Create a pull request

---

## License

This project is licensed under the MIT License.
© 2025 ALX, All rights reserved.

