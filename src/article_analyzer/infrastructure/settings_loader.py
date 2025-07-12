from typing import Optional

from src.article_analyzer.presentation.api.settings import (
    CORSSettings,
    ServerSettings,
    MainSettings
    )


def load_main_settings(
    server_settings: Optional[ServerSettings] = None,
    cors_settings: Optional[CORSSettings] = None,
    ) -> MainSettings:
    return MainSettings(
        server=server_settings or ServerSettings(),
        cors=cors_settings or CORSSettings()
    )
