FROM python:3.11

ENV pythonunbuffered 1

RUN mkdir /my_voting_app

WORKDIR /my_voting_app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
