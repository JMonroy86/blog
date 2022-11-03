from typing import Optional
from typing import Protocol
from pydantic import BaseModel


# properties required during user creation
class UserDto(BaseModel):
    username: str
    password: str
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class Users(UserDto):
    id: int


class UserRepo(Protocol):
    async def create_an_user(self, user_data: UserDto) -> Users:
        ...

    async def get_user_by_email(self, email: str) -> Users:
        ...

    async def get_user_by_username(self, username: str) -> Users:
        ...
