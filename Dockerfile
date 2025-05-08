FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app/app.py"]
