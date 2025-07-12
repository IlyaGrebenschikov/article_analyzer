from typing import Optional, Any

from fastapi import FastAPI

from .middlewares import setup_global_middlewares
from src.article_analyzer.domain.settings import MainSettings

def init_main_app(
    *sub_apps: tuple[str, FastAPI, Optional[str]],
    settings: MainSettings,
    **kwargs: Any
) -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        swagger_ui_oauth2_redirect_url=None,
        **kwargs
    )
    for apps in sub_apps:
        app.mount(*apps)
        
    setup_global_middlewares(app, settings.cors)    
         
    return app
