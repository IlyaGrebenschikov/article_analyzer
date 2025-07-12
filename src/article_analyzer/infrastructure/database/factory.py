from typing import Callable, Type

from .core import SessionFactoryType, TransactionManager
from .gateway import DBGateway

def create_database_factory(
    manager: Type[TransactionManager], session_factory: SessionFactoryType
) -> Callable[[], DBGateway]:
    def _create() -> DBGateway:
        return DBGateway(manager(session_factory()))

    return _create
