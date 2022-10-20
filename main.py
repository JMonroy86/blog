from fastapi import FastAPI
import uvicorn
from blog.core.config import Settings
from blog.core.db_config import init_db
from blog.apis.v1.base import api_router
from blog.core.api_dependencies import api_dependencies

app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)


def include_router():
    app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    db = await init_db()
    if db is None:
        raise Exception("error db es none")
    include_router()
    api_dependencies(app=app, pool=db)


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
