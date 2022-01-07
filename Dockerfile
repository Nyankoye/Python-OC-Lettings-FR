FROM python:3.9-bullseye
WORKDIR /oc_lettings_project
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]