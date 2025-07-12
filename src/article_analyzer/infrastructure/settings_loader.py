from typing import Optional
from pathlib import Path

from src.article_analyzer.domain.database.settings import DatabaseSettingsInterface
from src.article_analyzer.presentation.api.settings import (
    CORSSettings,
    ServerSettings,
    MainSettings
    )
from src.article_analyzer.presentation.api.v1.settings import (
    V1AppSettings, 
    V1Settings,
    )

def get_root_dir_path() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def load_v1_settings(
    database_settings: DatabaseSettingsInterface,
    v1_app_settings: Optional[V1AppSettings] = None,
    ) -> V1Settings:
    return V1Settings(
        root_dir=get_root_dir_path(),
        app=v1_app_settings or V1AppSettings(),
        database=database_settings
    )


def load_main_settings(
    server_settings: Optional[ServerSettings] = None,
    cors_settings: Optional[CORSSettings] = None,
    ) -> MainSettings:
    return MainSettings(
        server=server_settings or ServerSettings(),
        cors=cors_settings or CORSSettings()
    )
