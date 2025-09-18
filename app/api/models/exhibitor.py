from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.models.registry import table_registry
from app.api.models.user import User


@table_registry.mapped_as_dataclass
class Exhibitor:
    __tablename__ = "Exhibitor"

    user: Mapped["User"] = relationship("User", init=False)

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    contact_phone_number: Mapped[str] = mapped_column(String(20))
    contact_email: Mapped[str] = mapped_column(String(254))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), unique=True)
