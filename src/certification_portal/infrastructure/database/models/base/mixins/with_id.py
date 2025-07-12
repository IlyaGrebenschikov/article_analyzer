from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

class ModelWithIDMixin:
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
