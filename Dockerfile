FROM python:3.9-slim-buster
WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

# copy ui directories to image
COPY ./ui /app/ui
COPY ./src /app/src
COPY ./data /app/data

ENV PYTHONPATH /app
EXPOSE 8080

CMD python ui/app.py