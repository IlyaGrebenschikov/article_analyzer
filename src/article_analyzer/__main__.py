from .presentation.api.servers import run_api_uvicorn
from .presentation.api.setup import init_main_app
from .presentation.api.v1.setup import init_v1_app
from .infrastructure.dependency_injection.providers import V1SettingsProvider
from .infrastructure.settings_loader import (
    load_main_settings
    )

def main() -> None:
    main_settings = load_main_settings()
    v1_settings = V1SettingsProvider().load()
    app = init_main_app(
        init_v1_app(v1_settings.app),
        settings=main_settings
    )
    
    run_api_uvicorn(app, main_settings.server)


if __name__ == "__main__":
    main()
