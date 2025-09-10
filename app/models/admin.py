from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.registry import table_registry
from app.models.user import User


@table_registry.mapped_as_dataclass
class Admin:
    __tablename__ = "Admin"

    user: Mapped["User"] = relationship("User", init=False)

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    contact_email: Mapped[str] = mapped_column(String(254), unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(user.id), unique=True)
    managed_tradefairs_count: Mapped[int] = mapped_column(Integer, default=0)