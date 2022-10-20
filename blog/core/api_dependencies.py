from dataclasses import dataclass
from fastapi import FastAPI
from asyncpg import Pool
from blog.user.infrastructure.user_repository import UserRepoImpl


@dataclass
class Dependencies:
    user_repo: UserRepoImpl

    def __init__(self, user_repository_impl: UserRepoImpl):
        self.user_repo = user_repository_impl


def api_dependencies(app: FastAPI, pool: Pool):
    app.state.dep = Dependencies(user_repository_impl=UserRepoImpl(pool))
