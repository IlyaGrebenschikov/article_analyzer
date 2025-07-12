from .presentation.api.servers import run_api_uvicorn
from .presentation.api.setup import init_main_app
from .presentation.api.v1.setup import init_v1_app
from .infrastructure.dependency_injection.providers import load_settings_providers


def main() -> None:
    settings = load_settings_providers()
    app = init_main_app(
        init_v1_app(settings.v1),
        settings=settings.main
    )
    
    run_api_uvicorn(app, settings.main.server)


if __name__ == "__main__":
    main()
