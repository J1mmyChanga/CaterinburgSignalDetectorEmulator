from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class QueryState(SqlAlchemyBase):
    __tablename__ = 'query_state'
    id = Column(Integer, autoincrement=True, primary_key=True)
    state_yellow = Column(Boolean)
    state_red = Column(Boolean)
