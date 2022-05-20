FROM python:3.8

WORKDIR /Moadata
COPY . /Moadata

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

ENV FLASK_APP=flaskr

CMD ["gunicorn", "--bind", "0:5000", "flaskr:app"]