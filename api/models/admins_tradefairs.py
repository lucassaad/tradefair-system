from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.models.admin import Admin
from api.models.registry import table_registry
from api.models.tradefair import TradeFair


@table_registry.mapped_as_dataclass
class Admins_TradeFairs:
    __tablename__ = "Admins_TradeFairs"

    admin: Mapped["Admin"] = relationship("Admin")
    tradefair: Mapped["TradeFair"] = relationship("TradeFair")

    admin_id: Mapped[int] = mapped_column(ForeignKey(admin.id), primary_key=True)
    tradefair_id: Mapped[int] = mapped_column(ForeignKey(tradefair.id), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())