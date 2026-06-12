from fastapi import FastAPI
from src.api.routes import router
from src.config import settings


app = FastAPI(title=settings.app_name)
app.include_router(router)

@app.get("/")
async def home():
    return {"message": "This is the home endpoint!"}