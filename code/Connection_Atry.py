# import mysql.connector

# cursor = conn.cursor()
# # 执行 SQL 查询
# cursor.execute("SELECT * FROM your_table")
# # 获取结果
# result = cursor.fetchall()

# # 打印结果
# 关闭游标和连接
# cursor.close()
# conn.close()

import pymysql

conn = pymysql.connect(
    host='172.30.168.171',  # Host name, default is 127.0.0.1
    user='root@localhost',  # Username
    passwd='Audi139id5',  # Password
    port=3306,  # Port, default is 3306
    db='store1',  # Database name
    charset='utf8',  # Character encoding
)


# 获取游标
# cursor = conn.cursor()
# result = cursor.fetchall()


# for row in result:
#     print(row)
    
# # 执行 SQL 查询
# cursor.execute("SELECT * FROM your_table")

# print(conn)

# cursor.close()
# conn.close()

try:
    # 获取游标
    with conn.cursor() as cursor:
        # 执行 SQL 查询
        sql1 = "SELECT * FROM suppliers"
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        
        sql2 = "SELECT * FROM warehouses"
        cursor.execute(sql2)
        result2 = cursor.fetchall()

        sql3 = "SELECT * FROM goods"
        cursor.execute(sql3)
        result3 = cursor.fetchall()

        sql4 = "SELECT * FROM shops"
        cursor.execute(sql4)
        result4 = cursor.fetchall()
        
        # value = int(input("Input a value"))
        # sql = f"SELECT * FROM staff WHERE salary > {value}"
        # sql5 = f"SELECT AVG(salary) FROM staff WHERE (salary > {value})"
        sql5 = "SELECT * FROM staff"
        cursor.execute(sql5)
        result5 = cursor.fetchall()
        
        sql6 = "SELECT * FROM customer"
        cursor.execute(sql6)
        result6 = cursor.fetchall()
        
        sql7 = "SELECT * FROM onlineCustomer"
        cursor.execute(sql7)
        result7 = cursor.fetchall()
        
        sql8 = "SELECT * FROM orders"
        cursor.execute(sql8)
        result8 = cursor.fetchall()

        sql9 = "SELECT * FROM couriers"
        cursor.execute(sql9)
        result9 = cursor.fetchall()

        sql10 = "SELECT * FROM onlineOrders"
        cursor.execute(sql10)      
        result10 = cursor.fetchall()

        # 打印结果
        size = len(result1)

        print("")
        
        # 选定范围
        for i in range(5):
            print(result1[i])
            print(result2[i])
            print(result3[i])
            print(result4[i])
            # print(result5[i])
            print(result6[i])
            print(result7[i])
            print(result8[i])
            print(result9[i])
            print(result10[i])
            print("")


        for i in result5:
            print(i)


finally:
    # 关闭连接
    conn.close()
    


