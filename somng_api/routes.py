from fastapi import APIRouter
from database import Base, engine
from auth.views import auth
from events.views import events
from workshops.views import workshops
from conferences.views import conferences
import config

# Create tables
Base.metadata.create_all(bind=engine)
# Registering API Routes

routes = APIRouter(prefix=config.BASE_API_URL)

routes.include_router(auth)
routes.include_router(events)
routes.include_router(workshops)
routes.include_router(conferences)


@routes.get("/", tags=["Index"])
def index() -> dict:
    return {
        "Name": config.APP_NAME,
        "Description": config.APP_DESCRIPTION,
        "Version": config.APP_VERSION,
    }
