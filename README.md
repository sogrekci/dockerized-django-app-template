# A Dockerized Django Application Template

You can use this template to deploy your **Django** based web site (**Django** + **PostgreSQL** + **Gunicorn** + **Nginx** configuration) on Linux servers by containerizing with **Docker**.

Created and tested in the following environment: **Ubuntu 20.04**, **Docker 20.10.6**, **Docker-Compose 1.29.2**

### Usage

1. Remove the `dummyproject` folder and put your own Django project folder in place of it (the folder contains `manage.py`).
2. Create the `requirements.txt` file in your Django project folder (same place with `manage.py`) and append your dependicies in it (must have at least `django`, `gunicorn` and `psycopg2-binary`).
3. Edit `settings.py` of your Django project:
  * Alter `DATABASES` setting with the following:
```
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("POSTGRES_DB", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
```
  * Alter the Static Files settin with the following:
```
import os
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
```
4. Place your PostgreSQL database backup file (`datadump.sql`) in the `data-dump` folder if you have, **do not remove** this folder if you dont have a backup. If you have a large backup, then you might need to increase sleep time in `docker/entrypoint.webapp.sh`.
5. Edit `docker/env.webapp` file to set your project settings, the PostgreSQL user name must match the user appears in `data-dump/datadump.sql` if you have a backup in that folder.
6. Update the configuration files in the folder `docker` for your Django project name (that name is `dummyproject` in this repo, you should change this with your Django project name). You can use the simple script `change_app_name.py` for this purpose, run `python3 change_app_name` and answer the prompts (Old App Name = `dummyproject`).
7. Install [Docker](https://docs.docker.com/engine/install/) and [Docker-Compose](https://docs.docker.com/compose/install/) on the server, `cd` into docker directory (`dockerized-django-app-template/docker`).
8. Run `sudo docker-compose up -d --build` to build and start the container, run without `-d` flag to see what happened if you encounter any issues.
9. You can test your application now, visit your domain name or ip adress.
9. To stop the container, run `sudo docker-compose down` (add the `-v` flag to remove volumes, this clears newly added entries to database).
