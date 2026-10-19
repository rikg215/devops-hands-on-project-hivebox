FROM python:3.15.0-slim

COPY app.py /app/

WORKDIR /app/

CMD ["python", "app.py"]