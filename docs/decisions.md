# Decision Log

This file contains the main technical decisions I made during the project.

## ADR-001: Using FastAPI for the application

I used FastAPI because the project needed a small but clear HTTP API that could be tested, containerized, and deployed. It allowed me to create endpoints such as `/ping`, `/healthz`, `/version`, and `/metrics` with a simple structure. FastAPI also works well with `pytest` and `TestClient`. This helped me focus more on the DevOps pipeline instead of spending too much time on application complexity.

## ADR-002: Creating Kubernetes manifests first and then adding Helm

I first created plain Kubernetes manifests under the `k8s/` folder to understand the Deployment and Service structure clearly. After verifying that the application worked on Minikube, I added a Helm chart to make the deployment easier to manage and upgrade. This approach helped me understand what Helm generates instead of treating it as a black box. The final project keeps both the plain manifests and the Helm chart because they show the deployment evolution step by step.

## ADR-003: Using GitHub Actions, Trivy, and GHCR for the pipeline

I used GitHub Actions because the repository is already hosted on GitHub and it provides a simple way to automate testing, Docker image builds, security scanning, and image publishing. The workflow runs `pytest`, builds the Docker image, scans it with Trivy, and pushes the image to GitHub Container Registry. I used GHCR because it integrates well with GitHub Actions and can use `GITHUB_TOKEN` for authentication. Trivy was added to include a basic container security check in the pipeline.