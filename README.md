# FastAPI DevOps Pipeline

[![CI](https://github.com/alperennozalp/fastapi-devops-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/alperennozalp/fastapi-devops-pipeline/actions/workflows/ci.yml)

## Project Overview

This repository demonstrates a DevOps pipeline for a FastAPI application.

The project focuses on building, testing, containerizing, scanning, monitoring, and deploying a Python-based HTTP API by using common DevOps tools and practices. It includes automated tests, Docker-based containerization, Kubernetes deployment manifests, a Helm chart, GitHub Actions CI/CD workflow, container image security scanning, and basic monitoring support.

The main goal is to show how a backend service can be prepared and managed through a DevOps workflow, starting from local development and continuing through containerization, Kubernetes deployment, Helm-based installation, automated CI/CD, security checks, and observability.

## Project Scope

This project includes:

- A FastAPI application with health, version, and ping endpoints
- Automated endpoint tests with pytest
- Dockerfile and .dockerignore configuration
- Docker image build and container run workflow
- Kubernetes Deployment and Service manifests
- Minikube-based local Kubernetes deployment
- Helm chart for installing and upgrading the application
- GitHub Actions CI/CD workflow
- Automated test execution in CI
- Docker image build steps in CI/CD
- Container image security scanning
- Basic monitoring or observability setup
- README documentation for local, Docker, Kubernetes, Helm, and CI/CD usage

## Tech Stack

- Python: Main programming language used for the FastAPI application.
- FastAPI: Used to create API endpoints such as `/ping`, `/healthz`, `/version`, and `/metrics`.
- Uvicorn: Used as the ASGI server for running the FastAPI application.
- pytest: Used for automated endpoint testing.
- FastAPI TestClient: Used to test API endpoints without manually starting the server.
- httpx: Used by the test client for HTTP-style requests during testing.
- prometheus-client: Used to expose application metrics in Prometheus format.
- Docker: Used to containerize the FastAPI application.
- Kubernetes: Used to run the application with Deployment and Service resources.
- Minikube: Used as the local Kubernetes environment.
- Helm: Used to package and manage Kubernetes manifests.
- GitHub Actions: Used for CI/CD automation.
- Trivy: Used for container image security scanning.
- GitHub Container Registry: Used to store and publish the Docker image.

## Project Structure

```text
fastapi-devops-pipeline/
├── app/
│   ├── __init__.py## Project Structure

```text
fastapi-devops-pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── helm/
│   └── fastapi-devops-pipeline/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           └── service.yaml
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── tests/
│   └── test_endpoints.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pytest.ini
├── README.md
└── requirements.txt
│   └── main.py
├── tests/
│   └── test_endpoints.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

### Folder and file explanations

`app/`: Contains the FastAPI application code.

`app/main.py`: Main application file. The API endpoints such as `/ping`, `/healthz`, `/version`, and `/metrics` are defined here.

`app/__init__.py`: Makes the `app` folder usable as a Python package.

`tests/`: Contains the test files.

`tests/test_endpoints.py`: Contains endpoint tests for `/ping`, `/healthz`, `/version`, and `/metrics`.

`.github/workflows/ci.yml`: GitHub Actions workflow file. It runs the tests, builds the Docker image, scans the image with Trivy, and pushes the image to GitHub Container Registry.

`Dockerfile`: Used to build the Docker image of the FastAPI application.

`.dockerignore`: Used to keep unnecessary files out of the Docker build context.

`k8s/`: Contains the basic Kubernetes manifest files.

`k8s/deployment.yaml`: Defines how the application runs as a Kubernetes Deployment.

`k8s/service.yaml`: Defines how the application is exposed through a Kubernetes Service.

`helm/`: Contains the Helm chart version of the Kubernetes setup.

`helm/fastapi-devops-pipeline/Chart.yaml`: Contains basic information about the Helm chart.

`helm/fastapi-devops-pipeline/values.yaml`: Contains values such as the image name, tag, pull policy, service type, ports, and health check settings.

`helm/fastapi-devops-pipeline/templates/deployment.yaml`: Helm template for the Deployment.

`helm/fastapi-devops-pipeline/templates/service.yaml`: Helm template for the Service.

`requirements.txt`: Lists the Python packages used in the project.

`pytest.ini`: Contains pytest configuration for running the tests correctly.

`.gitignore`: Lists files and folders that should not be added to Git.

`README.md`: Explains the project structure, setup steps, Docker usage, Kubernetes usage, Helm usage, CI/CD workflow, and monitoring endpoint.

## API Endpoints

The application has four GET endpoints.

- `GET /ping`  
  Used to check if the application is responding.  
  Example response: `{"message": "pong"}`

- `GET /healthz`  
  Used as a basic health check endpoint. This endpoint is also used by the Kubernetes liveness and readiness probes.  
  Example response: `{"status": "healthy"}`

- `GET /version`  
  Returns version and commit information. If environment variables are not provided, it returns default local values.  
  Example response: `{"version": "dev", "commit": "local"}`

- `GET /metrics`  
  Exposes basic application metrics in Prometheus format.  
  This endpoint includes the `app_requests_total` metric, which counts handled requests.  
  Example output includes: `app_requests_total`

  ## Local Setup

This project uses a Python virtual environment.

Create the virtual environment:

`py -m venv .venv`

Activate it on Windows PowerShell:

`.\.venv\Scripts\Activate.ps1`

Install the required packages:

`pip install -r requirements.txt`

If the terminal starts with `(.venv)`, the virtual environment is active.

## Running the Application

Start the application locally:

`uvicorn app.main:app --reload`

Then open these URLs in the browser:

`http://127.0.0.1:8000/ping`

`http://127.0.0.1:8000/healthz`

`http://127.0.0.1:8000/version`

`http://127.0.0.1:8000/metrics`

Stop the application with:

`Ctrl + C`

## Running Tests

Run the tests with:

`pytest`

Current expected result:

`4 passed`

## Docker

The application can be built and run as a Docker container.

Build the Docker image locally:

`docker build -t fastapi-devops-pipeline .`

Run the container:

`docker run -d --name fastapi-devops-app -p 8000:8000 fastapi-devops-pipeline`

Then test the endpoints in the browser:

`http://127.0.0.1:8000/ping`

`http://127.0.0.1:8000/healthz`

`http://127.0.0.1:8000/version`

`http://127.0.0.1:8000/metrics`

Check running containers:

`docker ps`

View container logs:

`docker logs fastapi-devops-app`

Stop the container:

`docker stop fastapi-devops-app`

Remove the stopped container:

`docker rm fastapi-devops-app`

In the CI/CD workflow, the Docker image is also built automatically and pushed to GitHub Container Registry:

`ghcr.io/alperennozalp/fastapi-devops-pipeline:latest`

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

`/metrics`

Some useful troubleshooting commands:

`kubectl describe pod <pod-name>`

`kubectl logs <pod-name>`

`kubectl describe service fastapi-devops-service`

`kubectl get pods --show-labels`

`kubectl get endpointslices -l kubernetes.io/service-name=fastapi-devops-service`

Note: The first Kubernetes test used the local Docker image loaded into Minikube. Later, the Helm deployment was updated to use the image published on GitHub Container Registry.

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

The Helm chart now uses the Docker image published to GitHub Container Registry:

`ghcr.io/alperennozalp/fastapi-devops-pipeline:latest`

In `values.yaml`, the image pull policy is set to `Always` so that Kubernetes pulls the latest image when a new Pod is created.

## CI/CD and GitHub Container Registry

This project uses GitHub Actions for the CI/CD workflow.

The workflow is defined in:

`.github/workflows/ci.yml`

Current pipeline steps:

- Check out the repository
- Set up Python 3.12
- Install Python dependencies
- Run tests with pytest
- Build the Docker image
- Scan the Docker image with Trivy
- Push the Docker image to GitHub Container Registry

The Docker image is published to GitHub Container Registry:

`ghcr.io/alperennozalp/fastapi-devops-pipeline:latest`

The Helm chart is also configured to use this image from GHCR:

`ghcr.io/alperennozalp/fastapi-devops-pipeline`

After changing the Helm values, the application can be updated with:

`helm upgrade fastapi-devops ./helm/fastapi-devops-pipeline`

I tested the updated deployment on Minikube and verified that the `/ping`, `/healthz`, and `/version` endpoints worked successfully.

## Monitoring

The application exposes a basic Prometheus-compatible metrics endpoint.

Metrics endpoint:

`/metrics`

The project uses the `prometheus-client` package to generate metrics in Prometheus format.

The application currently tracks total handled requests with the following metric:

`app_requests_total`

The `/metrics` endpoint was tested locally with pytest and also verified through the Kubernetes service on Minikube.

After the latest image was pushed to GitHub Container Registry, the Helm chart was upgraded and the application was tested through:

`/ping`

`/healthz`

`/version`

`/metrics`

Since the Helm chart uses the GHCR image with the `latest` tag, the image pull policy is set to:

`Always`

This ensures that Kubernetes pulls the latest image from GitHub Container Registry when a new Pod is created.