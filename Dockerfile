FROM python:3.10.6

ENV PYTHONUNBUFFERED 1
ENV MODE=development

WORKDIR /opt/backend

RUN apt -y update && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "server.server:app", "--host", "0.0.0.0", "--port", "9001", "--reload"]