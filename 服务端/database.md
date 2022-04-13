数据库

Mac端

安装参考: [https://www.jianshu.com/p/0a58ef116ba6?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation](https://www.jianshu.com/p/0a58ef116ba6?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)

```	
安装 brew install mysql
开启服务 mysql.server start
关闭服务 mysql.server stop
默认用户是root,没有密码
修改默认密码 mysqladmin -u root password
修改密码 mysqladmin -u root password -p
用root连接数据库 mysql -u root -p
```

服务器 centeOS

安装参考 [https://www.runoob.com/mysql/mysql-install.html](https://www.runoob.com/mysql/mysql-install.html)	

```
安装
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum update
yum install mysql-server
权限设置：
chown -R mysql:mysql /var/lib/mysql/
初始化 MySQL
mysqld --initialize
启动systemctl start mysqld
关闭 systemctl stop mysqld

默认用户root,密码为空
mysqladmin -u root password "new_password";
```


数据库操作语句

[https://www.yiibai.com/mysql/insert-statement.html](https://www.yiibai.com/mysql/insert-statement.html)	
[https://www.runoob.com/mysql/mysql-drop-tables.html](https://www.runoob.com/mysql/mysql-drop-tables.html)	
[http://c.biancheng.net/cpp/html/1450.html]	

如果不存再插入 [https://blog.51cto.com/u_15309669/3732621](https://blog.51cto.com/u_15309669/3732621)	

```
INSERT INTO users(deviceId) 
SELECT 'aaa' FROM DUAL 
WHERE NOT EXISTS(SELECT * FROM users WHERE deviceId='aaa')
```

更改列的数据列表,INT(4)的4是显示位数
alter table users modify lastCommit INT(4);

**数据库工具可视化:**
dbeaver GUI工具 使用 [https://zhuanlan.zhihu.com/p/443877222](https://zhuanlan.zhihu.com/p/443877222)


**示例代码**

sql.py

```py
import pymysql
import time

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
        lastCommit INT(10) DEFAULT NULL,
        PRIMARY KEY (deviceId)
        )"""
    cursor.execute(sql)
    return conn,cursor

def update(deviceId,levels):
    conn,cursor = opendb()
    res = False
    try:
        # 检查是否存在deviceId
        checkSql = "INSERT INTO users(deviceId) SELECT '%s' FROM DUAL WHERE NOT EXISTS(SELECT * FROM users WHERE deviceId='%s')" % (deviceId,deviceId)
        cursor.execute(checkSql)
        # 更新 levels和左后提交的时间戳
        updateSql = "UPDATE users SET levels=%d,lastCommit=%s WHERE deviceId='%s'" % (levels,int(time.time()),deviceId)
        cursor.execute(updateSql)
        conn.commit()
        res = True
    except :
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
    print(res)
    # UPDATE users SET levels=2 WHERE deviceId='abc';
    # search('xiaoming2')
    # print(res)
```