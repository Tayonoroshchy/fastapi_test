from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('db clear')
    await create_tables()
    print('db ready')
    yield
    print('close')


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

