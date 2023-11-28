from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Float, Column, Text, ForeignKey


Base = declarative_base()


class MyGoods(Base):
    __tablename__ = "my_goods"
    id = Column(Integer, nullable=False, primary_key=True)
    Good_name = Column(String(50))
    Price = Column(Float)
    Amount = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100))
    Age = Column(Integer)


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, nullable=False, primary_key=True)
    Description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))


if __name__ == "__tables.py__":
  from db import engine as engine
  Base.metadata.create_all(engine)
