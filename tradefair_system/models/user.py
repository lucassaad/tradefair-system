from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from tradefair_system.models.product import Product
from tradefair_system.models.registry import table_registry


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        init=False, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(254), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now()
    )

    products: Mapped[list['Product']] = relationship(
        init=False,
        cascade='all, delete-orphan',
        lazy='selectin'
    )
