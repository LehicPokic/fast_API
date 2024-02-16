from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import delete_tables, create_tables
from router import routerController, routerMeter, routerParam, routerValue

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    print("Выключение")



app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerController)

app.include_router(routerMeter)

app.include_router(routerParam)

app.include_router(routerValue)


    # S_N: int
    # Modbus_address: int
    # Name_meter: str
    # Name_param: str
    # time: int
    # value: float




# @app.get("/tasks")

# def get_tasks():
#     task = Task(S_N = 1, Modbus_address = 128, Name_meter = "Map3E",  Name_param = "IRMS", time = 55, value = 6.0)
#     return {"data": task}


