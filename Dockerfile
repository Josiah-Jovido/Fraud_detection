FROM python:3.9.0

WORKDIR /app

COPY . /app

RUN pip install -r requirements_1.txt

ENTRYPOINT ["python"]

CMD ["flask_app.py"]
