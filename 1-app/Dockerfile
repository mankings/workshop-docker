# Base image
FROM python:3.8-alpine

# Image labels/tags
LABEL maintainer="Miguel Matos"

# Execute the command to create a folder for the application code
RUN mkdir /app

# Define the working directory inside the Docker container
WORKDIR /app

# Copy external files into the working directory
# In this case, copying python requirements file
COPY requirements.txt requirements.txt

# Install dependencies with pip
RUN pip install -r requirements.txt

# Copy the external code into the working directory
COPY app.py app.py

# Expose the port of the service
EXPOSE 8080/tcp

# Define the entrypoint/command to run when the container starts
ENTRYPOINT ["python3", "app.py"]