from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from tradefair_system.models.registry import table_registry


@table_registry.mapped_as_dataclass
class Product:
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(
        init=False, primary_key=True, autoincrement=True
    )
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    quantity: Mapped[int]
    created_at: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
