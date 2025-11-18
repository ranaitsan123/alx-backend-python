# 📘 **Messaging App — Docker Setup Tutorial**

This project uses **Docker** to fully manage the Django environment.
You do **not** need Python installed on your machine — Docker handles everything:

✔ Installing packages
✔ Creating the Django project
✔ Creating Django apps
✔ Running manage.py commands
✔ Running the development server

---

# 🚀 **1. Project Setup**

Create your project folder:

```bash
mkdir messaging_app
cd messaging_app
```

---

# 🐳 **2. Docker Configuration**

The project uses:

* `Dockerfile` → defines the Django environment
* `docker-compose.yml` → runs Django server
* `requirements.txt` → Python dependencies
* `.env` → environment variables

---

## **2.1 Dockerfile**

Create a file named **Dockerfile**:

```dockerfile
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (required for Django + psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/
```

---

## **2.2 requirements.txt**

Create:

```
Django>=5.0
djangorestframework
django-environ
psycopg2-binary
```

---

## **2.3 docker-compose.yml**

Create:

```yaml
version: '3.9'

services:
  web:
    build: .
    container_name: messaging_app_web
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
```

---

## **2.4 .env file**

Create:

```
DEBUG=1
SECRET_KEY=change-me
```

---

# 🏗️ **3. Initialize Django Project Using Docker**

Since Django is not installed locally, we use Docker to create the project.

### Create the Django project:

```bash
docker-compose run web django-admin startproject messaging_app .
```

This command will generate:

```
manage.py
messaging_app/
    settings.py
    urls.py
    wsgi.py
    asgi.py
```

---

# 🧩 **4. Create the “chats” App**

Still using Docker:

```bash
docker-compose run web python manage.py startapp chats
```

This creates:

```
chats/
    models.py
    views.py
    apps.py
    ...
```

---

# 🛠️ **5. Applying Migrations**

Run:

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python.manage.py migrate
```

This initializes your database tables.

---

# ▶️ **6. Run the Server**

Start the app:

```bash
docker-compose up
```

Access the development server:

👉 [http://localhost:8000/](http://localhost:8000/)

Stop the server:

`CTRL + C`

---

# ⚙️ **7. Running Django Commands via Docker**

Some useful examples:

### Create superuser

```bash
docker-compose run web python manage.py createsuperuser
```

### Django shell

```bash
docker-compose run web python manage.py shell
```

### Run tests

```bash
docker-compose run web python manage.py test
```

---

# 📦 **8. Installing New Packages**

1. Add the package to `requirements.txt`
2. Rebuild Docker:

```bash
docker-compose build
```

That's it — Docker will reinstall everything.

---

# 🎉 **You Are Ready to Build Your API**

After completing the Docker setup, proceed with:

* Custom user model
* Conversation model
* Message model
* Serializers
* ViewSets
* URL routing

