from typing import Optional, Any

from fastapi import FastAPI

def init_main_app(
    *sub_apps: tuple[str, FastAPI, Optional[str]],
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
                
    return app
