from fastapi import FastAPI
import uvicorn
import config
from routes import routes

app = FastAPI(
    title=config.APP_NAME,
    description=config.APP_DESCRIPTION,
    version=config.APP_VERSION,
    openapi_url=f"{config.BASE_API_URL}/openapi.json",
    tags=["SomNOG"],
)

app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
