FROM python:3.9

RUN apt-get update -y
ENV PYTHONUNBUFFERED=1
COPY . .
RUN chmod +x ./entrypoint.sh
RUN pip install -r requirements.txt
