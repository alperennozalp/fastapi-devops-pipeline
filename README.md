# FastAPI DevOps Pipeline

## Project Overview

This repository contains a small HTTP service built.

The goal of the project is not to build a complex application, but to create a simple service that can later be containerized, tested, deployed, monitored, and documented as part of a DevOps workflow.

## Current Scope

The current version includes the initial application foundation:

- A small FastAPI application
- Three HTTP endpoints: /ping, /healthz, and /version
- Basic automated endpoint tests with pytest
- A project-specific Python virtual environment setup
- Initial Git repository structure with a feature branch workflow

The next steps will focus on containerization with Docker, Kubernetes deployment with Helm, CI/CD automation, and observability.

## Tech Stack

### Implemented so far

- Python: Used as the main programming language for the small HTTP service.
- FastAPI: Used to create the API endpoints.
- Uvicorn: Used to run the FastAPI application locally.
- pytest: Used to run automated tests.
- FastAPI TestClient: Used to test the endpoints without manually starting the server.
- httpx: Required by the test client for HTTP-style requests during testing.

## Project Structure

```text
fastapi-devops-pipeline/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_endpoints.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

### Folder and file explanations
app/: Contains the application source code.
app/main.py: Defines the FastAPI application and API endpoints.
app/__init__.py: Makes the app folder importable in Python.
tests/: Contains automated tests.
tests/test_endpoints.py: Contains tests for /ping, /healthz, and /version.
requirements.txt: Lists the Python packages needed for the project.
pytest.ini: Configures pytest to find the application code during tests.
.gitignore: Defines files and folders that Git should ignore.
README.md: Documents the project and how to use it.

## API Endpoints

The service currently has three simple GET endpoints.

- GET /ping  
  Used to check if the application is responding.  
  Example response: {"message": "pong"}

- GET /healthz  
  Used as a basic health check endpoint.
  Example response: {"status": "healthy"}

- GET /version  
  Returns version and commit information. For now, it returns default local values. Later, these values can be provided through environment variables in the deployment or CI/CD process.  
  Example response: {"version": "dev", "commit": "local"}

  ## Local Setup

This project uses a virtual environment.

Create it:

`py -m venv .venv`

Activate it on Windows PowerShell:

`.\.venv\Scripts\Activate.ps1`

Install the packages:

`pip install -r requirements.txt`

If the terminal starts with `(.venv)`, the virtual environment is active.

## Running the Application

Start the app:

`uvicorn app.main:app --reload`

Open these URLs in the browser:

`http://127.0.0.1:8000/ping`

`http://127.0.0.1:8000/healthz`

`http://127.0.0.1:8000/version`

Stop the app with `Ctrl + C`.

## Running Tests

Run the tests:

`pytest`

Current expected result:

`3 passed`

## Docker

Build the Docker image:

`docker build -t fastapi-devops-pipeline .`

Run the container:

`docker run -d --name fastapi-devops-app -p 8000:8000 fastapi-devops-pipeline`

Check running containers:

`docker ps`

View container logs:

`docker logs fastapi-devops-app`

Stop the container:

`docker stop fastapi-devops-app`

Remove the stopped container:

`docker rm fastapi-devops-app`

## Kubernetes with Minikube

This project can also run on a local Kubernetes cluster with Minikube.

Start Minikube:

`minikube start --driver=docker`

Load the local Docker image into Minikube:

`minikube image load fastapi-devops-pipeline:latest`

Apply the Kubernetes Deployment:

`kubectl apply -f k8s/deployment.yaml`

Apply the Kubernetes Service:

`kubectl apply -f k8s/service.yaml`

Check the created resources:

`kubectl get deployments`

`kubectl get pods`

`kubectl get services`

Get the service URL:

`minikube service fastapi-devops-service --url`

Then open the returned URL in the browser with these paths:

`/ping`

`/healthz`

`/version`

Some useful troubleshooting commands:

`kubectl describe pod <pod-name>`

`kubectl logs <pod-name>`

`kubectl describe service fastapi-devops-service`

`kubectl get pods --show-labels`

`kubectl get endpointslices -l kubernetes.io/service-name=fastapi-devops-service`

## Helm

I also added a simple Helm chart for this project.

The chart is located here:

`helm/fastapi-devops-pipeline`

Before installing it, I can check the chart with:

`helm lint ./helm/fastapi-devops-pipeline`

I can also see what Kubernetes YAML files Helm will generate:

`helm template fastapi-devops ./helm/fastapi-devops-pipeline`

Install the chart:

`helm install fastapi-devops ./helm/fastapi-devops-pipeline`

Check the installed release:

`helm list`

If I change something in `values.yaml`, I can apply the change with:

`helm upgrade fastapi-devops ./helm/fastapi-devops-pipeline`

For now, `values.yaml` includes basic settings such as replica count, image information, service type, ports, and the health check path.
