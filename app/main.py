import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/healthz")
def healthz():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {
        "version": os.getenv("APP_VERSION", "dev"),
        "commit": os.getenv("GIT_SHA", "local"),
    }


