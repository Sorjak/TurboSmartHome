FROM python:3.6

ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE=settings.local
ENV DJANGO_SECRET_KEY=8@or@bb!%9s_&mumqdz*rhg5+7!^88d97um55wpu%5fqpxnga)
ENV DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

RUN mkdir /app


COPY requirements/local.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

WORKDIR /app

CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]



