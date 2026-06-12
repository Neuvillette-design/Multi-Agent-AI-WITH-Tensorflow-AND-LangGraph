from fastapi import FastAPI
from src.api.routes import router
from src.config import settings
from src.utils.logging import setup_logging

logger = setup_logging()

app = FastAPI(title=settings.app_name)
app.include_router(router)

@app.get("/")
async def home():
    return {"message": "This is the home endpoint!"}

@app.on_event("startup")
async def startup_event():
    logger.info("Application started!")