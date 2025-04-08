from pywebio.input import input, radio
from pywebio.input import *
from pywebio.output import put_buttons, put_text, put_image, clear
from pywebio.output import *
from pywebio import start_server
from pywebio.session import run_js
import datetime
import time
import pymysql
from pywebio.input import checkbox
from pywebio.output import put_text, put_html


conn = pymysql.connect(
    host='172.30.168.171',  # 连接名称，默认127.0.0.1
    user='root@localhost',  # 用户名
    passwd='Audi139id5',  # 密码
    port=3306,  # 端口，默认为3306
    db='store1',  # 数据库名称
    charset='utf8',  # 字符编码
)


def rangeDist():

    def button_click_dist_exit():
        pass
    
    put_row([
                put_image(open("IMG_MainPage/img_StaffPage/s1.jpg", 'rb').read(), width='220px', height='180px'),
                put_image(open("IMG_MainPage/img_StaffPage/s2.webp", 'rb').read(), width='220px', height='180px'),
                put_image(open("IMG_MainPage/img_StaffPage/s3.jpeg", 'rb').read(), width='220px', height='180px'),
                put_image(open("IMG_MainPage/img_StaffPage/s4.jpeg", 'rb').read(), width='220px', height='180px')
            ])

    put_text("\n")
    
    put_text("")
    rangeList = ['4500 ~ 5000', '5000 ~ 5500', '5500 ~ 6000', '6000 ~ 6500', '6500 ~ 7000', '7000 ~ 7500', '7500 ~ 8000', '8000 ~10000', 'More 10000+']
    countList = []
    
    with conn.cursor() as cursor:
        sql1 = f"""SELECT 
            CASE
                WHEN salary < 4500 THEN '4500 - '
                WHEN salary >= 4500 AND salary < 5000 THEN '4500 ~ 5000'
                WHEN salary >= 5000 AND salary < 5500 THEN '5000 ~ 5500'
                WHEN salary >= 5500 AND salary < 6000 THEN '5500 ~ 6000'
                WHEN salary >= 6000 AND salary < 6500 THEN '6000 ~ 6500'
                WHEN salary >= 6500 AND salary < 7000 THEN '6500 ~ 7000'
                WHEN salary >= 7000 AND salary < 7500 THEN '7000 ~ 7500'
                WHEN salary >= 7500 AND salary < 8000 THEN '7500 ~ 8000'
                WHEN salary >= 8000 AND salary < 10000 THEN '8000 ~10000'
                WHEN salary >= 10000 THEN 'More 10000+'
            END AS `range`,
            COUNT(*) AS count_of_staff
            FROM staff
            GROUP BY `range`
            ORDER BY count_of_staff DESC;"""
            
        cursor.execute(sql1)
        result1 = cursor.fetchall()

        put_text("No\t|\tSalaryRange\t|\tCount\t|\t")
        for rows in result1[0:len(result1)]:
            stringList = ""
            
            countList.append(rows[1])
            
            stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
            # print(rows[1])
                # from left to right
            for j in range(len(rows)):
                    # pass
                    # print(j)
                    
                stringList += str(rows[j])
                stringList += "\t|\t"
                        
            put_text(stringList)         
            put_text(" - - - -" * 6)
    
    print(countList)
    
    pass

    # plt.figure(figsize=(8, 6))  # 设置图形大小
    # plt.pie(countList, labels=rangeList, autopct='%1.1f%%', startangle=140)  # 绘制饼状图，并设置百分比显示格式和起始角度
    # plt.title('Salary Range Distribution')  # 设置图形标题
    # plt.show()  # 显示图形

rangeDist()

