from fastapi import APIRouter
# from fastapi import  HTTPException, status
from blog.user.domain import user_schema
from blog.user.infrastructure.user_repository import create_an_user

router = APIRouter()


@router.post("/")
async def user_signup(user: user_schema.UserDto):
    email = await create_an_user(user)

    data = user
    data["is_active"] = True
    data["is_superuser"] = True
    return data
