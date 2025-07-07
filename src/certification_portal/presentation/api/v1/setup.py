from typing import Any, Optional

from fastapi import FastAPI

from .settings import V1AppSettings

def init_v1_app(
    settings: V1AppSettings,
    **kwargs: Any
) -> tuple[str, FastAPI, Optional[str]]:
    app = FastAPI(
        **settings.model_dump(),
        **kwargs
    )
    return ("/api/v1", app, None)
