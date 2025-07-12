from typing import Any

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

SessionFactoryType = async_sessionmaker[AsyncSession]


def create_sa_engine(url: str | URL, **kwargs: Any) -> AsyncEngine:
    return create_async_engine(url, **kwargs)


def create_sa_session_factory(engine: AsyncEngine) -> SessionFactoryType:
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
