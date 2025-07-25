FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
