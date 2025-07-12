from dataclasses import dataclass
from pathlib import Path

from src.article_analyzer.domain.database.settings import DatabaseSettingsInterface
from src.article_analyzer.presentation.api.v1.settings import V1AppSettings

@dataclass
class V1Settings:
    root_dir: Path
    app: V1AppSettings
    database: DatabaseSettingsInterface
