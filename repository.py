from sqlalchemy import select

from database import new_session, ControllerTable, MeterTable, ParamTable, ValueTable
from schemas import ControllerAdd, MeterAdd, ParamAdd, ValueAdd


class ControllerRepository:
    @classmethod
    async def add_one(cls, data: ControllerAdd) -> int:
        async with new_session() as session:
            controller_dict = data.model_dump()
            print(controller_dict)
            controller = ControllerTable(**controller_dict)
            session.add(controller)
            await session.flush()
            await session.commit()
            return controller.S_N

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ControllerTable)
            result = await session.execute(query)
            controller_models = result.scalars().all()
            return controller_models


class MeterRepository:
    @classmethod
    async def add_one(cls, data: MeterAdd):
        async with new_session() as session:
            meter_dict = data.model_dump()
            print(meter_dict)
            meter = MeterTable(**meter_dict)
            session.add(meter)
            await session.flush()
            await session.commit()

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(MeterTable)
            result = await session.execute(query)
            meter_models = result.scalars().all()
            return meter_models


class ParamRepository:
    @classmethod
    async def add_one(cls, data: ParamAdd):
        async with new_session() as session:
            param_dict = data.model_dump()
            print(param_dict)
            param = ParamTable(**param_dict)
            session.add(param)
            await session.flush()
            await session.commit()

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ParamTable)
            result = await session.execute(query)
            param_models = result.scalars().all()
            return param_models


class ValueRepository:
    @classmethod
    async def add_one(cls, data: ValueAdd):
        async with new_session() as session:
            value_dict = data.model_dump()
            print(value_dict)
            value = ValueTable(**value_dict)
            session.add(value)
            await session.flush()
            await session.commit()

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ValueTable)
            result = await session.execute(query)
            value_models = result.scalars().all()
            return value_models
