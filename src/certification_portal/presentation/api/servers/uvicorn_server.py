from typing import Any

import uvicorn
from fastapi import FastAPI

from src.certification_portal.presentation.api.settings import ServerSettings

def run_api_uvicorn(
    app: FastAPI,
    settings: ServerSettings,
    **kwargs: Any
    ) -> None:
    uvicorn.run(app, **settings.model_dump(), **kwargs)
