# django-cloud-run
Django running on Cloud Run, connecting to Cloud SQL

## Set up Python environment
This config uses pyenv to ensure the exact Python version is used, also it's a really nice clean way of controlling virtual environments.
However, feel free to use whatever virtual environment method you like.
```bash
# Install pyenv & pyenv-virtualenv first. Example: https://realpython.com/intro-to-pyenv/
# Install Python 3.7.3
pyenv install -v 3.7.3
# Create virtual environment
pyenv virtualenv 3.7.3 cms-back
# Activate virtual environment
pyenv local cms-back
```

## Install Python modules
```bash
## Install prereqs for mysqlclient Python module (we need mysql_config from somewhere)
# Ubuntu:
sudo apt install default-libmysqlclient-dev
# CentOS/RHEL:
yum install mariadb-devel
# Mac OS:
brew install mysql
PATH=$PATH:/usr/local/mysql/bin

# Install all required modules
pip install -r requirements.txt
```

## Set up local SQL Proxy
```bash
# Get credentials for the cms-sql-dev service account (you only need to do this once)
gcloud iam service-accounts keys create ~/key.json --iam-account cms-sql-dev@central-management-system.iam.gserviceaccount.com

# Start the SQL Proxy Docker container
docker run -d -v ~/key.json:/config -p 127.0.0.1:3306:3306 gcr.io/cloudsql-docker/gce-proxy:1.14 /cloud_sql_proxy -instances=central-management-system:us-central1:cms-back-tcr=tcp:0.0.0.0:3306 -credential_file=/config
```

## Run the Django server
```bash
python manage.py runserver
```

## Alternatively, build and run a Docker container
```
docker build -t djangocloudrun .
docker run -p 8000:8000 -e PORT=8000 djangocloudrun
```