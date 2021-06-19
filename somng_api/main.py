from fastapi import FastAPI
import uvicorn
from config import APP_NAME, APP_DESCRIPTION, APP_VERSION

app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def index() -> dict:
    return {"Name": APP_NAME, "Description": APP_DESCRIPTION, "Version": APP_VERSION}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
