# from typing import Optional
from typing import Protocol
from pydantic import BaseModel, EmailStr


# properties required during user creation
class UserDto(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool
    is_superuser: bool


class Users(UserDto):
    id: int


class UserRepo(Protocol):
    async def create_an_user(self, user_data: UserDto) -> Users:
        ...
