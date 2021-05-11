# DjangoREST

A Django REST API template

By Yoann NOUVEAU


## How to run the servers

First boot up the backend, then the frontend,

## Backend



### 0) Dependencies
* [Django](https://www.djangoproject.com/)
* [djangorestframework](https://www.django-rest-framework.org/)
* [django-cors-headers](https://pypi.org/project/django-cors-headers/)

```sh
pip install djangorestframework markdown django-filter django-cors-headers
```

### 1) Run Server

```sh
python manage.py runserver
```

### 2) Migrate

```sh
python manage.py makemigrations
python manage.py migrate
```

### Backend Extras

#### Make a Super User

```sh
python manage.py createsuperuser
>> username
>> email
>> pwd
```
