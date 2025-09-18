from pydantic import BaseModel, Field

from app.api.schemas.user import UserOut


class ExhibitorBase(BaseModel):
    contact_phone_number: str = Field(..., description="Exhibitor's contact phone number")
    contact_email: str = Field(..., description="Exhibitor's contact email")


class ExhibitorIn(ExhibitorBase):
    pass


class ExhibitorOut(ExhibitorBase):
    id: int = Field(..., description="UExhibitor ID")
    user: UserOut = Field(..., description="")


class ExhibitorUpdate(BaseModel):
    contact_phone_number: str | None = Field(None, description="Exhibitor's updated contact phone number")
    contact_email: str | None = Field(None, description="Exhibitor's updated contact email")
