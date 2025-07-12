from typing import Any, Optional

from fastapi import FastAPI

from src.article_analyzer.domain.settings import V1Settings
from .controllers import setup_v1_controllers

def init_v1_app(
    settings: V1Settings,
    **kwargs: Any
) -> tuple[str, FastAPI, Optional[str]]:
    app = FastAPI(
        **settings.app.model_dump(),
        **kwargs
    )
    setup_v1_controllers(app)
    return ("/api/v1", app, None)
