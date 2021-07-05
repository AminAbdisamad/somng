from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.com",
                "password": "weakpassword",
            }
        }


class UserLoginSchema(BaseModel):
    # email: EmailStr = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {"email": "abdulazeez@x.com", "password": "weakpassword"}
        }
