from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from tradefair_system.models.user import User
from tradefair_system.schemas.message import Message
from tradefair_system.schemas.user import UserIn, UserOut, UsersList

router = APIRouter()


database = []


@router.post('/users/', response_model=UserOut, status_code=HTTPStatus.CREATED)
def post_user(userIn: UserIn):
    user = User(
        name=userIn.name,
        phone_number=userIn.phone_number,
        email=userIn.email,
        password=userIn.password,
    )
    user.id = len(database)
    database.append(user)

    return user


@router.get('/users/', response_model=UsersList, status_code=HTTPStatus.OK)
def get_all_users():
    return {'users': database}


@router.put(
    '/users/{user_id}', response_model=UserOut, status_code=HTTPStatus.OK
)
def put_user_by_id(user_id: int, user_in: UserIn):
    if user_id > len(database) or user_id < 0:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user = User(**user_in.model_dump())
    user.id = user_id

    database[user.id] = user

    return user


@router.delete(
        '/users/{user_id}', response_model=Message, status_code=HTTPStatus.OK
    )
def delete_user_by_id(user_id: int):
    if user_id > len(database) or user_id < 0:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found'
        )

    del database[user_id]
    return {'message': 'User deleted'}
