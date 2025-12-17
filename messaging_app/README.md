# 📦 Messaging App – CI/CD with Jenkins & GitHub Actions

## 📌 Project Overview

This project implements a **full CI/CD pipeline** for a Django-based messaging application using **Jenkins**, **GitHub Actions**, and **Docker**.

The goal is to automate:

* Code testing
* Code quality checks
* Docker image building
* Docker image deployment

This setup mirrors **real-world DevOps workflows** where every code change is automatically tested and deployed in a consistent and reliable way.

---

## 🛠️ Technologies Used

| Category         | Tools                   |
| ---------------- | ----------------------- |
| Backend          | Django, Python 3.10     |
| CI/CD            | Jenkins, GitHub Actions |
| Testing          | pytest, coverage        |
| Linting          | flake8                  |
| Containerization | Docker, Docker Hub      |
| Database         | MySQL                   |
| Version Control  | Git, GitHub             |

---

## 📂 Project Structure

```
messaging_app/
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── manage.py
├── requirements.txt
├── messaging_app/
├── chats/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── dep.yml
└── README.md
```

---

## 🔄 CI/CD Architecture

### 🔹 Jenkins (Manual CI/CD)

* Runs inside a Docker container
* Pulls source code from GitHub
* Runs Django tests using `pytest`
* Builds Docker images
* Pushes Docker images to Docker Hub
* Triggered manually from Jenkins UI

### 🔹 GitHub Actions (Automated CI/CD)

* Runs on every push and pull request
* Executes tests, linting, and coverage checks
* Builds and pushes Docker images on `main` branch
* Uses GitHub Secrets for secure credentials

---

## ⚙️ Jenkins Pipeline

### Jenkins Setup

Jenkins is run in Docker:

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

### Jenkinsfile Responsibilities

* Clone GitHub repository
* Install dependencies
* Run tests (`pytest`)
* Build Docker image
* Push Docker image to Docker Hub

📄 File: `messaging_app/Jenkinsfile`

---

## 🚀 GitHub Actions Workflows

### 1️⃣ Continuous Integration – `ci.yml`

Triggered on:

* Push
* Pull Request

Includes:

* MySQL service container
* Django tests (`pytest`)
* Linting (`flake8`)
* Coverage report generation
* Coverage artifact upload

📄 File: `.github/workflows/ci.yml`

---

### 2️⃣ Continuous Deployment – `dep.yml`

Triggered on:

* Push to `main` branch

Includes:

* Docker image build
* Docker Hub authentication
* Docker image push

📄 File: `.github/workflows/dep.yml`

---

## 🔐 Security & Secrets Management

### Jenkins Credentials

* `github-creds` → GitHub Personal Access Token
* `dockerhub-creds` → Docker Hub access token

### GitHub Secrets

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`

No credentials are hardcoded in the repository.

---

## 🧪 Testing & Code Quality

* **pytest** is used for unit testing
* **flake8** enforces Python code standards
* **coverage** generates test coverage reports
* Builds fail automatically if tests or linting fail

---

## 🐳 Dockerization

The application is containerized using Docker:

* Python 3.10 base image
* MySQL client dependencies installed
* Django application exposed on port `8000`

📄 File: `messaging_app/Dockerfile`

---

## ✅ How to Verify the Setup

### Jenkins

1. Open `http://localhost:8080`
2. Trigger the pipeline manually
3. Ensure the build finishes successfully (green)

### GitHub Actions

1. Push code to the repository
2. Check **Actions** tab on GitHub
3. Confirm workflows complete successfully

### Docker Hub

1. Visit Docker Hub repository
2. Confirm `messaging_app:latest` image exists

---

## 📈 Real-World Benefits

✔ Automated testing before code merges
✔ Early detection of bugs and style issues
✔ Faster and reliable deployments
✔ Secure handling of credentials
✔ Scalable CI/CD pipeline

---

## 🧩 Future Improvements

* Kubernetes deployment
* Security scanning (Trivy, Snyk)
* Zero-downtime rolling updates
* Production-grade environment separation

---

## 👥 Peer Review & Evaluation

This project is evaluated through:

* Manual QA review
* Peer reviews
* Verification of CI/CD workflows

All required files and workflows are included for successful evaluation.

---

## ✨ Author

**Aichalahnite**
ALX Software Engineering Program – Backend Specialization

---


