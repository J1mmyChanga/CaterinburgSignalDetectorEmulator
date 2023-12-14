from sqlalchemy import Column, Integer, String
from .db_session import SqlAlchemyBase


class Offices(SqlAlchemyBase):
    __tablename__ = 'offices'
    id = Column(Integer, autoincrement=True, primary_key=True)
    address = Column(String)