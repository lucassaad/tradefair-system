from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.api.models.registry import table_registry


@table_registry.mapped_as_dataclass
class Role:
    __tablename__: "Role"

    id: Mapped[int] = mapped_column(init=False, primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(String(100), unique=True)