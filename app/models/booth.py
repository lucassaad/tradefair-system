from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.exhibitor import Exhibitor
from app.models.registry import table_registry
from app.models.tradefair import TradeFair


@table_registry.mapped_as_dataclass
class Booth:
    __tablename__ = "Booth"

    exhibitor: Mapped["Exhibitor"] = relationship("Exhibitor", init=False)
    tradefair: Mapped["TradeFair"] = relationship("TradeFair", init=False)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    booth_number: Mapped[int] = mapped_column(Integer)
    exhibitor_id: Mapped[int] = mapped_column(ForeignKey(exhibitor.id))
    tradefair_id: Mapped[int] = mapped_column(ForeignKey(tradefair.id))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
