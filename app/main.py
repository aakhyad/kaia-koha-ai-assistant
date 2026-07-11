
from app.routes.health import router as health_router
from app.core.logging import logger, setup_logging
from fastapi import FastAPI

from app.core.settings import settings
setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)

app.include_router(health_router)

@app.on_event("startup")
async def startup():
    logger.info("KAIA started successfully")


@app.on_event("shutdown")
async def shutdown():
    logger.info("KAIA stopped")

@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "Welcome to KAIA - Koha AI Assistant",
    }


