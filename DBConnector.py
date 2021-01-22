import json
import pymysql
import logging

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt = '%a, %d %b %Y %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename = 'report.log',
    # 打开日志文件的方式
    filemode = 'w'
)


class ConnectDatabase:
    def __init__(self, db):
        conf = self.get_conf(db)
        self.host = conf['host']
        self.user = conf['user']
        self.password = conf['password']
        self.db = conf['database']
        self.port = conf['port']

    def get_conf(self, db):
        with open("dbConfig.json", "r", encoding="utf-8") as f:
            conf = json.load(f)
        return conf[db]

    def connect_db(self):
        conn = pymysql.connect(self.host, self.user, self.password, self.db, self.port, charset="utf8")  # 最好加上utf-8
        cur = conn.cursor()
        return conn, cur

    # 获取数据库 的表, 并存储到list中
    def getTabs(self, cur):
        sql = 'show tables'
        cur.execute(sql)
        res = cur.fetchall()
        saveTabs = []
        for tab in res:
            tab = tab[0]
            saveTabs.append(tab)
        # print(saveTabs)
        return saveTabs

    # 获取列
    def get_cols(self, table, cur):
        sql = 'desc ' + str(table) + ''
        cur.execute(sql)
        res = cur.fetchall()
        return res

    # 执行sql, 返回结果
    def get_res(self, cur, sql):
        cur.execute(sql)
        res = cur.fetchall()
        return res

    # 数据的提交
    def get_fetch(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    # 数据库关闭
    def disconnect_db(self, conn, cur):
        cur.close()
        conn.close()