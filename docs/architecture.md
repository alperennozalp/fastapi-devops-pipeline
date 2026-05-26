# Architecture Diagram

This file shows the basic project flow.

```mermaid
flowchart LR
    Developer["Developer"] --> GitHub["GitHub Repository"]
    GitHub --> Actions["GitHub Actions CI/CD"]

    Actions --> Tests["Run Tests"]
    Actions --> Build["Build Docker Image"]
    Actions --> Scan["Trivy Scan"]
    Actions --> GHCR["Push to GHCR"]

    GHCR --> Helm["Helm Chart"]
    Helm --> Kubernetes["Kubernetes / Minikube"]

    Kubernetes --> Pod["FastAPI Pod"]
    Pod --> Endpoints["API Endpoints"]

    Endpoints --> Ping["/ping"]
    Endpoints --> Health["/healthz"]
    Endpoints --> Version["/version"]
    Endpoints --> Metrics["/metrics"]
 