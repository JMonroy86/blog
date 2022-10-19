# from typing import Optional
from pydantic import BaseModel, EmailStr


# properties required during user creation
class User_schema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDto(User_schema):
    def __init__(self, _id: int, user: User_schema) -> None:
        self.id = _id
        self.user = user
