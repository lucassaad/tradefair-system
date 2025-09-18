from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.models.exhibitor import Exhibitor
from app.api.models.registry import table_registry
from app.api.models.tradefair import TradeFair


@table_registry.mapped_as_dataclass
class Booth:
    __tablename__ = "Booth"

    exhibitor: Mapped["Exhibitor"] = relationship("Exhibitor", init=False)
    tradefair: Mapped["TradeFair"] = relationship("TradeFair", init=False)

    exhibitor_id: Mapped[int] = mapped_column(ForeignKey(exhibitor.id), primary_key=True)
    tradefair_id: Mapped[int] = mapped_column(ForeignKey(tradefair.id), primary_key=True)
    booth_number: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())