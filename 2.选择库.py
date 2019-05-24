import pymysql
import settings

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "use bbs;"


try:
    res = cursor.execute(sql)
    if res == 0:
        print('切换到成功')

except Exception as e:
    print('切换失败')
    conn.rollback()

cursor.close()
conn.close()