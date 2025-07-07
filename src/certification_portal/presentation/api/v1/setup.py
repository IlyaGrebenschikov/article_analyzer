from typing import Any, Optional

from fastapi import FastAPI

def init_v1_app(
    **kwargs: Any
) -> tuple[str, FastAPI, Optional[str]]:
    app = FastAPI(
        **kwargs
    )
    return ("/api/v1", app, None)
