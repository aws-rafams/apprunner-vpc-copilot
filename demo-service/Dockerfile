FROM python:3.8-alpine

WORKDIR /app

# Copy dependency file
COPY requirements.txt requirements.txt

# Install dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt

# Add source code into container image in path /app
COPY . /app

# Start the service
CMD ["python3", "frontend.py"]