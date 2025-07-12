import abc
from typing import Generic, Type

from sqlalchemy.ext.asyncio import AsyncSession

from .crud import CRUDRepository
from src.article_analyzer.infrastructure.database.models.base import ModelType
from src.article_analyzer.domain.database.repository import Repository


class BaseRepository(Repository, Generic[ModelType]):
    __slots__ = ("_session", "_crud")

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._crud = CRUDRepository(session, self.model)

    @property
    @abc.abstractmethod
    def model(self) -> Type[ModelType]:
        raise NotImplementedError
