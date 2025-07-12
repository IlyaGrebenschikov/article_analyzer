from pydantic_settings import BaseSettings, SettingsConfigDict

class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix='SERVER_',
        extra="ignore",
    )
    port: int = 8080
    host: str = "0.0.0.0"
    

class CORSSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='CORS_',
        extra='ignore'
    )
    methods: list[str] = ["*"]
    headers: list[str] = ["*"]
    origins: list[str] = ["*"]


class MainSettings(BaseSettings):
    server: ServerSettings
    cors: CORSSettings
