FROM python:3.8
WORKDIR /app
COPY . /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

ENV FLASK_APP=flaskr

# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn","--bind","0:5000","flaskr:app"]