from pydantic import BaseModel

# class STaskAdd(BaseModel):
#     name: str
#     description: str | None = None
#
#
# class STask(STaskAdd):
#     id: int

"""Контроллер класс"""


class ControllerAdd(BaseModel):
    S_N: int
    Name: str


class MeterAdd(BaseModel):
    Modbus_Address: int
    Name: str
    Controller_S_N: int


class ParamAdd(BaseModel):
    Name: str
    Type: str
    Register: int
    Meter_Modbus_Address: int


class ValueAdd(BaseModel):
    Time: int
    Value: float
    Param_Register: int
    Param_Meter_Modbus_Address: int

