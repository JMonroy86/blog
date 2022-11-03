from blog.user.domain.user_schema import UserRepo


class UserApplication:
    user_repo: UserRepo

    def __init__(self, user_repo_imp: UserRepo):
        self.user_repo = user_repo_imp

    async def create_an_user(self, user_data):
        if user_data.username == "":
            raise Exception("username doesn't have to be empty")
        if user_data.email == "":
            raise Exception("email doesn't have to be empty")
        if user_data.password == "":
            raise Exception("password doesn't have to be empty")

        email_data = await self.user_repo.get_user_by_email(user_data.email)
        if email_data:
            raise Exception("email already exist, please, choose another one")

        username = await self.user_repo.get_user_by_username(user_data.username)
        if username:
            raise Exception(
                "username already exist, please, choose another one")

        result = await self.user_repo.create_an_user(user_data)
        return result

    async def get_user_by_email(self, email):
        email_data = await self.user_repo.get_user_by_email(email)
        if email_data is None:
            raise Exception("Email address not found")
        return email_data

    async def get_user_by_username(self, username):
        email_data = await self.user_repo.get_user_by_username(username)
        if email_data is None:
            raise Exception("Username not found")
        return email_data
