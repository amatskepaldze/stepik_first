import sqlalchemy
from sqlalchemy.orm import sessionmaker

import tables

engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/poll_app")
session = sessionmaker(bind=engine)

connection = session()
# res = connection.execute(sqlalchemy.text("SELECT * from Users"))
# print(res.fetchall())

new_good = tables.MyGoods()
new_good.Good_name = "apple"
new_good.Price = 12.5
new_good.Amount = 1
connection.add(new_good)
connection.commit()

goods = connection.query(tables.MyGoods).all()
print(goods)