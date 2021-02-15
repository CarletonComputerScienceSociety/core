<img src="/assets/core_logo.png" width="400px">

**Core is the central application that powers many of our online services and events.**

<hr>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/CarletonComputerScienceSociety/Core/blob/master/License)

<hr>

## Table of Contents
- [Context](#context)
- [Setup](#setup)
  - [Local](#local)
  - [Docker](#docker)
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

### Local

If you do not have a virtual environment

```bash
virtualenv venv -p python3
```

Activate virtual environment

```bash
source venv/bin/activate
```

Deactivate virtual environment

```bash
deactivate
```

Start Rabbitmq

```bash
rabbitmq-server
```

Start Celery Worker

```bash
celery -A core worker -l info
```

Configure Django Environment Settings

```bash
export DJANGO_SETTINGS_MODULE=core.settings.dev
```

Setup Django Application

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Docker

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

## Commands

Make migrations

```bash
python manage.py makemigrations PROJECTNAMEHERE
```

Create superuser in docker

```bash
docker exec -it DOCKERCONTAINERID python manage.py createsuperuser
```