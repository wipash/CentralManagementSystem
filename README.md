# CentralManagementSystem
[![Build Status](https://travis-ci.com/torontocatrescue/CentralManagementSystem.svg?branch=develop)](https://travis-ci.com/torontocatrescue/CentralManagementSystem)
[![codecov](https://codecov.io/gh/torontocatrescue/CentralManagementSystem/branch/develop/graph/badge.svg)](https://codecov.io/gh/torontocatrescue/CentralManagementSystem)


## Build and run with Docker

## Dev environment
```bash
# The cloud-sql-proxy service will start in the background the first time you
# run these commands, and will continue running even when cms-back-dev stops

# Start in foreground:
docker-compose --file .\docker-compose-dev.yml up --build cms-back-dev

# Start in background:
docker-compose --file .\docker-compose-dev.yml up --build --detach cms-back-dev

# Clean up, and stop any detached services (including cloud-sql-proxy)
docker-compose down
```

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
