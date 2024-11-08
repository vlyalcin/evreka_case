FROM python:3.10

WORKDIR /code

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY ../evreka_case /code/evreka_case
COPY ../manage.py /code/manage.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
