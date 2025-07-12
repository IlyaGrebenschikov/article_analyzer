from pathlib import Path

from src.article_analyzer.presentation.api.v1.settings import V1AppSettings
from src.article_analyzer.domain.database.settings import DatabaseSettingsInterface
from src.article_analyzer.infrastructure.database.settings import PostgresSettings
from src.article_analyzer.presentation.api.v1.settings import V1Settings

class V1SettingsProvider:
    def _provide_root_dir_path(self) -> Path:
        return Path(__file__).resolve().parent.parent.parent
    
    def _provide_database_settings(self) -> DatabaseSettingsInterface:
        return PostgresSettings()
    
    def _provide_app_settings(self) -> V1AppSettings:
        return V1AppSettings()
    
    def _provide_v1_settings(
        self,
        root_dir: Path,
        app_settings: V1AppSettings,
        database_settings: DatabaseSettingsInterface
        ) -> V1Settings:
        return V1Settings(
            root_dir=root_dir,
            app=app_settings,
            database=database_settings
        )
    
    def load(self) -> V1Settings:
        return self._provide_v1_settings(
            self._provide_root_dir_path(),
            self._provide_app_settings(),
            self._provide_database_settings()
        )
