# Usar una imagen base de Python
FROM python:3.10-alpine

# install bash
RUN apk add --no-cache bash

# Set the working directory to the containerr
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Admin auth for run.sh
RUN chmod +x run.sh

# Expose Port
EXPOSE 5000

# Defining environment variables
ENV FLASK_APP=/app/challenge-emprinet/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

# Execute Script
CMD ["sh", "./run.sh"]
