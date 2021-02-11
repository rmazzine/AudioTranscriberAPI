FROM python:3.7-slim
WORKDIR /flaskapp
ADD ./flaskapp/ /flaskapp
ADD ./requirements.txt /flaskapp
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install libsndfile1 -y
RUN apt-get install ffmpeg -y
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:3800", "wsgi", "--timeout", "600"]