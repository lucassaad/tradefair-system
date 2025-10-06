from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from tradefair_system.database import get_session
from tradefair_system.models.user import User
from tradefair_system.schemas.message import Message
from tradefair_system.schemas.user import UserIn, UserOut, UsersList

router = APIRouter()


@router.post('/users/', response_model=UserOut, status_code=HTTPStatus.CREATED)
def post_user(user_in: UserIn, session: Session = Depends(get_session)):

    db_user = session.scalar(
        select(User).where((User.email == user_in.email))
    )

    if db_user is not None:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Email already exists'
        )

    db_user = User(**user_in.model_dump())
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
    user_id: int, user_in: UserIn, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where((User.id == user_id)))

    if db_user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    try:
        db_user.name = user_in.name
        db_user.email = user_in.email
        db_user.phone_number = user_in.phone_number
        db_user.password = user_in.password

        session.commit()
        session.refresh(db_user)

        return db_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Email already exists'
        )


@router.delete(
    '/users/{user_id}', response_model=Message, status_code=HTTPStatus.OK
)
def delete_user_by_id(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where((User.id == user_id)))

    if db_user is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}
