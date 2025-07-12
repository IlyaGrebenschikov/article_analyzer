from typing import Optional, Type, overload

from typing_extensions import Unpack

from .base import BaseRepository
from src.certification_portal.domain.database.exceptions import InvalidParamsError
from src.certification_portal.domain.user.types import (
    UserCreationType,
    UserIdentityType,
    UserIdType,
    UserLoginType
)
from src.certification_portal.domain.user.interfaces import (
    UserRepositoryInterface
    )
from src.certification_portal.infrastructure.database.models import UserModel

class UserRepository(BaseRepository[UserModel], UserRepositoryInterface):
    __slots__ = ()

    @property
    def model(self) -> Type[UserModel]:
        return UserModel

    async def create(self, **data: Unpack[UserCreationType]) -> Optional[UserModel]:
        return await self._crud.insert(**data)

    @overload
    async def get_one(self, **identity: Unpack[UserIdType]) -> Optional[UserModel]: ...
    @overload
    async def get_one(self, **identity: Unpack[UserLoginType]) -> Optional[UserModel]: ...
    @overload
    async def get_one(self, **identity: Unpack[UserIdentityType]) -> Optional[UserModel]: ...
    async def get_one(self, **identity) -> Optional[UserModel]:
        user_id = identity.get("id")
        login = identity.get("login")
        if not (user_id or login):
            raise InvalidParamsError("at least one identifier must be provided")

        if user_id:
            clause = self.model.id == user_id
        else:
            clause = self.model.login == login

        return await self._crud.select(clause)
