from dataclasses import dataclass

from src.article_analyzer.presentation.api.settings import (
    CORSSettings,
     ServerSettings
     )

@dataclass
class MainSettings:
    server: ServerSettings
    cors: CORSSettings
