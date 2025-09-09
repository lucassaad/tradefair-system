from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.exhibitor import Exhibitor
from app.models.registry import table_registry


@table_registry.mapped_as_dataclass
class Product:
    __tablename__ = "Product"

    exhibitor: Mapped["Exhibitor"] = relationship("Exhibitor", init=False)

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(100))
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    exhibitor_id: Mapped[int] = mapped_column(ForeignKey(exhibitor.id))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
