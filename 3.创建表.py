
import pymysql
import settings


conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


sql = """
create table user(uid int primary key auto_increment, username char(10) unique not null, usertype enum('0','1') default '0', password char(6) not null, regtime  timestamp default now(), email varchar(100) not null);
"""


res = cursor.execute(sql)


cursor.close()
conn.close()