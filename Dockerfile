FROM python:3.9

WORKDIR /app

COPY . /app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 80

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]