from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from .ioc import V1AdaptersProvider
from src.article_analyzer.presentation.api.v1.settings import V1Settings

def v1_setup_dependencies(
    app: FastAPI,
    v1_settings: V1Settings,
    ) -> None:
    v1_adapters_provider = V1AdaptersProvider(v1_settings)
    container = make_async_container(v1_adapters_provider)
    
    setup_dishka(container=container, app=app)
