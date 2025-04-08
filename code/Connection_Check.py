import pymysql
import random

## Using to check whether it's succuessfully connecting
conn = pymysql.connect(
    host='172.30.168.171',  # Host name, default is 127.0.0.1
    user='root@localhost',  # Username
    passwd='Audi139id5',  # Password
    port=3306,  # Port, default is 3306
    db='store1',  # Database name
    charset='utf8',  # Character encoding
)

import randGoods
# print(randGoods.imgList)

with conn.cursor() as cursor:    
    for num, i in zip( range(len(randGoods.imgList) + 1),randGoods.imgList):
        ele = str(i)
        print(num, ele)
        ele1 = num
        ele2 = i
        
        sql = f"INSERT INTO websiteBox (webNumber, website) VALUES ({ele1}, '{ele2}');"                    
        cursor.execute(sql)
        conn.commit()
        
    # result = cursor.fetchall()