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

## venv 
creat virtual env in this folder
start powershell in under the folder D:\Coding\DRFApiYouTube

    python -m venv .venv

activate env
start cmd or powershell

    D:\Coding\DRFApiYouTube>.venv\Scripts\activate

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

2. run django, quit by ctr-c

    python manage.py runserver 8000

3. start a new app named api in django

    (.venv) PS D:\Coding\DRFApi\backend> python manage.py startapp api

    add the name to cfehome\setting.py INSTALLED_APPS
    
4. creat view in api app

    def api_home in view.py
    
    creat urls.py in api folder, add urlpatterns

    add url in cfehome\urls.py

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