FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/backend

RUN apt -y update && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

CMD ["/bin/sh", "-c", "python -m uvicorn server.main:app --host 0.0.0.0 --port 9000 --reload"]