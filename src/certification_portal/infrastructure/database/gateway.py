from typing import Type

from .core import TransactionManager
from .repositories import UserRepository
from src.certification_portal.domain.common.interfaces import BaseGateway
from src.certification_portal.domain.database.repository import RepositoryType

class DBGateway(BaseGateway):
    __slots__ = ("manager",)

    def __init__(self, manager: TransactionManager) -> None:
        self.manager = manager
        super().__init__(manager)

    def _init_repo(self, cls: Type[RepositoryType]) -> RepositoryType:
        return cls(self.manager.session)
    
    def user(self) -> UserRepository:
        return self._init_repo(UserRepository)
