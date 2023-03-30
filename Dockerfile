FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /App
COPY . /Domain
CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8080"]