from src.article_analyzer.domain.settings import MainSettings
from src.article_analyzer.presentation.api.settings import (
    CORSSettings,
    ServerSettings,
    )

class MainSettingsProvider:
    def _provide_server_settings(self) -> ServerSettings:
        return ServerSettings()
    
    def _provide_cors_settings(self) -> CORSSettings:
        return CORSSettings()

    def _provide_main_settings(
        self,
        server: ServerSettings,
        cors: CORSSettings
        ) -> MainSettings:
        return MainSettings(
            server=server,
            cors=cors
            )
    
    def load(self) -> MainSettings:
        return self._provide_main_settings(
            self._provide_server_settings(),
            self._provide_cors_settings()
        )
