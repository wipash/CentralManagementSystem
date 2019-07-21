# CentralManagementSystem
[![Build Status](https://travis-ci.com/torontocatrescue/CentralManagementSystem.svg?branch=develop)](https://travis-ci.com/torontocatrescue/CentralManagementSystem)

## Build and run with Docker

## Dev environment
Coming soon

## Staging environment
``` bash
# Generate credentials for the Cloud SQL service account
gcloud iam service-accounts keys create cms-sql-dev-key.json --iam-account cms-sql-dev@central-management-system.iam.gserviceaccount.com

# Build latest version:
docker-compose build

# Run:
docker-compose up

# Run manage.py commands:
docker-compose run cms-back python manage.py showmigrations
```
* Frontend: http://localhost:8080
* Backend: http://localhost:8081
