FROM python:3.12-alpine

LABEL maintainer="Miguel Matos"

RUN mkdir -p /app/www

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 8080

CMD ["python3", "app.py"]
