from unittest.mock import AsyncMock
import pytest
from pydantic import EmailStr
from blog.user.application.user import UserApplication, UserRepo
from blog.user.domain.user_schema import UserDto, Users


class FakeUserRepoImpl(UserRepo):
    async def create_an_user(self, user_data: UserDto) -> Users:
        raise Exception(
            "error missing mock implementation in FakeUserRepoImpl create_an_user")

    async def get_user_by_email(self, email: str) -> Users:
        raise Exception(
            "error missing mock implementation in FakeUserRepoImpl get_user_by_email")

    async def get_user_by_username(self, username: str) -> Users:
        raise Exception(
            "error missing mock implementation in FakeUserRepoImpl get_user_by_username")


@pytest.mark.asyncio
class Test_users_application:
    expected = {
        "username": "string",
        "password": "string",
        "email": "user@example.com",
        "is_active": True,
        "is_superuser": True,
        "id": 1
    }

    user = Users(
        id=expected["id"],
        username=expected["username"],
        password=expected["password"],
        email=expected["email"],
        is_active=expected["is_active"],
        is_superuser=expected["is_superuser"]
    )

    async def test_create_an_user(self):
        user_data = {"username": "string",
                     "email": "user@example.com", "password": "psw"}

        user_dto = UserDto(username=user_data["username"],
                           password=user_data["password"],
                           email=EmailStr(user_data["email"]))

        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_email = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_username = AsyncMock(return_value=None)
        user_repo_imp.create_an_user = AsyncMock(return_value=self.user)
        user_instance = UserApplication(user_repo_imp)
        user_created = await user_instance.create_an_user(user_dto)
        assert self.expected == user_created

    async def test_get_an_error_sending_empty_username_in_create_an_user(self):
        user_data = {"username": "",
                     "email": "user@example.com", "password": "psw"}

        user_dto = UserDto(username=user_data["username"],
                           password=user_data["password"],
                           email=EmailStr(user_data["email"]))

        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.create_an_user = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_email = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_username = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.create_an_user(user_dto)
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "username doesn't have to be empty"

    async def test_get_an_error_sending_empty_email_in_create_an_user(self):
        user_data = {"username": "string",
                     "email": "", "password": "psw"}

        user_dto = UserDto(username=user_data["username"],
                           password=user_data["password"],
                           email=EmailStr(user_data["email"]))

        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.create_an_user = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_email = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_username = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.create_an_user(user_dto)
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "email doesn't have to be empty"

    async def test_get_an_error_sending_empty_password_in_create_an_user(self):
        user_data = {"username": "string",
                     "email": "user@example.com", "password": ""}

        user_dto = UserDto(username=user_data["username"],
                           password=user_data["password"],
                           email=EmailStr(user_data["email"]))

        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.create_an_user = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_email = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_username = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.create_an_user(user_dto)
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "password doesn't have to be empty"

    async def test_get_an_error_sending_an_existing_email_in_create_an_user(self):
        user_data = {"username": "string",
                     "email": "user@example.com", "password": "psw"}

        user_dto = UserDto(username=user_data["username"],
                           password=user_data["password"],
                           email=EmailStr(user_data["email"]))

        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_email = AsyncMock(return_value=self.user)
        user_repo_imp.get_user_by_username = AsyncMock(return_value=None)
        user_repo_imp.create_an_user = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.create_an_user(user_dto)
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "email already exist, please, choose another one"

    async def test_get_an_error_sending_an_existing_username_in_create_an_user(self):
        user_data = {"username": "string",
                     "email": "user@example.com", "password": "psw"}

        user_dto = UserDto(username=user_data["username"],
                           password=user_data["password"],
                           email=EmailStr(user_data["email"]))

        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_email = AsyncMock(return_value=None)
        user_repo_imp.get_user_by_username = AsyncMock(return_value=self.user)
        user_repo_imp.create_an_user = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.create_an_user(user_dto)
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "username already exist, please, choose another one"

    async def test_get_user_by_email(self):
        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_email = AsyncMock(return_value=self.user)
        user_instance = UserApplication(user_repo_imp)
        finded_user = await user_instance.get_user_by_email(self.expected["email"])
        assert finded_user == self.expected

    async def test_get_a_message_error_sending_email_address_that_doesnt_exist_in_get_user_by_email(self):
        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_email = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.get_user_by_email("notexistingemail@testemail.com")
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "Email address not found"

    async def test_get_user_by_username(self):
        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_username = AsyncMock(return_value=self.user)
        user_instance = UserApplication(user_repo_imp)
        finded_user = await user_instance.get_user_by_username(self.expected["username"])
        assert finded_user == self.expected

    async def test_get_a_message_error_sending_username_that_doesnt_exist_in_get_user_by_username(self):
        user_repo_imp = FakeUserRepoImpl()
        user_repo_imp.get_user_by_username = AsyncMock(return_value=None)
        user_instance = UserApplication(user_repo_imp)
        with pytest.raises(Exception) as exc_info:
            await user_instance.get_user_by_username("thisUsernameDoesntExist")
        assert exc_info.type is Exception
        assert exc_info.value.args[0] == "Username not found"
