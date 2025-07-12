from .main_provider import MainSettingsProvider
from .v1_provider import V1SettingsProvider
from src.article_analyzer.domain.settings import Settings

def load_settings_providers() -> Settings:
    return Settings(
        V1SettingsProvider().load(),
        MainSettingsProvider().load()
    )

__all__ = (
    "MainSettingsProvider",
    "V1SettingsProvider",
    "load_settings_providers"
)
