from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='POSTGRES_',
        extra='ignore'
    )
    drivername: str = 'postgresql+asyncpg'
    host: str
    port: int
    username: str
    password: str
    database: str
    
    @property
    def url_obj(self) -> URL:
        return URL.create(
            **self.model_dump()
        )

    @property
    def url_str(self) -> str:
        return (
            f'postgresql+asyncpg://'
            f'{self.username}:'
            f'{self.password}@'
            f'{self.host}:'
            f'{self.port}/'
            f'{self.database}'
        )
