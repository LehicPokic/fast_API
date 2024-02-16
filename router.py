from typing import Annotated

from fastapi import APIRouter, Depends

from repository import ControllerRepository, MeterRepository, ParamRepository, ValueRepository
from schemas import ControllerAdd, MeterAdd, ParamAdd, ValueAdd

routerController = APIRouter(prefix="/controller")

routerMeter = APIRouter(prefix="/controller/meter")

routerParam = APIRouter(prefix="/controller/meter/param")

routerValue = APIRouter(prefix="/controller/meter/param/value")



@routerController.post("")
async def add_controller(schemas_controller: Annotated[ControllerAdd, Depends()]):
    await ControllerRepository.add_one(schemas_controller)
    return {"Ok": True}


@routerController.get("")
async def get_controller():
    controllers = await ControllerRepository.find_all()
    return {"data": controllers}


@routerMeter.post("")
async def add_meter(schemas_meter: Annotated[MeterAdd, Depends()]):
    meter = await MeterRepository.add_one(schemas_meter)
    return {"Ok": True}


@routerMeter.get("")
async def get_meter():
    meter = await MeterRepository.find_all()
    return {"data": meter}


@routerParam.post("")
async def add_param(schemas_param: Annotated[ParamAdd, Depends()]):
    param = await ParamRepository.add_one(schemas_param)
    return {"Ok": True}


@routerParam.get("")
async def get_param():
    param = await ParamRepository.find_all()
    return {"data": param}


@routerValue.post("")
async def add_param(schemas_value: Annotated[ValueAdd, Depends()]):
    value = await ValueRepository.add_one(schemas_value)
    return {"Ok": True}


@routerValue.get("")
async def get_param():
    value = await ValueRepository.find_all()
    return {"data": value}