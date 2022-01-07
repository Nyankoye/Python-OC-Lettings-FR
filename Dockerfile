FROM python:3.9-bullseye
WORKDIR /oc_lettings_project
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
CMD ["python", "manage.py", "runserver"]