from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(...)
    phone_number: str = Field(...)
    email: EmailStr = Field(...)


class UserIn(UserBase):
    password: str = Field(...)


class UserOut(UserBase):
    id: int = Field(...)
    created_at: datetime = Field(...)


class UsersList(BaseModel):
    users: list[UserOut]
