FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
COPY App /app/App
COPY Domain /app/Domain

WORKDIR /app

RUN pip install libsvm-official
RUN pip install -r requirements.txt

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "80"]