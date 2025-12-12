FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Expose port (run with: docker run -p 8000:8000 image)
EXPOSE 8000

CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
git 