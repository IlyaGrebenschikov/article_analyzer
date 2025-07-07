from fastapi import FastAPI

from .healthcheck import healthcheck_router

def setup_v1_controllers(app: FastAPI) -> None:
    app.include_router(healthcheck_router)
