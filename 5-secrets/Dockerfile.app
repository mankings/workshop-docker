FROM python:3.8-alpine

LABEL maintainer="Miguel Matos"

RUN mkdir /app
RUN mkdir /app/www

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 8080/tcp

VOLUME /app/www

ENTRYPOINT ["python3", "app.py"]