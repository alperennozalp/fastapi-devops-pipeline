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
