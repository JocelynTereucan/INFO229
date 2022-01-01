FROM python:3.6.3

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE $BIND_PORT

COPY . /app
CMD [ "python", "app/main.py" ]
