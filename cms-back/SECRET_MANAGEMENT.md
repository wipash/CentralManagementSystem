# Travis Secrets
Travis needs to have credentials for a service account to decrypt Berglas secrets, and to run tests against the Cloud SQL database.

## Initial Setup
Create a service account, and grant access to Cloud SQL:
```bash
export SA_NAME=travis-sa
gcloud beta iam service-accounts create ${SA_NAME} \
  --description "Service Account for Travis CI" \
  --display-name ${SA_NAME}

export PROJECT_ID=central-management-system
export SA_EMAIL=$(gcloud iam service-accounts list --filter="NAME=${SA_NAME}" --format="value(EMAIL)")

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member serviceAccount:${SA_EMAIL} \
  --role roles/cloudsql.editor
```

This account will also need to be granted access to any required Berglas secrets (required Berglas, see [here](#install-berglas)):
```bash
export BUCKET_ID=cms-secrets
./berglas grant ${BUCKET_ID}/cms-devsql-password --member serviceAccount:${SA_EMAIL}
```

## Export and Encrypt Keys
You first need the [Travis CLI](https://github.com/travis-ci/travis.rb) installed:
```bash
sudo apt install ruby ruby-dev make gcc
sudo gem install travis
```
Log in to Travis, using your GitHub credentials
```bash
travis login --com

# You can also use a GitHub access token:
travis login --com --github-token YOURTOKEN
```

Dump the credential file for the service account we just created, and encrypt it using Travis:
```bash
gcloud iam service-accounts keys create ${SA_NAME}-key.json --iam-account ${SA_EMAIL}
travis encrypt-file --com ${SA_NAME}-key.json
```

Take note of the output, and add the relevant command to .travis.yml to decrypt the file

# Berglas Secrets
This project uses [Berglas](https://github.com/GoogleCloudPlatform/berglas) to securely store secrets. Berglas encrypts secrets using a key stored in [Google KMS](https://console.cloud.google.com/security/kms/keyring/manage/global/berglas?project=central-management-system), and then stores them in a [Cloud Storage bucket](https://console.cloud.google.com/storage/browser/cms-secrets?project=central-management-system).

Before managing keys, you'll need to [install & set up](#initial-setup-1) the Berglas CLI.

## Setup Environment

```bash
export PROJECT_ID=central-management-system
export BUCKET_ID=cms-secrets
export RUN_ID=cmsback
export KMS_KEY=projects/${PROJECT_ID}/locations/global/keyRings/berglas/cryptoKeys/berglas-key
export SA_EMAIL=$(gcloud beta run configurations describe ${RUN_ID} --region=us-central1 --platform=managed --format="value(spec.template.spec.serviceAccountName)")
```

## Normal usage

### Create or overwrite a key

1. Create or overwrite existing key
```bash
./berglas create ${BUCKET_ID}/secret-name "MyP@55w0rd"\
  --key ${KMS_KEY}
```

2. Get the Cloud Run service account's email
```bash
export SA_EMAIL=$(gcloud beta run configurations describe ${RUN_ID} --region=us-central1 --platform=managed --format="value(spec.template.spec.serviceAccountName)")
```

3. Grant Cloud Run service account access to the secret
```bash
./berglas grant ${BUCKET_ID}/foo --member serviceAccount:${SA_EMAIL}
```

4. Grant dev service account access to the secret, only required for secrets that need to be read in dev/staging/test
```bash
./berglas grant ${BUCKET_ID}/foo --member serviceAccount:cms-sql-dev@central-management-system.iam.gserviceaccount.com
```


### Use the secret
1. Declare environment variables in format `berglas://${BUCKET_ID}/secret-name`
```bash
export DATABASE_PASSWORD=berglas://cms-secrets/cms-devsql-password
```
2. Execute app using Berglas
```bash
./berglas exec -- sh ./run.sh
```


## Initial setup

### Install Berglas

1. Log in to Gcloud SDK to generate Default Application Credentials
```bash
gcloud auth application-default login
```

2. Download Berglas
```bash
wget https://storage.googleapis.com/berglas/master/linux_amd64/berglas
chmod +x ./berglas
```

### Set up a new Google Cloud Platform project
This step is only required once, at the beginning of a new project.

1. Enable required services
```bash
gcloud services enable --project ${PROJECT_ID} \
  cloudkms.googleapis.com \
  storage-api.googleapis.com \
  storage-component.googleapis.com
```

2. Create storage bucket and keyring
```bash
./berglas bootstrap --project ${PROJECT_ID} --bucket ${BUCKET_ID}
```

3. Enable auditing
```bash
gcloud projects get-iam-policy ${PROJECT_ID} > policy.yaml

cat <<EOF >> policy.yaml
auditConfigs:
- auditLogConfigs:
  - logType: DATA_READ
  - logType: ADMIN_READ
  - logType: DATA_WRITE
  service: cloudkms.googleapis.com
- auditLogConfigs:
  - logType: ADMIN_READ
  - logType: DATA_READ
  - logType: DATA_WRITE
  service: storage.googleapis.com
EOF

gcloud projects set-iam-policy ${PROJECT_ID} policy.yaml
rm policy.yaml
```

4. Grant the service account access to read the Cloud Run deployment's environment variables
```bash
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member serviceAccount:${SA_EMAIL} \
  --role roles/run.viewer
```
