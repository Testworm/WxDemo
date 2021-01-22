from DBConnector import *
import random

connectDB = ConnectDatabase('wx')
conn, cur = connectDB.connect_db()


def demo():
    sql = 'select * from `order`'
    res = connectDB.get_res(cur, sql)
    print(res)


def insert():
    sql = "insert into `order`(orderId, payAmount) value('12', '200')"
    res = connectDB.get_fetch(conn, cur, sql)
    print(res)


if __name__ == '__main__':
    demo()
    insert()