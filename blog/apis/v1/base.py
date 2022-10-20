from fastapi import APIRouter
from blog.apis.v1.infraestructure import users_infra


api_router = APIRouter()
api_router.include_router(users_infra.router, prefix="/users", tags=["users"])
