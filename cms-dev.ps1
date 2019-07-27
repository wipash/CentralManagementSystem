[CmdletBinding()]
param(
    [string] $Project,
    [string] $Command
)

# Project settings
$PROJECT_ID = "central-management-system"
$SERVICE_ACCOUNT = "cms-sql-dev"

# Docker-compose file settings
$DOCKER_COMPOSE_DEV_FILE = Join-Path $PWD "docker-compose-dev.yml"
$DOCKER_COMPOSE_PROD_FILE = Join-Path $PWD "docker-compose-prod.yml"
$DOCKER_COMPOSE_OVERRIDE_FILE = New-TemporaryFile

# Derived variables
$KEY_FILE_NAME = "$SERVICE_ACCOUNT-key.json"
$KEY_FILE_PATH = Join-Path $PWD $KEY_FILE_NAME
$SERVICE_ACCOUNT_EMAIL = "$SERVICE_ACCOUNT@$PROJECT_ID.iam.gserviceaccount.com"


Function Initialize-Gcloud {
    # Check that we're logged in to gcloud
    $auth = gcloud auth list --filter=status:ACTIVE --format json | ConvertFrom-Json
    if (!$auth) {
        Write-Host -ForegroundColor Yellow "You aren't signed in to Gcloud. Signing you in now."
        Connect-GcloudSDK
    }

    # Check that the default project is set correctly
    $config = gcloud config list --format json | ConvertFrom-Json
    if ($config.core.project -ne $PROJECT_ID) {
        Write-Host -ForegroundColor Yellow "Wrong project set as default ($($config.core.project)), changing to $PROJECT_ID"
        Set-GcloudDefaultProject
    }

    # Check that the service account key config file is present and valid
    Test-GcloudServiceAccountKeyFile -Create $true

    Write-Host -ForegroundColor Green "Everything looks good!"

}

Function Connect-GcloudSDK {
    $result = gcloud auth login --format json | ConvertFrom-Json
    if ($result.access_token) {
        Write-Host -ForegroundColor Green "Successfully logged in"
    }
    else {
        Write-Host -ForegroundColor Red "Could not log in, please try manually with:"
        Write-Host -ForegroundColor Yellow "gcloud auth login"
        exit 1
    }
}

Function Set-GcloudDefaultProject {
    $projects = gcloud projects list --format json | ConvertFrom-Json
    if ($projects.name -eq $PROJECT_ID) {
        gcloud config set project $PROJECT_ID
    }
    else {
        Write-Host -ForegroundColor Red "Project $PROJECT_ID is not available with your current login."
        exit 1
    }

}

Function Test-GcloudServiceAccountKeyFile {
    Param (
        [boolean] $Create = $false
    )
    if (!(Test-Path -Path $KEY_FILE_PATH)) {
        Write-Host -ForegroundColor Yellow "No service account key file"
        if (!$Create) {
            Write-Host -ForegroundColor Red "Please run ""$(Split-Path $MyInvocation.PSCommandPath -Leaf) setup"""
            exit 1
        }
        Get-GcloudServiceAccountKeyFile
    }
    else {
        $keyfile = Get-Content -Path $KEY_FILE_PATH | ConvertFrom-Json
        if ($keyfile.client_email -ne $SERVICE_ACCOUNT_EMAIL) {
            Write-Host -ForegroundColor Red "Key file $KEY_FILE_NAME is for an incorrect account"
            exit 1
        }
    }
}

Function Get-GcloudServiceAccountKeyFile {
    Write-Host -ForegroundColor Green "Requesting new key file for $SERVICE_ACCOUNT"
    gcloud iam service-accounts keys create $KEY_FILE_PATH --iam-account $SERVICE_ACCOUNT_EMAIL --format json | ConvertFrom-Json
    if (!(Test-Path -Path $KEY_FILE_PATH)) {
        Write-Host -ForegroundColor Red "Key file generation failed"
        exit 1
    }
}

Function New-DockerOverrideFile {
    "---
version: '3'
services:
  cms-back-dev:
    volumes:
      - $($KEY_FILE_PATH):/config.json
  cloud-sql-proxy:
    volumes:
      - $($KEY_FILE_PATH):/config.json
" | Out-File $DOCKER_COMPOSE_OVERRIDE_FILE
}


Function Invoke-DockerCompose {
    Param (
        [Parameter(Mandatory=$True)]
        $args
    )
    Test-GcloudServiceAccountKeyFile
    # Create docker-compose override file to set the path to the key file
    New-DockerOverrideFile
    &docker-compose --file $DOCKER_COMPOSE_DEV_FILE --file $DOCKER_COMPOSE_OVERRIDE_FILE $args
}

switch -Regex ($Project) {
    "setup" {
        Initialize-Gcloud
    }
    "stop|down" {
        Invoke-DockerCompose -args @("down")
    }
    "ps" {
        Invoke-DockerCompose -args @("ps")
    }
    "cms-back" {
        switch -Regex ($Command) {
            "setup" {
                Initialize-Gcloud
            }
            "build" {
                Invoke-DockerCompose -args @("build")
            }
            "dev" {
                Invoke-DockerCompose -args @("up", "--build", "cms-back-dev")
            }
            "test" {
                Invoke-DockerCompose -args @("run", "--rm", "cms-back-dev", "python", "manage.py", "test")
            }
            "flake8" {
                Invoke-DockerCompose -args @("run", "--rm", "--no-deps", "cms-back-dev", "flake8")
            }
            "makemigrations" {
                Invoke-DockerCompose -args @("run", "--rm", "cms-back-dev", "python", "manage.py", "makemigrations")
            }
            "showmigrations" {
                Invoke-DockerCompose -args @("run", "--rm", "cms-back-dev", "python", "manage.py", "showmigrations")
            }
            "migrate" {
                Invoke-DockerCompose -args @("run", "--rm", "cms-back-dev", "python", "manage.py", "migrate")
            }
            "stop|down" {
                Invoke-DockerCompose -args @("down")
            }
            default {
                Write-Host "No known command specified"
            }
        }
    }
    "cms-front" {
        Write-Host "Not implemented yet"
    }
    default {
        Write-Host "No known project specified"
    }
}

