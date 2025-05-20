FROM python:3.8-alpine

LABEL maintainer="Miguel Matos"

RUN mkdir /app

# Make an extra folder for the data
RUN mkdir /app/www

# All the same
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
EXPOSE 8080

# Define a local volume for the data
VOLUME /app/www

CMD ["python3", "app.py"]
