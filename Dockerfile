FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./main.py"]

HEALTHCHECK --interval=5m --timeout=3s \
  CMD python -c "import requests; requests.get('http://localhost:5000/healthz')"