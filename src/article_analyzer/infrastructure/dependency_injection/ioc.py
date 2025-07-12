from dishka.integrations.fastapi import FastapiProvider

from src.article_analyzer.presentation.api.v1.settings import V1Settings

class V1AdaptersProvider(FastapiProvider):
    def __init__(
        self,
        settings: V1Settings,
        scope = None,
        component = None,
        ) -> None:
        super().__init__(scope, component)
        self._settings = settings
    
    pass
