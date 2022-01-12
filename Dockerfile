FROM python:3.9-bullseye
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0
WORKDIR /oc_lettings_project
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
# collect static files 
RUN python manage.py collectstatic --noinput
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT