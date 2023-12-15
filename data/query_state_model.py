from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class QueryState(SqlAlchemyBase):
    __tablename__ = 'query_state'
    id = Column(Integer, autoincrement=True, primary_key=True)
    old_state_yellow = Column(Boolean)
    old_state_red = Column(Boolean)
    new_state_yellow = Column(Boolean)
    new_state_red = Column(Boolean)