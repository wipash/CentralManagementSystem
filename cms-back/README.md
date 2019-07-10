# django-cloud-run
Django running on Cloud Run, connecting to Cloud SQL

# Docker-compose
Generate credentials for the Cloud SQL service account
```bash
gcloud iam service-accounts keys create cms-sql-dev-key.json --iam-account cms-sql-dev@central-management-system.iam.gserviceaccount.com
```
Start the environment
```bash
docker-compose up --build
```

# Docker
Generate credentials for the Cloud SQL service account
```bash
gcloud iam service-accounts keys create cms-sql-dev-key.json --iam-account cms-sql-dev@central-management-system.iam.gserviceaccount.com
```

Start the SQL Proxy Docker container
```bash
docker run -d -v ${PWD}/cms-sql-dev-key.json:/config.json -p 127.0.0.1:3306:3306 gcr.io/cloudsql-docker/gce-proxy:1.14 /cloud_sql_proxy -instances=central-management-system:us-central1:cms-back-tcr=tcp:0.0.0.0:3306 -credential_file=/config.json
```

Build and run the docker container
```bash
docker build -t cms-back .
docker run -p 8000:8000 -e PORT=8000 cms-back
```


# Local dev environment

## Set up Python environment
Using Pyenv
```bash
# Install pyenv & pyenv-virtualenv first. Example: https://realpython.com/intro-to-pyenv/
# Install Python 3.7.3
pyenv install -v 3.7.3
# Create virtual environment
pyenv virtualenv 3.7.3 cms-back
# Activate virtual environment
pyenv local cms-back
```

Using venv, for example on Windows:
```
python -m venv env
.\env\Scripts\Activate.ps1
```

## Install prereqs for mysqlclient Python module
### Ubuntu:
```
sudo apt install default-libmysqlclient-dev
```
### CentOS/RHEL:
```
sudo yum install mariadb-devel
```
### MacOS:
```
brew install mysql
PATH=$PATH:/usr/local/mysql/bin
```

## Install Python modules
```
pip install -r requirements.txt
```

## Set up local SQL Proxy
```bash
# Get credentials for the cms-sql-dev service account (you only need to do this once)
gcloud iam service-accounts keys create cms-sql-dev-key.json --iam-account cms-sql-dev@central-management-system.iam.gserviceaccount.com

# Start the SQL Proxy Docker container
docker run -d -v ${PWD}/cms-sql-dev-key.json:/config.json -p 127.0.0.1:3306:3306 gcr.io/cloudsql-docker/gce-proxy:1.14 /cloud_sql_proxy -instances=central-management-system:us-central1:cms-back-tcr=tcp:0.0.0.0:3306 -credential_file=/config.json
```

## Run the Django server
```bash
python manage.py runserver
```

## Alternatively, build and run a Docker container
```
docker build -t cms-back .
docker run -p 8000:8000 -e PORT=8000 cms-back
```
