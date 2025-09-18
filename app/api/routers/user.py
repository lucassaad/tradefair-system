from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.api.connection import Session, get_session
from app.api.models.user import User
from app.api.schemas.user import UserIn, UserOut

user_table = {}

router = APIRouter(tags=["User"])


@router.post("/api/v1/user", status_code=HTTPStatus.CREATED, response_model=UserOut)
def create_user(user_in: UserIn, session: Session = Depends(get_session)):
    user = User(
        name=user_in.name,
        phone_number=user_in.phone_number,
        email=user_in.email,
        password=user_in.password,
        created_at=datetime.now(),
    )
    # temporary - local database
    id = len(user_table) + 1
    user.id = id
    user_table[id] = user
    return user
