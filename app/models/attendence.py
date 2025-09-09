from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.client import Client
from app.models.registry import table_registry
from app.models.tradefair import TradeFair


@table_registry.mapped_as_dataclass
class Attendance:
    __tablename__ = "Attendance"

    client: Mapped["Client"] = relationship("Client")
    tradefair: Mapped["TradeFair"] = relationship("TradeFair")

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    status: Mapped[str] = mapped_column(String(100))
    client_id: Mapped[int] = mapped_column(ForeignKey(client.id))
    trade_id: Mapped[int] = mapped_column(ForeignKey(tradefair.id))
    registration_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())