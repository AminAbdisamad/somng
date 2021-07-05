from fastapi import FastAPI
from config import APP_NAME, APP_DESCRIPTION, APP_VERSION
from database import Base, engine
from auth.views import auth

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)
app.include_router(auth)


@app.get("/", tags=["Index"])
def index() -> dict:
    return {"Name": APP_NAME, "Description": APP_DESCRIPTION, "Version": APP_VERSION}
