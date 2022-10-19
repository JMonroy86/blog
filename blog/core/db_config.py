import asyncpg
from blog.core.config import Settings


async def init_db():
    return await asyncpg.create_pool(
        Settings.DATABASE_URL,
        command_timeout=60,
        min_size=2,
        max_size=4
    )
