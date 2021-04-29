<img src="/assets/core_logo.png" width="400px">

**Core is the central application that powers many of our online services and events.**

<hr>

![CI](https://github.com/CarletonComputerScienceSociety/core/actions/workflows/workflow.yml/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/CarletonComputerScienceSociety/Core/blob/master/License)

<hr>

## Table of Contents
- [Context](#context)
- [Setup](#setup)
  - [Local](#non-docker-setup)
  - [Docker](#docker-setup)
- [Applications](#applications)
  - [Code Challenges](#code-challenges)
  - [Resources](#resources)
- [Commands](#commands)

## Context

Core is a Django based application. We used Django to build this application because of Django's "app based" structure and Django's preconfigured dashboard system. The hope is that to avoid having to configure and run several microservices, we can instead create new Django apps.

#### Services

 - Django (Core Application)
 - PostgreSQL
 - RabbitMQ
 - Celery

## Setup

Docker is recommended for application setup due to the high number of services required for this project.

### Non-Docker Setup

### 1. Create virtual environment

```bash
virtualenv venv -p python3
```

### 2. Activate virtual environment

```bash
source venv/bin/activate
```

You will also need to know how to deactivate your virtual environment later, which can be done by running the following:

```bash
deactivate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Update your Database configuration

Currently this application uses a postgres database, but for local development if may be quicker for you to use SQLite.

Open ```core/settings/base.py```

If you would like to use SQLite, uncomment the SQLite config. If you would like to use postgres, enter your postgres information.
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'ccss_resources',
#        'USER': 'postgres',
#        'PASSWORD': '1234',
#        'HOST': 'ccss_resources_db',
#        'PORT': 5432,
#    }
# }

```

### 5. Configure Django Environment Settings

```bash
export DJANGO_SETTINGS_MODULE=core.settings.dev
```

### 6. Migrate Database

```bash
python manage.py migrate
```

### 7. Start Django server

```bash
python manage.py runserver 0.0.0.0:8000
```

### 8. Start Rabbitmq (optional)

```bash
rabbitmq-server
```

### 9. Start Celery Worker (optional)

```bash
celery -A core worker -l info
```


### Docker Setup

Everything in this application is preconfigured to use host names from our docker-compose.yml.

```bash
docker-compose up
```

## Applications

### Code Challenges

The Code Challenges app is used to manage code challenge events.

<br>

<img src="/assets/codechallenges_schema.png" width="800px">

### Resources

The Resources app controls the dynamic content on the CCSS website. This app was created so volunteers could easily populate the website with resources, links, jobs postings and more.

<br>

<img src="/assets/resources_schema.png" width="800px">

## Useful Commands

Make migrations

```bash
python manage.py makemigrations PROJECTNAMEHERE
```

Make superuser

```bash
python manage.py createsuperuser
```

Create superuser in docker

```bash
docker exec -it DOCKERCONTAINERID python manage.py createsuperuser
```

Lint using Black

```bash
black .
```
