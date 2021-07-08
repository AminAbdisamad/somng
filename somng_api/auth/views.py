from fastapi import APIRouter, Body, Depends

from .model import UserSchema, UserLoginSchema
from .services import signJWT, check_user
from .auth_bearer import JWTBearer

auth = APIRouter(prefix="/auth")

users = []


@auth.post("/create", tags=["Auth"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@auth.post("/login", tags=["Auth"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Wrong login details!"}


# protected
@auth.get("/protected/", tags=["Protected"], dependencies=[Depends(JWTBearer())])
def protected():
    return "I'm protected"
