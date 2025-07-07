from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class V1ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix='V1_API_',
        extra="ignore",
    )

    port: int = 8080
    host: str = "0.0.0.1"


class V1Settings(BaseSettings):
    root_dir: Path
    api: V1ApiSettings


def get_root_dir_path() -> Path:
    return Path(__file__).resolve().parent.parent.parent
