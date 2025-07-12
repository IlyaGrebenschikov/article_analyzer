from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.article_analyzer.presentation.api.settings import CORSSettings

def setup_global_middlewares(app: FastAPI, settings: CORSSettings) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins,
        allow_credentials=True,
        allow_methods=settings.methods,
        allow_headers=settings.headers,
    )
