FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py populate_database && python3 manage.py runserver 0.0.0.0:8000"]