from sqlalchemy import ForeignKey, Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedColumn, relationship

engine = create_async_engine(
    "sqlite+aiosqlite:///1.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class ControllerTable(Model):
    __tablename__ = "Controller"
    S_N: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]

class MeterTable(Model):
    __tablename__ = "Meter"
    id: Mapped[int] = mapped_column(primary_key=True)
    Modbus_Address: Mapped[int]
    Name: Mapped[str]
    Controller_S_N = mapped_column(ForeignKey('Controller.S_N'))


class ParamTable(Model):
    __tablename__ = "Param"
    id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str]
    Type: Mapped[str]
    Register: Mapped[int]
    Meter_Modbus_Address = mapped_column(ForeignKey('Meter.Modbus_Address'))


class ValueTable(Model):
    __tablename__ = "Value"
    id: Mapped[int] = mapped_column(primary_key=True)
    Time: Mapped[int]
    Value: Mapped[float]
    Param_Register = mapped_column(ForeignKey('Param.Register'))
    Param_Meter_Modbus_Address = mapped_column(ForeignKey('Meter.Modbus_Address'))



async def create_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)



async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)
