from pathlib import Path

from pydantic_settings import BaseSettings

class V1Settings(BaseSettings):
    root_dir: Path


def get_root_dir_path() -> Path:
    return Path(__file__).resolve().parent.parent.parent
