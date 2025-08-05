FROM python:3.11-slim

WORKDIR /app
COPY . /app

#COPY requirements.txt /tmp/requirements.txt

RUN pip install -r requirements.txt

CMD ["python","-m","http.server","8000"]