FROM python:3

# Set environment variable to avoid buffering issues with Python
ENV PYTHONUNBUFFERED 1

# Install system dependencies (including distutils)
RUN apt-get update && apt-get install -y python3-distutils

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from the djangoLearn folder into the container's /app
COPY ./ /app