import pymysql.cursors
import logging
logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s",level=logging.INFO)


config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'passwd' : '123456',
    'db' : 'test01',
    'charset' : 'utf8',
    'cursorclass' : pymysql.cursors.DictCursor
}

"""
connect = pymysql.connect(**config)
# 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
connect.autocommit(1)  # conn.autocommit(True)

# 使用cursor()方法获取操作游标
cursor = connect.cursor()
# 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。

try:
    # 创建数据库
    DB_NAME = 'test01'
    cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
    cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % DB_NAME)
    connect.select_db(DB_NAME)

    # 创建表
    TABLE_NAME = 'user'
    cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' % TABLE_NAME)

    # 批量插入纪录
    values = []
    for i in range(10):
        values.append((i, 'kk' + str(i)))
    cursor.executemany('INSERT INTO user values(%s,%s)', values)

    # 查询数据条目
    count = cursor.execute('SELECT * FROM %s' % TABLE_NAME)
    print('total records:', cursor.rowcount)

    # 获取表名信息
    desc = cursor.description
    print("%s %3s" % (desc[0][0], desc[1][0]))

    cursor.scroll(5, mode='absolute')
    results = cursor.fetchall()
    for result in results:
        print(result)

except Exception as e:
    traceback.print_exc()
    # 发生错误时回滚
    connect.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    connect.close()
"""

# 创建链接
connection = pymysql.connect(**config)
# 创建游标1
cursor = connection.cursor()
ids = [1, 2, 3, 4, 5]
name = ["tom", "jerry", "lucy", "marry", "jim"]
age = [30, 27, 33, 29, 31]
sex = ["M", "F", "F", "F", "M"]
values_01 = zip(ids, name, age, sex)
try:
    # 表格中新插入列
    sql_alter01 = """ALTER TABLE test ADD (age int, sex varchar(1))"""

    # 表格中插入数据
    sql_insert_01 = """INSERT INTO test VALUES (%s, %s, %s, %s)"""

    # 执行sql语句
    cursor.executemany(sql_insert_01, values_01)

    # 打印插入成功的信息
    logging.info("==================[insert success]=================")


except Exception as e:
    connection.rollback()
    logging.info("==================[failed]======================")

finally:
    connection.commit()
    cursor.close()
    connection.close()
