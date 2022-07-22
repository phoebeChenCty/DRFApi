---
title: "My Notes"
output:
  html_document:
    number_sections: true
  pdf_document:
    number_sections: true
---

# Django Rest Framework Api
    https://www.youtube.com/watch?v=c708Nf0cHrs&list=PL4hq-GKoM2Tq7q6bnTxOvHcsrZ28mo4Mw&index=4&t=130s
    https://www.youtube.com/watch?v=VBqJ0-imSMU&t=14573s (router and model viewset)

## venv 
creat virtual env in this folder
start powershell in under the folder D:\Coding\DRFApi

    python -m venv .venv

activate env
start cmd or powershell

    D:\Coding\DRFApi>.venv\Scripts\activate

install package
create requirements.txt

    pip install -r requirements.txt

install package
    python -m pip install numpy

install autopep8 for formating

## Django
1. start django project

    cd backend
    django-admin startproject cfehome .
    there's a period in the end

2. run server, quit by ctr-c

    python manage.py runserver 8000

3. start a new app named api in django

    (.venv) PS D:\Coding\DRFApi\backend> python manage.py startapp api

    add the name to cfehome\setting.py INSTALLED_APPS
    
4. creat view in api app

    def api_home in view.py
    
    creat urls.py in api folder, add urlpatterns=[], not use {}

    add url in cfehome\urls.py

5. creat database (change models.py first)
    python manage.py makemigrations # let the database know everything in models.py
    python manage.py migrate # update the database based on the change of models.py

6. open django shell
    python manage.py shell

7. Django REST Framework
    add rest_framework to cfehome\setting.py INSTALLED_APPS

8. use generics api view
    add ProductDetailAPIView(generics.RetrieveAPIView) in Product/views.py

9. create all database instance urls in one place.
    create urls.py in product
    update cfehome/urls.py

## install django-cors-headers, so that frontend can visit
    https://pypi.org/project/django-cors-headers/
    1. 
        INSTALLED_APPS = [
        ...,
        "corsheaders",
        ...,
        ]
    2. 
        MIDDLEWARE = [
        ...,
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        ...,
        ]
    3. 
        CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        ]

## Celery & redis
    1. install redis in wsl: https://developer.redis.com/create/windows/
    2. start redis (in wsl)
        redis-server
    3. python -m pip install celery
        python -m pip install redis
    4. edit __init__.py, celery.py, settings.py in cfehome folder to set celery
    5. queue up task and start worker: in backend folder
        in Django shell:
            python manage.py shell
            >>> from cfehome.celery import debug_task
            >>> debug_task.delay() # add task to queue
            >>> exit()
    6. start a worker to process the task, in backend folder
        celery -A cfehome.celery worker --loglevel=info


    
## rename folder in workspace

    Open workspace settings
    Rename folder from command line: mv old new (shutdown ongoing terminal)
    Rename the path in the folders settings of workspace, and save

## Git
1. create new git repo
2. in root directory of the project folder
    
    git init
3. create .gitignore file, add 

    .venv/
4. push to git

        git add -A
        git commit -m 'Added my project'
        git remote add origin https://github.com/phoebeChenCty/DRFApi.git (use http)
        git branch -M master
        git push -u origin master
5. switching remote urls from ssh to http
https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories#removing-a-remote-repository

## create python client
run client

    (.venv) PS D:\Coding\DRFApi> python .\py_client\basic.py

the endpoint must has the same port as server