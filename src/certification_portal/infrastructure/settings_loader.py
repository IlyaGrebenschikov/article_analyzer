from typing import Optional

from src.certification_portal.presentation.api.v1.settings import (
    V1ApiSettings,
    V1Settings,
    get_root_dir_path
    )

def load_v1_settings(
    v1_api_settings: Optional[V1ApiSettings] = None
    ) -> V1Settings:
    return V1Settings(
        root_dir=get_root_dir_path(),
        api=v1_api_settings or V1ApiSettings()
    )
