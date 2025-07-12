from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.article_analyzer.domain.database.settings import DatabaseSettingsInterface

class V1AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="V1_APP_",
        extra="ignore",
    )
    title: Optional[str] = "FastAPI"
    version: Optional[str] = "0.1.0"
    docs_url: Optional[str] = "/docs"
    redoc_url: Optional[str] = "/redoc"


@dataclass
class V1Settings:
    root_dir: Path
    app: V1AppSettings
    database: DatabaseSettingsInterface
