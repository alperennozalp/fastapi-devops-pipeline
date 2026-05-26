# Runbook

This file contains basic operational commands for the project.

## Check the application locally

Start the application:

`uvicorn app.main:app --reload`

Test the endpoints:

`http://127.0.0.1:8000/ping`

`http://127.0.0.1:8000/healthz`

`http://127.0.0.1:8000/version`

`http://127.0.0.1:8000/metrics`

Stop the application with:

`Ctrl + C`

## Run tests

Run all tests:

`pytest`

Expected result:

`4 passed`

## Check Kubernetes resources

Check deployments:

`kubectl get deployments`

Check pods:

`kubectl get pods`

Check services:

`kubectl get services`

Check EndpointSlices:

`kubectl get endpointslices -l kubernetes.io/service-name=fastapi-devops-service`

## Access the application on Minikube

Get the service URL:

`minikube service fastapi-devops-service --url`

Then test the endpoints by adding these paths to the returned URL:

`/ping`

`/healthz`

`/version`

`/metrics`

## View application logs

First get the Pod name:

`kubectl get pods`

Then check logs:

`kubectl logs <pod-name>`

## Describe a Pod

Use this when a Pod is not starting or is stuck:

`kubectl describe pod <pod-name>`

## Restart the deployment

Restart the application deployment:

`kubectl rollout restart deployment fastapi-devops-app`

Check rollout status:

`kubectl rollout status deployment fastapi-devops-app`

## Helm operations

List Helm releases:

`helm list`

Install the chart:

`helm install fastapi-devops ./helm/fastapi-devops-pipeline`

Upgrade the release:

`helm upgrade fastapi-devops ./helm/fastapi-devops-pipeline`

Check Helm history:

`helm history fastapi-devops`

Rollback to a previous revision:

`helm rollback fastapi-devops <revision-number>`

## Common issue: /metrics returns Not Found

If `/metrics` returns:

`{"detail":"Not Found"}`

the application may still be running an older Docker image.

In this project, the Helm chart uses the GHCR image with:

`pullPolicy: Always`

After checking the image settings, run:

`helm upgrade fastapi-devops ./helm/fastapi-devops-pipeline`

Then check the Pod again:

`kubectl get pods`