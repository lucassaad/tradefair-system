from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.admin import Admin
from app.models.registry import table_registry
from app.models.tradefair import TradeFair


@table_registry.mapped_as_dataclass
class Admins_TradeFairs:
    __tablename__ = "Admins_TradeFairs"

    admin: Mapped["Admin"] = relationship("Admin")
    tradefair: Mapped["TradeFair"] = relationship("TradeFair")

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    admin_id: Mapped[int] = mapped_column(ForeignKey(admin.id))
    tradefair_id: Mapped[int] = mapped_column(ForeignKey(tradefair.id))