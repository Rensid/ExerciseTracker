from fastapi import FastAPI
from app.routers import category_router, exercise_router, auth_router, user_router
from app.base.base import init_models
from contextlib import asynccontextmanager


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield


app.include_router(category_router)
app.include_router(exercise_router)
app.include_router(auth_router)
app.include_router(user_router)


@app.get('/')
async def root():
    return {"message": "Hi"}
