from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.registry import table_registry
from app.models.user import User


@table_registry.mapped_as_dataclass
class Client:
    __tablename__ = "Client"

    user: Mapped["User"] = relationship("User", init=False)

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(user.id), unique=True)
    attended_tradefairs: Mapped[int] = mapped_column(Integer, default=0)
