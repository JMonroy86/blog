from fastapi import FastAPI
import uvicorn
from blog.core.config import Settings
from blog.core.db_config import init_db
from blog.apis.v1.base import api_router

app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)


async def start_db():
    app.state.pool = await init_db()


def include_router():
    app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    include_router()
    await start_db()


def main():
    uvicorn.run(
        app="main:app",
        host='localhost',
        port=8000,
        reload=True,
        workers=1,
    )


if __name__ == '__main__':
    main()
