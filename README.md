<h3 align="center">Sound Cloud</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Sound Cloud is a audio library app written in Python, Django, Django Rest Framework

### Prerequisites

You must have Python installed, to check it

```
python --version
```

### Installing and running (without docker)

A step by step series of examples that tell you how to get a development env running.

Installing dependencies with pip

```
python -m pip -r install requirements.txt
```

Making model migrations

```
python ./manage.py makemigrations
```

Migrating into database

```
python ./manage.py migrate
```

Creating a superuser

```
python ./manage.py createsuperuser
```

Collecting static

```
python ./manage.py createsuperuser
```

Running app

```
python ./manage.py runserver
```

### Installing and running (with docker)

A step by step series of examples that tell you how to get a development env running.

Creating Docker image

```
docker-compose up --build
```

#### Note: at this part you have to open new terminal tab!

To watch what Docker containers are running now

```
docker ps
```

Collecting static

```
docker exec -it sound_cloud_web python manage.py collectstatic
```

Creating a superuser

```
docker exec -it sound_cloud_web python manage.py createsuperuser
```

## ⛏️ Built Using <a name = "built_using"></a>

- [PostgreSQL](https://www.postgresql.org/) - Database
- [Django](https://www.djangoproject.com/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Server Framework

## ✍️ Authors <a name = "authors"></a>

- [@serega-s](https://github.com/serega-s) -Initial Work
