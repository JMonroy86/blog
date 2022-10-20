
from blog.user.infrastructure.user_repository import UserRepoImpl


class UserIntegration:
    user_repo: UserRepoImpl

    def __init__(self, user_repo_imp: UserRepoImpl):
        self.user_repo = user_repo_imp

    async def create_an_user(self, user_data):
        print(user_data.username)
        if user_data.username == "":
            raise ValueError("username doesnt have to be empty")
        if user_data.email is None:
            raise ValueError("email doesnt have to be empty")
        if user_data.password is None:
            raise ValueError("password doesnt have to be empty")
        if user_data.is_active is None:
            raise ValueError("is_active doesnt have to be empty")
        if user_data.is_superuser is None:
            raise ValueError("is_superuser doesnt have to be empty")

        email_data = await self.user_repo.get_user_by_email(user_data.email)
        print(email_data)
        if email_data:
            raise Exception("email already exist, choose another one, please")

        username = await self.user_repo.get_user_by_username(user_data.username)
        if username:
            raise Exception(
                "username already exist, choose another one, please")

        result = await self.user_repo.create_an_user(user_data)
        return result
