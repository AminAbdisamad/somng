import time
from typing import Dict, Any, Union
import jwt
from config import JWT_ALGORITHM, JWT_SECRET, ACCESS_TOKEN_EXPIRE_SECONDS
from .model import UserLoginSchema


def signJWT(user_id: str) -> Dict[str, str]:

    """Generates and returns JWT that expires in 1800 Seconds (30 Minutes)"""

    payload = {
        "user_id": user_id,
        "expires": time.time() + int(ACCESS_TOKEN_EXPIRE_SECONDS),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}


def decodeJWT(token: str) -> Union[dict, None]:
    """Returns a dictionary with a decoded JWT if token is VALID or None"""
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return None


def check_user(data: UserLoginSchema):
    # Will asume we've stored users in a database
    users: list = []

    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False
