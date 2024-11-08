FROM python:3.10

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

