from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.auth import authenticate_user, get_current_user
from app.auth.jwt import get_new_tokens
from app.base.base import get_async_session
from app.crud.user_crud import create_new_user
from app.models.user_model import User
from app.schemas.user_schema import Token, UserPasswordSchema


auth_router = APIRouter()


@auth_router.post('/registration')
async def register_new_user(user_data: UserPasswordSchema,
                            session: AsyncSession = Depends(get_async_session)):
    user = await create_new_user(session, user_data)
    tokens = await get_new_tokens(user)
    return tokens


@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                session: AsyncSession = Depends(get_async_session)) -> Token:
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    tokens = await get_new_tokens(user)
    return Token(**tokens)


@auth_router.get('/users/get_me/')
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
