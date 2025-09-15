from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., description="User's name")
    phone_number: str = Field(..., description="User's phone number")
    email: str = Field(..., description="User's email")


class UserIn(UserBase):
    password: str = Field(..., description="User's password")


class UserOut(UserBase):
    id: int = Field(..., description="User ID")
    created_at: datetime = Field(..., description="Timestamp when the user was created")


class UserUpdate(BaseModel):
    name: str | None = Field(None, description="Updated user name")
    phone_number: str | None = Field(None, description="Updated user phone number")
    email: str | None = Field(None, description="Updated user email")
    password: str | None = Field(None, description="Updated user password")