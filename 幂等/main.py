from DBConnector import *
import random

connectDB = ConnectDatabase()
get_conf = connectDB.get_conf(db='wx')
conn, cur = connectDB.connect_db(get_conf["host"], get_conf["user"],
                     get_conf["password"], get_conf["database"], get_conf["port"])


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