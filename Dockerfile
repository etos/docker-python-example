FROM python:3.9.0-slim-buster

# SYS
RUN apt-get update
RUN apt-get install -y build-essential

# APP
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "src/" ]
