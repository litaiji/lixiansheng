import pymysql

import settings

import hashlib

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


username = input("请输入用户名：")
password = input("请输入密码：")


sql = "select username,password from user where username=%s and password=sha1(%s)"

res = cursor.execute(sql,[username,password])

if res == 0 :
    print('登录失败')
else:
    print('登录成功')

cursor.close()
conn.close()
