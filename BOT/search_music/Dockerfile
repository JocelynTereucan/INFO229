FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3

RUN pip install mysql.connector
RUN pip install pika
RUN pip install youtube-search
RUN pip install google-api-python-client
ENV PYTHONUNBUFFERED 1

COPY ./manager.py ./manager.py

CMD ["python", "manager.py"]