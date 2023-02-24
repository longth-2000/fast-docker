FROM python:3.10

WORKDIR /code

COPY . .

RUN pip install fastapi uvicorn
RUN pip install sqlalchemy
RUN pip install sqlalchemy[mysql]
RUN pip install debugpy

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]