from abc import abstractmethod
from typing import Protocol


class UserRepositoryInterface(Protocol):
    @abstractmethod
    async def get_one(self): ...

    @abstractmethod
    async def create(self): ...
