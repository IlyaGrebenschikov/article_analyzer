from __future__ import annotations

from typing import (
    Any,
    Mapping,
    Optional,
    Sequence,
    Type,
    cast,
)

from sqlalchemy import (
    ColumnExpressionArgument,
    CursorResult,
    delete,
    exists,
    func,
    insert,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.article_analyzer.domain.database.crud import AbstractCRUDRepository
from src.article_analyzer.infrastructure.database.models.base import ModelType


class CRUDRepository(AbstractCRUDRepository[ModelType]):
    __slots__ = ("_session",)

    def __init__(self, session: AsyncSession, model: Type[ModelType]) -> None:
        super().__init__(model)
        self._session = session

    async def insert(self, **values: Any) -> Optional[ModelType]:
        stmt = insert(self.model).values(**values).returning(self.model)
        return (await self._session.execute(stmt)).scalars().first()

    async def insert_many(
        self, data: Sequence[Mapping[str, Any]]
    ) -> Sequence[ModelType]:
        stmt = insert(self.model).returning(self.model)
        result = await self._session.scalars(stmt, data)
        return result.all()

    async def select(
        self,
        *clauses: ColumnExpressionArgument[bool],
    ) -> Optional[ModelType]:
        stmt = select(self.model).where(*clauses)
        return (await self._session.execute(stmt)).scalars().first()

    async def select_many(
        self,
        *clauses: ColumnExpressionArgument[bool],
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Sequence[ModelType]:
        stmt = select(self.model).where(*clauses).offset(offset).limit(limit)
        return (await self._session.execute(stmt)).scalars().all()

    async def update(
        self, *clauses: ColumnExpressionArgument[bool], **values: Any
    ) -> Sequence[ModelType]:
        stmt = update(self.model).where(*clauses).values(**values).returning(self.model)
        return (await self._session.execute(stmt)).scalars().all()

    async def update_many(self, data: Sequence[Mapping[str, Any]]) -> CursorResult[Any]:
        return await self._session.execute(update(self.model), data)

    async def delete(
        self, *clauses: ColumnExpressionArgument[bool]
    ) -> Sequence[ModelType]:
        stmt = delete(self.model).where(*clauses).returning(self.model)
        return (await self._session.execute(stmt)).scalars().all()

    async def exists(self, *clauses: ColumnExpressionArgument[bool]) -> bool:
        stmt = exists(select(self.model).where(*clauses)).select()
        return cast(bool, await self._session.scalar(stmt))

    async def count(self, *clauses: ColumnExpressionArgument[bool]) -> int:
        stmt = select(func.count()).where(*clauses).select_from(self.model)
        return cast(int, await self._session.scalar(stmt))

    def with_query_model(self, model: Type[ModelType]) -> CRUDRepository[ModelType]:
        return CRUDRepository(self._session, model)
