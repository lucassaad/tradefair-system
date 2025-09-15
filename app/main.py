from fastapi import FastAPI
from app.routers import user

test = FastAPI()

test.include_router(user.router)