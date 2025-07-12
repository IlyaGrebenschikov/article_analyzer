from dataclasses import dataclass

from .main_settings import MainSettings
from .v1_settings import V1Settings

@dataclass
class Settings:
    v1: V1Settings
    main: MainSettings


__all__ = (
    "MainSettings",
    "Settings",
    "V1Settings",
)
