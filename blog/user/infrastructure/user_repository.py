from asyncpg import Pool
from blog.user.domain.user_schema import Users, UserDto, UserRepo


class UserRepoImpl(UserRepo):
    _connection: Pool

    def __init__(self, pool: Pool):
        self._connection = pool

    async def create_an_user(self, user_data: UserDto) -> Users:

        async with self._connection.acquire() as connection:
            result = await connection.fetchval('''
                                        INSERT INTO users(username,
                                        email, password, is_active,
                                        is_superuser) VALUES($1, $2, $3, $4, $5) RETURNING id''',
                                               user_data.username,
                                               user_data.email,
                                               user_data.password,
                                               user_data.is_active,
                                               user_data.is_superuser)

            user_created = Users(
                username=user_data.username,
                email=user_data.email,
                password=user_data.password,
                is_active=user_data.is_active,
                is_superuser=user_data.is_superuser,
                id=result
            )
            return user_created

    async def get_user_by_email(self, email) -> Users:
        print(email)
        async with self._connection.acquire() as connection:
            return await connection.fetchrow(
                'SELECT * FROM users WHERE email = $1', email)

    async def get_user_by_username(self, username) -> Users:
        async with self._connection.acquire() as connection:
            return await connection.fetchrow(
                'SELECT * FROM users WHERE username = $1', username)
