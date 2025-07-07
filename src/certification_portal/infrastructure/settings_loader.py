from typing import Optional

from src.certification_portal.presentation.api.settings import (
    CORSSettings,
    ServerSettings,
    MainSettings
    )
from src.certification_portal.presentation.api.v1.settings import (
    V1AppSettings, 
    V1Settings,
    get_root_dir_path
    )

def load_v1_settings(
    v1_app_settings: Optional[V1AppSettings] = None
    ) -> V1Settings:
    return V1Settings(
        root_dir=get_root_dir_path(),
        app=v1_app_settings or V1AppSettings()
    )


def load_main_settings(
    server_settings: Optional[ServerSettings] = None,
    cors_settings: Optional[CORSSettings] = None,
    ) -> MainSettings:
    return MainSettings(
        server=server_settings or ServerSettings(),
        cors=cors_settings or CORSSettings()
    )
