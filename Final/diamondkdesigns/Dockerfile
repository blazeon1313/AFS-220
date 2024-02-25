FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y apache2-dev
RUN pip install -r requirements.txt

COPY . .


EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]