from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from tradefair_system.database import get_session
from tradefair_system.models.user import User
from tradefair_system.schemas.message import Message
from tradefair_system.schemas.user import UserIn, UserOut, UsersList
from tradefair_system.security import (
    get_current_user,
    get_password_hash,
)

router = APIRouter()


@router.post('/users/', response_model=UserOut, status_code=HTTPStatus.CREATED)
def post_user(user_in: UserIn, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where((User.email == user_in.email)))

    if db_user is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Email already exists'
        )

    hashed_password = get_password_hash(user_in.password)

    db_user = User(
        name=user_in.name,
        phone_number=user_in.phone_number,
        email=user_in.email,
        password=hashed_password,
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get('/users/', response_model=UsersList, status_code=HTTPStatus.OK)
def get_all_users(
    offset: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(offset).limit(limit)).all()

    return {'users': users}


@router.put(
    '/users/{user_id}', response_model=UserOut, status_code=HTTPStatus.OK
)
def put_user_by_id(
    user_id: int,
    user_in: UserIn,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    try:
        current_user.name = user_in.name
        current_user.email = user_in.email
        current_user.phone_number = user_in.phone_number
        current_user.password = get_password_hash(user_in.password)

        session.commit()
        session.refresh(current_user)

        return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Email already exists'
        )


@router.delete(
    '/users/{user_id}', response_model=Message, status_code=HTTPStatus.OK
)
def delete_user_by_id(
    user_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    session.delete(current_user)
    session.commit()

    return {'message': 'User deleted'}
