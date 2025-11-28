from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tradefair_system.database import get_session
from tradefair_system.models import User
from tradefair_system.schemas.token import Token
from tradefair_system.security import (
    create_access_token,
    get_current_user,
    verify_password,
)

router = APIRouter(prefix='/auth', tags=['auth'])

currentUser = Annotated[User, Depends(get_current_user)]
db_session = Annotated[AsyncSession, Depends(get_session)]
OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]


@router.post('/token', response_model=Token, status_code=HTTPStatus.OK)
async def login_for_access_token(
    form_data: OAuth2Form,
    session: db_session
):
    user = await session.scalar(
        select(User).where(User.email == form_data.username)
    )

    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Incorrect email or password',
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Incorrect email or password',
        )

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh_token', response_model=Token)
async def refresh_access_token(user: currentUser):
    new_access_token = create_access_token(
        data={'sub': user.email}
    )

    return {'access_token': new_access_token, 'token_type': 'bearer'}
