from typing import Any, Dict, TypeVar

from sqlalchemy.orm import DeclarativeBase


ModelType = TypeVar('ModelType', bound='Base')


class Base(DeclarativeBase):
    def as_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        for attr, value in self.__dict__.items():
            if attr.startswith("_"):
                continue
            if isinstance(value, Base):
                result[attr] = value.as_dict()
            elif isinstance(value, (list, tuple)):
                result[attr] = type(value)(
                    v.as_dict() if isinstance(v, Base) else v for v in value
                )
            else:
                result[attr] = value

        return result
