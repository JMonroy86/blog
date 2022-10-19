from fastapi import Depends
from blog.core.db_config import init_db


async def create_an_user(user_data, pool=Depends(init_db())):
    async with pool.acquire() as connection:
        async with connection.transaction():
            await connection.execute('''
          INSERT INTO users(username, email, password, is_active, is_superuser) VALUES($1, $2, $3, $4, $5)
      ''', user_data.username, user_data.email, user_data.password, user_data.is_active, user_data.is_superuser)

            return user_data


async def get_user_by_email(email, pool=Depends(init_db())):
    print(email, "holaa")
    async with pool.acquire() as connection:
        async with connection.transaction():
            return await connection.fetchrow(
                'SELECT * FROM users WHERE email = $1', email)
