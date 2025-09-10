from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.registry import table_registry
from app.models.role import Role
from app.models.user import User


@table_registry.mapped_as_dataclass
class Roles_Users:
    __tablename__ = "Roles_Users"

    role: Mapped["Role"] = relationship("Role")
    user: Mapped["User"] = relationship("User")

    role_id: Mapped[int] = mapped_column(ForeignKey(role.id), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(user.id), primary_key=True)