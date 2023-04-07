import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from apps import background, models
from apps.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='今天吃什么',
    description='“今天吃什么”后端接口文档',
    version='0.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        '*'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(background, prefix='/background', tags=['后台'])


if __name__ == '__main__':
    uvicorn.run('run:app', reload=True)