from fastapi import APIRouter, Body

from .model import PostSchema, UserSchema, UserLoginSchema
from .auth import signJWT

auth = APIRouter(prefix="/api/v1/auth")

users = []


@auth.post("/", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return signJWT(user.email)
