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

    client_id: Mapped[int] = mapped_column(ForeignKey(client.id), primary_key=True)
    trade_id: Mapped[int] = mapped_column(ForeignKey(tradefair.id), primary_key=True)
    status: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())