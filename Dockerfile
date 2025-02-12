FROM python:3.10-alpine

# install bash
RUN apk add --no-cache bash

# set workdir in container
WORKDIR /app

# Copy files to container
COPY . /app

# give permissions 
RUN chmod +x /app/run.sh

# install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# expose port 500
EXPOSE 5000

# execute run.sh
CMD ["/bin/sh", "-c", "/app/run.sh"]
