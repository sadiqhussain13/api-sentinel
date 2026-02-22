FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \ 
    postgresql-client \ 
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x /app/manage.py

CMD ["sh", "-c", "python manage.py migrate && gunicorn -b 0.0.0.0:8000 wsgi:application"]