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

