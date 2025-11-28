from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_as_dataclass,
    mapped_column,
    registry,
    relationship,
)

table_registry = registry()


@mapped_as_dataclass(table_registry)
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        init=False, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(254), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    products: Mapped[list['Product']] = relationship(
        init=False,
        cascade='all, delete-orphan',
        lazy='selectin'
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now()
    )


@mapped_as_dataclass(table_registry)
class Product:
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(
        init=False, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now()
    )

