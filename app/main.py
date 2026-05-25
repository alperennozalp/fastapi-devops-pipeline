import os

from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests handled by the application",
)


@app.get("/ping")
def ping():
    REQUEST_COUNT.inc()
    return {"message": "pong"}


@app.get("/healthz")
def healthz():
    REQUEST_COUNT.inc()
    return {"status": "healthy"}


@app.get("/version")
def version():
    REQUEST_COUNT.inc()
    return {
        "version": os.getenv("APP_VERSION", "dev"),
        "commit": os.getenv("GIT_SHA", "local"),
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)