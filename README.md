# Mise à l'échelle d'une application Django en utilisant une architecture modulaire 

- Site web d'Orange County Lettings

Ce projet a été forké dans le but de me permettre de developper des competences dans:
- La mise en place d'un pipline CI/CD en utilisant CircleCI
- La création d'une image docker
- Le deploiement d'une image docker sur Heroku
- La mise en place d'un sytème de controle de code en utilisant sentry
- La refactorisation d'une application pour reduire les dettes techniques
- l'application une architecture modulaire dans une application Python

#### Pipline CI/CD
1. A chaque commit sur la branche master le pipline CI/CD va d'abord tester le code, si tout est ok
2. Il passe à la construction de l'image docker, puis la pousse sur mon docker hub avec un tag representant le numero de commit sur CircleCI
3. Après ces deux étapes, l'image est ensuite deploiyée sur heroku
- Vous pouvez consulter [l'application sur heroku](https://oc-lettings-14.herokuapp.com/)

## Execution du code
1. Cloner ce dépôt de code à l'aide de la commande: <code>$ git clone https://github.com/Nyankoye/Python-OC-Lettings-FR </code>
2. Créez un environnement virtuel dans le projet en utilisant la commande: <code> $ python -m venv env </code>
3. Activer l'environnement <code> source venv/bin/activate </code>
    - sur windows <code> .\venv\Scripts\activate </code>
    - Pour désactiver l'environnement, `deactivate`
4. Installer les paquets Python répertoriés dans le fichier requirements.txt en utilisant la commande : <code>$ pip install -r requirements.txt </code>
5. Vous deplacez dans le repertoir suivant: <code> cd /path/to/Python-OC-Lettings-FR </code>
6. Demarrer l'application en utilisant la commande: <code> $ python manage.py runserver </code>
7. Aller sur `http://localhost:8000` dans un navigateur.

## Tests unitaires
Pour lancer les tests unitaires, il vous suffit de:
- Vous deplacez dans le repertoir suivant: <code> cd /path/to/Python-OC-Lettings-FR </code>
- Puis utiliser la commande: <code> $ python manage.py test </code>

## Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Déploiement
Le déploiement de notre application consistera à la mettre en production notre application sur heroku. Afin qu'elle soit consultable par n'importe qui, pour cela nous allons utiliser docker et heroku 
1. Intaller [docker](https://docs.docker.com/get-docker/) sur votre machine
2. Créer un fichier Dockerfile à la source du projet: `/path/to/Python-OC-Lettings-FR`
    ```
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
    ```
    - PYTHONDONTWRITEBYTECODE : Empêche Python d'écrire des fichiers pyc
    - `$PORT` est une variable d'environnement de heroku, pendant l'execution de l'image en local il faudra spécifier le port
3. Ajouter guinicorn dans la liste des module requis
4. Ajouter whitenoise dans la liste des module requis et modifier les variables d'environnement SECRET_KEY, DEBUG, et ALLOWED_HOSTS dans settings.py :
    ```
    SECRET_KEY = os.environ.get('SECRET_KEY', default='foo')
    DEBUG = int(os.environ.get('DEBUG', default=0))
    ALLOWED_HOSTS = ["oc-lettings-14.herokuapp.com","localhost","127.0.0.1"]  
    ```
5. Modifier middleware dans settings.py pour ajourer Whitenoise
    ```
    MIDDLEWARE = [
    # ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    ```
    - Configurez la gestion de vos fichiers statiques avec STATIC_ROOT:
        ```
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        ```
6. Construiser et excuter l'image en local: 
   ``` 
   docker build -t mon_app .
   docker run -d -e "PORT=8000" -e "DEBUG=1" -p 8000:8000 mon_app
   ```
7. Après avoir fait le Dockerfile, le fichier `config.yml` se trouvant dans le repertoire: `path\Python-OC-Lettings-FR\.circleci` s'occuppera de faire le depoiement de l'application sur heroku après chaque commit sur la branch master 
- les commandes suivante seront exécuter grâce au fichier de config:
    ```
    $ heroku container:login
    $ heroku container:push -a nom_app web
    $ heroku container:release -a nom_app web
    ```
      
### Utilisation de l'image docker en local
- Afin d'executer l'image que j'ai contruit pour deployer l'application sur heroku, utiliser la commande : <code> $ docker run -d -e "PORT=8000" -e "DEBUG=1" -p 8000:8000 nyankoye/oc_lettings_project:0.0.136 </code>
