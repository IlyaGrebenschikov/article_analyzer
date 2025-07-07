from typing import Optional

from src.certification_portal.presentation.api.settings import (
    ServerSettings,
    MainSettings
    )
from src.certification_portal.presentation.api.v1.settings import (
    V1Settings,
    get_root_dir_path
    )

def load_v1_settings(
    ) -> V1Settings:
    return V1Settings(
        root_dir=get_root_dir_path(),
    )
    

def load_main_settings(
    server_settings: Optional[ServerSettings] = None
    ) -> MainSettings:
    return MainSettings(
        server=server_settings or ServerSettings()
    )
