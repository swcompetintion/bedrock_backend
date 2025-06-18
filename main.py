from fastapi import FastAPI
from core.config import settings
from auth.routes import router as auth_router
from auth.routes import router as todos_router


app = FastAPI()


api_prefix = settings.base_api_url


app.include_router(auth_router, prefix=f"{api_prefix}/auth")
app.include_router(todos_router, prefix=f"{api_prefix}/todos")
