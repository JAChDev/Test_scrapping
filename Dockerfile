FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
COPY App /app/App
COPY Domain /app/Domain

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libsvm-dev && \
    pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "80"]