from starlette.config import Config

config = Config(".env")
APP_NAME = config("APP_NAME", default=None)
APP_DESCRIPTION = config("APP_DESCRIPTION", default=None)
APP_VERSION = config("APP_VERSION", default="1.0.0")
BASE_API_URL = config("BASE_API_URL", default="/api/v1")
SQLALCHEMY_DATABASE_URL_SQLITE = config("SQLALCHEMY_DATABASE_URL_SQLITE", default=None)
JWT_ALGORITHM = config("JWT_ALGORITHM", default=None)
JWT_SECRET = config("JWT_SECRET_KEY", default=None)
ACCESS_TOKEN_EXPIRE_SECONDS = config("ACCESS_TOKEN_EXPIRE_SECONDS", default=1800)


# from enum import Enum


# class Status(str, Enum):
#     closed = "Closed"
#     open = "Open"
#     in_active = "In-Active"


# print(Status.closed.value)
# for item in Status:
#     print(item.value)
