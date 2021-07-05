from fastapi import FastAPI
from config import APP_NAME, APP_DESCRIPTION, APP_VERSION
from database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def index() -> dict:
    return {"Name": APP_NAME, "Description": APP_DESCRIPTION, "Version": APP_VERSION}
