from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import Index

from .base import Base
from .base.mixins import (
    ModelWithTimeMixin,
    ModelWithIDMixin
    )

class UserModel(ModelWithIDMixin, ModelWithTimeMixin, Base):
    login: Mapped[str] = mapped_column()
    password: Mapped[str]

    __tablename__ = 'user'
    __table_args__ = (
        Index("idx_lower_login", func.lower(login),unique=True),
        )
