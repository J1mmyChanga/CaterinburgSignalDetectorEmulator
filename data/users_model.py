from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase
from .offices_model import Offices


class Users(SqlAlchemyBase):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    state_yellow = Column(Boolean)
    office = Column(Integer, ForeignKey('offices.id'))

    offices = relationship(Offices, backref='users')