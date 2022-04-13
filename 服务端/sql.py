import pymysql
import time
import string

def opendb():
    # 创建连接
    conn = pymysql.connect(host='localhost',user='root',password='123456',charset='utf8mb4')
    # 创建游标
    cursor = conn.cursor()
  
    # 创建数据库db
    sql = "CREATE DATABASE IF NOT EXISTS WaterSort"
    # 执行创建数据库的sql
    cursor.execute(sql)
    # 选择操作的db
    cursor.execute("USE WaterSort")
    # 创建表
    sql = """
        CREATE TABLE IF NOT EXISTS users(
        deviceId VARCHAR(45),
        levels INT(4) DEFAULT NULL,
        lastCommit DATE DEFAULT NULL,
        PRIMARY KEY (deviceId)
        )"""
    cursor.execute(sql)
    return conn,cursor

def update(deviceId,levels):
    conn,cursor = opendb()
    res = False
    # try:
        # 检查是否存在deviceId
    checkSql = "INSERT INTO users(deviceId) SELECT '%s' FROM DUAL WHERE NOT EXISTS(SELECT * FROM users WHERE deviceId='%s')" % (deviceId,deviceId)
    #print(checkSql)
    cursor.execute(checkSql)
    # 更新 levels和左后提交的时间戳
    updateSql = "UPDATE users SET levels=%d,lastCommit=%s WHERE deviceId='%s'" % (levels,int(time.time()),deviceId)
    #print(updateSql)
    cursor.execute(updateSql)
    conn.commit()
    res = True
    # except :
        # 回滚
    conn.rollback()
    conn.close()
    return res
    
def search(deviceId):
    conn,cursor = opendb()
    res = []
    try:
        sql = "SELECT levels,lastCommit FROM users WHERE deviceId='%s'" % (deviceId)
        cursor.execute(sql)
        res = cursor.fetchall()
    except :
        # 回滚
        conn.rollback()
    conn.close()
    if len(res) > 0:
        levels,lastCommit = res[0]
        print(levels)
        print(lastCommit)
        return True,levels,lastCommit
    else:
        print('没有deviceId = %s' % deviceId)
        return False,None,None
            
def insert(deviceId,levels):
    conn,cursor = opendb()
    sql = "INSERT INTO users(deviceId,levels) VALUES('78b',2)"
    res = cursor.execute(sql)
    conn.commit()
    print (res)
    conn.close()


if __name__ == '__main__':
    # insert("abc",1)
    res = update("abc",82)
    #print(res)
#     UPDATE users SET levels=2 WHERE deviceId='abc';
#     search('xiaoming2')
    # print(res)
