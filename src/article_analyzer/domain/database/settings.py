from abc import abstractmethod
from typing import Protocol

from sqlalchemy import URL

class DatabaseSettingsInterface(Protocol):
    @property
    @abstractmethod
    def url_str(self) -> str: ...

    @property
    @abstractmethod
    def url_obj(self) -> URL: ...
