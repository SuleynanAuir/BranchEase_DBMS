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
import random
from pywebio.input import file_upload
from pywebio.output import put_text
import os

conn = pymysql.connect(
    host='172.30.168.171',  # 连接名称，默认127.0.0.1
    user='root@localhost',  # 用户名
    passwd='Audi139id5',  # 密码
    port=3306,  # 端口，默认为3306
    db='store1',  # 数据库名称
    charset='utf8',  # 字符编码
)

def button_click_staff():                
        time.sleep(0.1)
        clear()
        put_text("helloWorld")
        put_row([
        put_image(open("IMG_MainPage/img_StaffPage/p6.webp", 'rb').read(), width='310px', height='220px'),                    
        put_image(open("IMG_MainPage/img_StaffPage/p2.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_MainPage/img_StaffPage/p1.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_MainPage/img_StaffPage/p5.jpeg", 'rb').read(), width='310px', height='220px')    
        ])
        
        put_text("\n")
        
        put_row([
            put_image(open("IMG_MainPage/img_StaffPage/Edit.jpeg", 'rb').read(), width='100px', height='100px'),
            put_text("\tView overall of all Members!!\n\t\t\tCheck Info: \n\t• Name, phoneNumber, gender...\n\t• Salary, ID, Distribution..."),
            # put_button([" ","", "", "",""], onclick = button_click)                        
        ])
        
        put_row([                                    
            put_button(["View"], onclick = button_click_view)
        ])
        
        put_text("\n")
        
        put_row([
            put_image(open("IMG_MainPage/img_StaffPage/View.jpeg", 'rb').read(), width='100px', height='100px'),
            put_text("\tEdit overall of all Members!!\n\t\t\tChange Info: \n\t• Name, Salary...\n\t• PhoneNumber..."),
            # put_button([" ","", "", "",""], onclick = button_click)                        
        ])
        
        put_row([                                    
            put_button(["Edit"], onclick = button_click_edit)
        ])
        

def button_click_view():
    clear()
    put_row([
        put_image(open("IMG_MainPage/img_StaffPage/p6.webp", 'rb').read(), width='310px', height='220px'),                    
        put_image(open("IMG_MainPage/img_StaffPage/p2.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_MainPage/img_StaffPage/p1.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_MainPage/img_StaffPage/p5.jpeg", 'rb').read(), width='310px', height='220px')    
    ])
    
    put_text("\n")
    put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
            # check data
    with conn.cursor() as cursor:            
        sql1 = f"SELECT * FROM staff"    
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        
        for rows in result1[0:5]:
                stringList = ""
                print(rows)
                stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
            # print(rows[1])
                # from left to right
                for j in range(len(rows)):
                    # pass
                    # print(j)
                    
                    stringList += str(rows[j])
                    stringList += "\t|\t"
                    
                
                put_text(stringList)         
                put_text(" - - - -" * 18)
        
        def button_click_dist():
            
            sum_value = 0
            clear()

            def button_click_dist_rangeDist():
                # import rangeDist
                # rangeDist.rangeDist()
                clear()
                put_row([
                put_column([put_button(["Exit Staff Pages <-"], onclick = button_click_dist_exit), 
                            put_button(["Salary DistPage <-"], onclick = button_click_dist_rangeDist),
                            put_button(["Salary InfoPage <-"], onclick = button_click_dist_info),
                            put_button(["Gender DistPage<-"], onclick = button_click_dist_genderDist)
                            
                           ]
                          ),
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
                        SUM(CASE WHEN gender = 'Male' THEN 1 ELSE 0 END) AS male_count,
                        SUM(CASE WHEN gender = 'Female' THEN 1 ELSE 0 END) AS female_count,
                        COUNT(*) AS total_count_staff                        
                        FROM staff
                        GROUP BY `range`
                        ORDER BY total_count_staff DESC;"""
                        
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()

                    put_text("\n")
                    put_text("No\t\tSalary Range\t\tMale\tFemale\tTotal")                    

                    strList = []
                    
                    for rows in result1[0:len(result1)]:
                        stringList = ""
                        
                        # 对应等级数量
                        # print(rows[1])
                        countList.append(rows[1])
                        
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                        # print(rows[1])
                            # from left to right
                        for j in range(len(rows)):
                                # pass
                                # print(j)
                                
                            stringList += str(rows[j])
                            stringList += "\t|\t"                                    
                        # put_text(stringList)
                        strList.append(stringList)
                        # put_text(" - - - -" * 18)
                
                put_row([
                put_column([
                    put_text(strList[0]),
                    put_text(strList[1]),
                    put_text(strList[2]),
                    put_text(strList[3]),
                    put_text(strList[4]),
                    put_text(strList[5]),
                    put_text(strList[6]),
                    put_text(strList[7]),
                    put_text(strList[8]),                    
                ]),

                # put_image(open("IMG_MainPage/img_StaffPage/s4.jpeg", 'rb').read(), width='500px', height='500px')                
                # ])
                put_column([
                    put_image(open("IMG_MainPage/DistPage/p1.jpg", 'rb').read(), width='400px', height='90px'),
                    # put_image(open("IMG_MainPage/DistPage/p2.webp", 'rb').read(), width='500px', height='90px'),
                    put_image(open("IMG_MainPage/DistPage/p3.jpeg", 'rb').read(), width='400px', height='90px'),
                    put_image(open("IMG_MainPage/DistPage/p4.webp", 'rb').read(), width='400px', height='90px'),
                    put_image(open("IMG_MainPage/DistPage/p5.jpeg", 'rb').read(), width='400px', height='90px'),
                    
                ])
                ])
                
                print(countList)
                print(strList)
                pass
            
            def button_click_dist_genderDist():
                pass
            
            def button_click_dist_info():
                pass
            
            put_row([
                put_column([put_button(["Exit Staff Pages <-"], onclick = button_click_dist_exit), 
                            put_button(["Salary DistPage <-"], onclick = button_click_dist_rangeDist),
                            put_button(["Salary InfoPage <-"], onclick = button_click_dist_info),
                            put_button(["Gender DistPage<-"], onclick = button_click_dist_genderDist)
                            
                           ]
                          ),
                put_image(open("IMG_MainPage/img_StaffPage/s1.jpg", 'rb').read(), width='220px', height='180px'),
                put_image(open("IMG_MainPage/img_StaffPage/s2.webp", 'rb').read(), width='220px', height='180px'),
                put_image(open("IMG_MainPage/img_StaffPage/s3.jpeg", 'rb').read(), width='220px', height='180px'),
                put_image(open("IMG_MainPage/img_StaffPage/s4.jpeg", 'rb').read(), width='220px', height='180px')
            ])

            put_text("\n")
            
            # 计算平均值            
            for row in result1:
                sum_value += float(row[3])
            
            avg_value = sum_value / len(result1) - 1000

            with conn.cursor() as cursor:
                sql = f"SELECT * FROM staff WHERE salary < {avg_value} ORDER BY salary DESC"
                
                cursor.execute(sql)
                result = cursor.fetchall()
                                        
            # avg_value = sum_value / len(result1) - 1000
            
            put_text("Average Salary: " + ("{:.2f}".format(avg_value)) + "\n\t\t\t\t\t\t\t\tMember Lower than AVG: ({} results found)".format(len(result)))
                        
            # with conn.cursor() as cursor:
            #     sql = f"SELECT * FROM staff WHERE salary < {avg_value} ORDER BY salary DESC"
                
            #     cursor.execute(sql)
            #     result = cursor.fetchall()

            for row in result:
                stringList = ""
                stringList += "• "
            # print(rows[1])
                # from left to right
                for j in range(len(row)):
                    # pass
                    # print(j)                    
                    stringList += str(row[j])
                    stringList += "\t|\t"
                    
                put_text(stringList)         
                put_text(" - - - -" * 18)                                                        
                    
            pass
        
        def button_click_dist_exit():
            clear()
            button_click_staff()
            
            
        def button_click_view_more():
            clear()
            # IMG_MainPage/img_StaffPage/07-Bob-Burg-Blog-Great-salesmanship.jpg
            put_image(open("IMG_MainPage/img_StaffPage/07-Bob-Burg-Blog-Great-salesmanship.jpg", 'rb').read(), width='800px', height='300px')
            
            put_text('\n')                        
            put_row([                
                put_button(["Exit Staff Page <-"], onclick = button_click_dist_exit),
                put_text("Scroll down Query one by one (Whole)")
            ])
            
            # inputs = input_group(
            #     "\tSearch",
            #     [input("Click here to Search!", name = "search")]
            #     )
            
            def button_click():
                pass
            
            # put_button(["Search"], onclick = button_click)
            
            with conn.cursor() as cursor:            
                sql1 = f"SELECT * FROM staff"    
                cursor.execute(sql1)
                result1 = cursor.fetchall()
        
                for rows in result1[0:len(result1)]:
                    stringList = ""
                    print(rows)
                    stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
            # print(rows[1])
                # from left to right
                    for j in range(len(rows)):
                    # pass
                    # print(j)
                    
                        stringList += str(rows[j])
                        stringList += "\t|\t"
                        
                    put_text(stringList)         
                    put_text(" - - - -" * 18)
            
            # inputs = input_group(
            #     "\tSearch",
            #     [input("Click here to Search!", name = "search")]
            #     )
                    
            
            pass
        
        def button_click_search_exit():
            clear()
            button_click_staff()
        
        def button_click_exit_Tomain():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ])
        
            put_text("\n")
            put_row([        
            put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            def button_click_goods():
                pass
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            def button_click_warehouse():
                pass
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            def button_click_courier():
                pass
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")    
            
            # end fake Main Page    
            pass
        

        def button_click_shop():
            pass
            
        # Shop (fake main)
            put_row([        
                put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            
            # fake defination                            
                put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")    
            
        
        # 执行 SQL语句
        def button_click_search():
            clear()            
            put_image(open("IMG_MainPage/img_StaffPage/p6.webp", 'rb').read(), width='800px', height='300px')
            put_text("\n")
            
            put_button(["Exit Staff Page <-"], onclick = button_click_search_exit)
            
            search_option = radio("Search Type", options=["ID", "Name", "Salary", "Gender", "Phone"], inline=True)
            
            put_text("\n")
                   
            put_text("Search: [{}]".format(search_option) + "\t -- {}".format(datetime.datetime.now()))
            
            inputs = input_group(
                "\tSearch",
                [input("Click here to Search!", name = "searchCop", placeholder="Click here to Search🔍")]
                )
            
            # print(inputs["searchCop"])
            
            # 去除输入中的首尾空格
            # staffName = str(inputs["searchCop"]).strip()
            
            put_text("\n")            
            # SQL
            with conn.cursor() as cursor:
                
                # Name (1)
                if (search_option == "Name"):          
                    staffName = str(inputs["searchCop"]).strip()  
                    sql1 = f"SELECT * FROM staff WHERE staffName LIKE '{staffName}%'"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    
                    put_text("{} results Found:".format(len(result1)))
                    put_text('\n')
                    put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
                    for rows in result1:
                            stringList = ""
                            print(result1)
                            stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                            for j in range(len(rows)):
                                    # pass
                                    # print(j)
                                    
                                stringList += str(rows[j])
                                stringList += "\t|\t"                            
                                
                            put_text(stringList)         
                            put_text(" - - - -" * 18)                     
                
                # Gender (2)
                if (search_option == "Gender"):
                    gender = str(inputs["searchCop"]).strip()
                    sql2 = f"SELECT * FROM staff WHERE gender = '{gender}'"    
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()
            
                    put_text("{} results Found:".format(len(result2)))
                    put_text('\n')
                    put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
                    for rows in result2:
                            stringList = ""
                            print(result2)
                            stringList += "•" + str(result2.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                            for j in range(len(rows)):
                                    # pass
                                    # print(j)
                                    
                                stringList += str(rows[j])
                                stringList += "\t|\t"                            
                                
                            put_text(stringList)         
                            put_text(" - - - -" * 18)            
                
                # ID (3)            
                if (search_option == "ID"):
                    ID = int(str(inputs["searchCop"]).strip())
                    sql3 = f"SELECT * FROM staff WHERE staffID = {ID}"    
                    cursor.execute(sql3)
                    result3 = cursor.fetchall()
            
                    put_text("{} results Found:".format(len(result3)))
                    put_text('\n')
                    put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
                    for rows in result3:
                            stringList = ""
                            print(result3)
                            stringList += "•" + str(result3.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                            for j in range(len(rows)):
                                    # pass
                                    # print(j)
                                    
                                stringList += str(rows[j])
                                stringList += "\t|\t"                            
                                
                            put_text(stringList)         
                            put_text(" - - - -" * 18)          
                
                # Salary (4)            
                if (search_option == "Salary"):
                    
                    clear()
                    put_image(open("IMG_MainPage/img_StaffPage/p6.webp", 'rb').read(), width='800px', height='300px')                    
                    put_text("\n")
                    put_button(["Exit Staff Page <-"], onclick = button_click_search_exit)

                    inputs = input_group(
                        "Salary Range",
                        [ 
                            input("Input Starting salary:", name = "starSalary", placeholder="e.g: 2000+"),
                            input("Input PeakBest salary:", name = "peakSalary", placeholder="e.g: 3500+")
                        ]
                    )
                    
                    s1 = int(str(inputs["starSalary"]).strip())
                    s2 = int(str(inputs["peakSalary"]).strip())
                    
                    sql4 = f"SELECT * FROM staff WHERE ({s1} < salary AND salary < {s2})"  
                    cursor.execute(sql4)
                    result4 = cursor.fetchall()
                    

                    put_text("Salary Range [{}, {}]".format(inputs["starSalary"], inputs["peakSalary"]))
                    put_text("")
                    
                    put_text("{} results Found:".format(len(result4)))
                    put_text('\n')
                    put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
                    for rows in result4:
                            stringList = ""
                            print(result4)
                            stringList += "•" + str(result4.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                            for j in range(len(rows)):
                                    # pass
                                    # print(j)
                                    
                                stringList += str(rows[j])
                                stringList += "\t|\t"                            
                                
                            put_text(stringList)         
                            put_text(" - - - -" * 18)            

                # Phone(5)
                if (search_option == "Phone"):
                    phone = str(inputs["searchCop"]).strip()
                    sql5 = f"SELECT * FROM staff WHERE staffPhone = '{phone}'"    
                    cursor.execute(sql5)
                    result5 = cursor.fetchall()
            
                    put_text("{} results Found:".format(len(result5)))
                    put_text('\n')
                    put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
                    for rows in result5:
                            stringList = ""
                            print(result5)
                            stringList += "•" + str(result5.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                            for j in range(len(rows)):
                                    # pass
                                    # print(j)
                                    
                                stringList += str(rows[j])
                                stringList += "\t|\t"                            
                                
                            put_text(stringList)         
                            put_text(" - - - -" * 18)            

                # if (search_option == "Gender"):
                #     gender = str(inputs["searchCop"]).strip()
                #     sql2 = f"SELECT * FROM staff WHERE gender = '{gender}'"    
                #     cursor.execute(sql2)
                #     result2 = cursor.fetchall()
            
                #     put_text("{} results Found:".format(len(result2)))
                #     put_text('\n')
                #     put_text("No\t\tstaffID\t\tshopID\t\tName\t\t\tSalary\t\tGender\t\tPhone")
                #     for rows in result2:
                #             stringList = ""
                #             print(result2)
                #             stringList += "•" + str(result2.index(rows) + 1) + "\t|\t"
                #             # print(rows[1])
                #                 # from left to right
                #             for j in range(len(rows)):
                #                     # pass
                #                     # print(j)
                                    
                #                 stringList += str(rows[j])
                #                 stringList += "\t|\t"                            
                                
                #             put_text(stringList)         
                #             put_text(" - - - -" * 18)            
                              
                            
                    
            pass
            
        put_row([
        put_button(["View More"], onclick = button_click_view_more),
        put_button(["Distribution"], onclick = button_click_dist),
        put_button(["Searching"], onclick = button_click_search),
        put_button(["Exit Staff Page <-"], onclick = button_click_dist_exit),
        put_button(["Exit Main Page <-"], onclick = button_click_exit_Tomain)
        ])
        
        
    pass
# button_click_view()

def button_click_edit():
    pass

def MainPage():
    
    def RegisterPage():
        clear()
        with conn.cursor() as cursor:
            put_row([
            # put_image(open("IMG_RegistPage/ps3.jpeg", 'rb').read(), width='600px', height='320px'),
            put_image(open("IMG_RegistPage/ps4.jpeg", 'rb').read(), width='1200px', height='320px')]
            )                            
            
            put_text("");
            put_text("\t\t\t\t\t\t\t\t\t\tDesign Register")
            country_options = ['United States',
                    'China',
                    'Russia',
                    'India',
                    'Brazil',
                    'Germany',
                    'France',
                    'United Kingdom',
                    'Japan',
                    'Canada',
                    'Australia',
                    'South Korea',
                    'Spain',
                    'Italy',
                    'Mexico',
                    'Indonesia',
                    'Netherlands',
                    'Switzerland',
                    'Singapore',
                    'United Arab Emirates',
                    'Saudi Arabia',
                    'Turkey',
                    'Argentina',
                    'Sweden',
                    'Poland',
                    'Belgium',
                    'Norway',
                    'Austria',
                    'Thailand',
                    'Iran',
                    'Egypt',
                    'Denmark',
                    'Greece',
                    'Czech Republic',
                    'Portugal',
                    'Israel',
                    'Ireland',
                    'Malaysia',
                    'Pakistan',
                    'South Africa',
                    'Vietnam',
                    'Philippines',
                    'Finland',
                    'Hungary',
                    'Ukraine',
                    'Chile',
                    'Romania',
                    'Iraq',
                    'Nigeria',
                    'New Zealand']

            selected_country = select("Select Region:", country_options)
        
            global inputs1
        
            inputs0 = input_group(
        "\tRegister page", # page Name
        [
            # input("Input Your Age", name = "age"),
            input("Please Input City", name = "city"),                                 
            input("Please Input Account\n", name = "account", placeholder="6 separate Integer"),
            input("Please Input Password", type = PASSWORD, name = "password", placeholder="5 Integer Password"),
            input("Please Verify Password", type = PASSWORD, name = "verfPassword", placeholder="5 Integer Password")
        ]
        )
            
            # time.sleep(0.3)
            clear()
            put_image(open("IMG_RegistPage/ps3.jpeg", 'rb').read(), width='1200px', height='350px')
            times = 1
            
            # 密码验证
            while (True):
                if (inputs0["password"] != inputs0["verfPassword"]):                                
                    inputs1 = input_group(
                        "Reput Page",
                        [
                        input("Please Input Password", type = PASSWORD, name = "password", placeholder="5 Integer Password"),
                        input("Please Verify Password", type = PASSWORD, name = "verfPassword", placeholder="5 Integer Password")
                        ]
                    )
                    
                    if (inputs0["password"] != inputs0["verfPassword"]):
                        put_text("Error x{}\t—— {}".format(times, datetime.datetime.now()))
                        times += 1
                    # clear()
                
                else:
                    put_text("\n")
                    put_text("\t\t\t\t\t\t\t\t\t\t\tCorrect !!!")
                    time.sleep(1.5)                
                    clear()
                    break
            
            # correct input then store the Logininfo
            loginID = inputs0["account"]
            loginPassword = inputs0["password"]
            
            sql = f"SELECT COUNT(*) FROM shops"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            put_text("Finish")
            # print(result)
            result = result[0][0]

            
            sql = f"INSERT INTO loginInfo (loginID, loginPassword) \
                    VALUES ({loginID}, {loginPassword})"        
            cursor.execute(sql)
            result = cursor.fetchall()
            
            conn.commit()    
            
        # put_row([
        #     put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
        #     put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
        #     put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
        #     put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
        # ])
        
        # put_column(
        #     [
        #         put_button(["[Register Click]"], onclick = RegisterPage),
        #         put_button(["[Login Click]"], onclick = LoginPage)
        #     ]
        # )         
        # return
    
        # LoginPage()                


    def LoginPage():
        
        def button_click_loc(a):
            pass
            # import geocoder
            # # 获取自己所在地区的位置信息
            # location = geocoder.ip('me')
            # if location.ok:
            #     put_text("Yours: Latitude {}ºN \t Longitude {}ºE (China Mainland)\t-- {}".format(location.lat, location.lng, datetime.datetime.now()))
        
        clear()
        # (10001, 'ElectroMart', '123 Main Street, Anytown, USA'),
        put_row([
            put_image(open("IMG_LoginPage/Asp/ps1.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_LoginPage/Asp/ps2.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_LoginPage/Asp/ps3.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_LoginPage/Asp/ps4.jpeg", 'rb').read(), width='310px', height='220px'),       
        ])
        
        put_text("")
        # put_buttons(["Location"], onclick = button_click_loc)
        
        # put_image(open("IMG_LoginPage/180387505.jpg", 'rb').read(), width='1200px', height='350px')
        country_options = ['United States',
                    'China',
                    'Russia',
                    'India',
                    'Brazil',
                    'Germany',
                    'France',
                    'United Kingdom',
                    'Japan',
                    'Canada',
                    'Australia',
                    'South Korea',
                    'Spain',
                    'Italy',
                    'Mexico',
                    'Indonesia',
                    'Netherlands',
                    'Switzerland',
                    'Singapore',
                    'United Arab Emirates',
                    'Saudi Arabia',
                    'Turkey',
                    'Argentina',
                    'Sweden',
                    'Poland',
                    'Belgium',
                    'Norway',
                    'Austria',
                    'Thailand',
                    'Iran',
                    'Egypt',
                    'Denmark',
                    'Greece'
                    ]
        
        put_text("\t\t\t\t\t\t\t\t\t\tDesign Your Shop!")

        selected_country = select("Select Region:", country_options)
        
        
        inputs1 = input_group(
            "Design Your Shop",
            [
            input("Please Input ShopName:", name = "shopName"),
            input("•1  Input City:", name = "City"),
            input("•2  Input Town:", name = "Town"),
            input("•3  Input Street:", name = "Street")        
            ]
            )
        
        put_text("Shop Centre: "+ "*" + inputs1["shopName"] + "*" + " was born !")
        put_text("locat: " + str(selected_country) + " / " + inputs1["City"] + " / " + inputs1["Town"] + " / " + inputs1["Street"] + " -- {}".format(datetime.datetime.now()))
        
        # time.sleep(5)
        
        global input_info
        input_info = str(selected_country) + " " + inputs1["City"] + " " + inputs1["Town"] + " " + inputs1["Street"]        

        
        # break
    # login Page

    # Using to Login in   
    # clear()
    
    def condition(a):
        if (a == 1):
            RegisterPage()
        if (a == 2):
            LoginPage()
    
    
    # put_row([
    #     put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
    #     put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
    #     put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
    #     put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
    # ])
    
    # put_column(
    #     [
    #         put_button(["[Register Click]"], onclick = RegisterPage),
    #         # put_button(["[Login Click]"], onclick = LoginPage)
    #     ]
    # )
    
    
    RegisterPage()
    LoginPage()            
                
    # clear()
    # Main Page's Home Page
    put_row([
        put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
    ])
    
    
    def button_click(a):
        pass
    
    # Shop
    def button_click_shop(a): 
        clear()
        
        def button_click_exit_Toshop():
            clear()
            # put_column([
            #     put_button(["Exit Shop Page <-"], onclick = button_click_exit_Toshop),
            #     put_button(["Exit Main Page <-"], onclick = button_click_exit_Tomain)
            # ])       
                 
            put_row([
            put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ]) 
            
            put_text('\n')
            
            put_column([
                put_button(["Exit Shop Page <-"], onclick = button_click_exit_Toshop),
                put_button(["Exit Main Page <-"], onclick = button_click_exit_Tomain)
            ])              
            # put_button(["Exit Shop Page <-"], onclick = button_click_exit_Toshop)    
            for rows in result1[0:5]:
                    stringList = ""
                    print(rows)
                    stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
                    for j in range(len(rows)):                        
                        stringList += str(rows[j])
                        stringList += "\t|\t"                        
                    
                    put_text(stringList)         
                    put_text(" - - - -" * 18)
                             
            pass
        
        def button_click_exit_Tomain():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ])
        
            put_text("\n")    
        # Shop (fake main)
            put_row([        
            put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")    
            
            # end fake Main Page    
            pass

        
        # Shop Page
        put_row([
        put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
        ])               
        
        def button_click_search_search():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
        ])            
            
            put_column([
            put_button(["Exit Shop Page"], onclick = button_click_exit_Toshop),
            put_button(["Exit Main Page"], onclick = button_click_exit_Tomain)
            ])
            
            search_option = radio("Search Type", options = ["Name", "ID", "Address"], inline = True)
            
            put_text("\n")
            put_text("Search: [{}]".format(search_option) + "\t -- {}".format(datetime.datetime.now()))    

            inputs = input_group(
                "\tSearch",
                [input("Click here to Search!", name = "searchCop", placeholder="Click here to Search🔍")]
                )                                            

            with conn.cursor() as cursor:            
                if (search_option == "Name"):
                    name = inputs['searchCop'].strip()          
                    sql1 = f"SELECT * FROM shops WHERE shopName LIKE '%{name}%'"                    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    
                    put_text("{} results Found:".format(len(result1)))
                    put_text('\n')
                    put_text("No\t\tShopID\t\tShopName\t\tAddress")
                        
                    for rows in result1:
                        stringList = ""
                        print(result1)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                                # print(rows[1])
                                    # from left to right
                        for j in range(len(rows)):
                                        # pass
                                        # print(j)
                                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                            
                                    
                        put_text(stringList)         
                        put_text(" - - - -" * 18)                                 

                if (search_option == "ID"):
                    shopID = inputs['searchCop'].strip()          
                    sql1 = f"SELECT * FROM shops WHERE shopID = {shopID}"                    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    
                    put_text("{} results Found:".format(len(result1)))
                    put_text('\n')
                    put_text("No\t\tShopID\t\tShopName\t\tAddress")
                        
                    for rows in result1:
                        stringList = ""
                        print(result1)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                                # print(rows[1])
                                    # from left to right
                        for j in range(len(rows)):
                                        # pass
                                        # print(j)
                                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                            
                                    
                        put_text(stringList)         
                        put_text(" - - - -" * 18)                 

                if (search_option == "Address"):
                    shopAddress = inputs['searchCop'].strip()          
                    sql1 = f"SELECT * FROM shops WHERE shopName LIKE '%{shopAddress}%'"                    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    
                    put_text("{} results Found:".format(len(result1)))
                    put_text('\n')
                    put_text("No\t\tShopID\t\tShopName\t\tAddress")
                        
                    for rows in result1:
                        stringList = ""
                        print(result1)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                                # print(rows[1])
                                    # from left to right
                        for j in range(len(rows)):
                                        # pass
                                        # print(j)
                                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                            
                                    
                        put_text(stringList)         
                        put_text(" - - - -" * 18)         
        put_text("\n")
        
        put_column([
        put_button(["Exit Shop Page <-"], onclick = button_click_exit_Toshop),
        put_button(["Exit Main Page <-"], onclick = button_click_exit_Tomain),
        put_button(["Search Shop Q  <-"], onclick = button_click_search_search)
        ])
        
        put_text("No\t|\tID\t\t|\tShopName\t|\tShop Address")
        
        with conn.cursor() as cursor:            
            sql1 = f"SELECT * FROM shops"    
            cursor.execute(sql1)
            result1 = cursor.fetchall()
        
        for rows in result1[0:5]:
                stringList = ""
                print(rows)
                stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
                for j in range(len(rows)):                        
                    stringList += str(rows[j])
                    stringList += "\t|\t"                        
                    
                put_text(stringList)         
                put_text(" - - - -" * 18) 
        
        
        # with conn.cursor() as cursor:            
        #     sql1 = f"SELECT * FROM shops"    
        #     cursor.execute(sql1)
        #     result1 = cursor.fetchall()
            
            # for rows in result1[0:5]:
            #         stringList = ""
            #         print(rows)
            #         stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
            #     # print(rows[1])
            #         # from left to right
            #         for j in range(len(rows)):                        
            #             stringList += str(rows[j])
            #             stringList += "\t|\t"                        
                    
            #         put_text(stringList)         
            #         put_text(" - - - -" * 18)        
                
        
    def button_click_staff(a):    
        
        def button_click_exit_Tomain():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ])
        
            put_text("\n")    
        # Shop (fake main)
            put_row([        
            put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")         
            
########################################################################################                    
        time.sleep(0.1)
        clear()
        put_text("helloWorld")
        put_row([
        put_image(open("IMG_MainPage/img_StaffPage/p6.webp", 'rb').read(), width='310px', height='220px'),                    
        put_image(open("IMG_MainPage/img_StaffPage/p2.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_MainPage/img_StaffPage/p1.webp", 'rb').read(), width='310px', height='220px'),
        put_image(open("IMG_MainPage/img_StaffPage/p5.jpeg", 'rb').read(), width='310px', height='220px')    
        ])
                
        put_text("\n")
        put_button(["Exit to Main Page <-"], onclick = button_click_exit_Tomain)
        put_text("\n")
        
        put_row([
            put_image(open("IMG_MainPage/img_StaffPage/Edit.jpeg", 'rb').read(), width='100px', height='100px'),
            put_text("\tView overall of all Members!!\n\t\t\tCheck Info: \n\t• Name, phoneNumber, gender...\n\t• Salary, ID, Distribution..."),
            # put_button([" ","", "", "",""], onclick = button_click)                        
        ])
        
        put_row([                                    
            put_button(["View"], onclick = button_click_view)
        ])
        
        put_text("\n")
        
        put_row([
            put_image(open("IMG_MainPage/img_StaffPage/View.jpeg", 'rb').read(), width='100px', height='100px'),
            put_text("\tEdit overall of all Members!!\n\t\t\tChange Info: \n\t• Name, Salary...\n\t• PhoneNumber..."),
            # put_button([" ","", "", "",""], onclick = button_click)                        
        ])
        
        put_row([                                    
            put_button(["Edit"], onclick = button_click_edit)
        ])
                
    def button_click_goods(a):
        
        def button_click_exit_Tomain():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ])
        
            put_text("\n")    
        # Shop (fake main)
            put_row([        
            put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")    
            
            # end fake Main Page    
            pass
            
        def button_click_order():
            clear()
            put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
            
            with conn.cursor() as cursor:            
                sql1 = f"SELECT * FROM orders"    
                cursor.execute(sql1)
                result1 = cursor.fetchall()

            put_text('')
            # put_text("\t\t\t\t\t\t\t\t\t\tOrder List\n")
            put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
            put_text('\n')
            put_text("\t\t\t\t\t\t\t\t\t\tOrder List\n")
            put_text("No\t|\tOrderID\t|\tCustID\t|\tQuantity\t|\tDate\t|\tgoodsID\t|\tshopID\t|\tstaffID")
            for rows in result1:
                stringList = ""
                print(rows)
                stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                    # print(rows[1])
                        # from left to right
                for j in range(len(rows)):                        
                    stringList += str(rows[j])
                    stringList += "\t|\t"                        
                        
                put_text(stringList) 
            
            
            # Option
            search_option = radio("You wanna to Check", options = ["Order", "Customer", "goods", "shops", "staffs"], inline = True)   


            # judgement 
##########################################################################################################################                                                                
            
            if (search_option == "Order"):
                clear()
                put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM orders"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("\t\t\t\t\t\t\t\t\tOrder List")
                    put_text("No\t|\tOrderID\t|\tCustID\t|\tQuantity\t|\tDate\t|\tgoodsID\t|\tshopID\t|\tstaffID")
                    for rows in result1:
                        stringList = ""
                        print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList)                                                         
            
                inputs = input_group(
                    "Search Box",
                    [input("Input OrderID", name = "answer", placeholder="Input Order ID")]
                )
                
                answer = int(inputs["answer"])
                clear()
                put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM orders WHERE (orderID = {answer})"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("")
                    put_text("\t\t\t\t\t\t\t\t\tOrder List")
                    put_text("No\t|\tOrderID\t|\tCustID\t|\tQuantity\t|\tDate\t|\tgoodsID\t|\tshopID\t|\tstaffID")
                    for rows in result1:
                        stringList = ""
                        print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList) 
                                                    
##########################################################################################################################                                                                
            if (search_option == "Customer"): 
                clear()                                
                clear()
                put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM customer"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("\t\t\t\t\t\t\t\t\tCustomer List")
                    put_text("No\t|\tCustID\t|\tPhone\t|\tCustname\t|\t")
                    for rows in result1:
                        stringList = ""
                        print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList)                                                         
            
                inputs = input_group(
                    "Search Box",
                    [input("Input CustomerID", name = "answer", placeholder="Input Cust ID")]
                )
                
                answer = int(inputs["answer"])
                clear()
                put_row([
                    put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
                ])
                
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM customer WHERE (customerID = {answer})"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("")
                    put_text("\t\t\t\t\t\t\t\t\tCustomer List")
                    put_text("No\t|\tCustID\t|\tCust Phone")
                    for rows in result1:
                        stringList = ""
                        # print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList) 
                                
##########################################################################################################################                                                                
                
            if (search_option == "goods"):
                clear()
                put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM goods"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("\t\t\t\t\t\t\t\t\tGoods List")
                    put_text("No\t|\tgoodsID\t|\tPrice\t|\tgoodsName\t|\twarehouseID\t|\t")
                    for rows in result1:
                        stringList = ""
                        print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList)                                                         
            
                inputs = input_group(
                    "Search Box",
                    [input("Input GoodsID", name = "answer", placeholder="Input Goods ID")]
                )
                
                
                answer = int(inputs["answer"])
                clear()
                put_row([
                    put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
                ])                
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM goods WHERE (goodsID = {answer})"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    # put_text("No\t|\tCustID\t|\tCust Phone")
                    put_text("")
                    put_text("\t\t\t\t\t\t\t\t\tGoods List")
                    put_text("No\t|\tgoodsID\t|\tPrice\t|\tgoodsName\t|\twarehouseID\t|\t")
                    for rows in result1:
                        stringList = ""
                        # print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                                                        
                        put_text(stringList)                 

##########################################################################################################################                                                                
                
            if (search_option == "shops"):
                clear()
                put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM shops"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("\t\t\t\t\t\t\t\t\tShops List")
                    put_text("No\t|\tshopID\t|\tshopName\t|\tAddress\t|\t")
                    for rows in result1:
                        stringList = ""
                        print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList)                                                         
            
                inputs = input_group(
                    "Search Box",
                    [input("Input ShopID", name = "answer", placeholder="Input Shop ID")]
                )         
                
                
                answer = int(inputs["answer"])
                clear()
                put_row([
                    put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
                ])                
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM shops WHERE (shopID = {answer})"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    # put_text("No\t|\tCustID\t|\tCust Phone")
                    put_text("")
                    put_text("\t\t\t\t\t\t\t\t\tShops List")
                    put_text("No\t|\tshopID\t|\tshopName\t|\tAddress\t|\t")
                    for rows in result1:
                        stringList = ""
                        # print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                                                        
                        put_text(stringList)                                                          
            
##########################################################################################################################                                                                

            if (search_option == "staffs"):
                clear()
                put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM orders"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    put_text("\t\t\t\t\t\t\t\t\tStaff List")
                    put_text("No\t|\tstaffID\t|\tshopID\t|\tName\t|\tSalary\t|\tGender\t|\tPhone\t|\t")
                    for rows in result1:
                        stringList = ""
                        print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                        
                                
                        put_text(stringList)                                                         
            
                inputs = input_group(
                    "Search Box",
                    [input("Input StaffID", name = "answer", placeholder="Input Staff ID")]
                )            
                
                
                answer = int(inputs["answer"])
                clear()
                put_row([
                    put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
                    put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
                ])                
                put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                
                with conn.cursor() as cursor:            
                    sql1 = f"SELECT * FROM staff WHERE (staffID = {answer})"    
                    cursor.execute(sql1)
                    result1 = cursor.fetchall()
                    put_text('\n')
                    # put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
                    # put_text("No\t|\tCustID\t|\tCust Phone")
                    put_text("")
                    put_text("\t\t\t\t\t\t\t\t\tStaff List")
                    put_text("No\t|\tstaffID\t|\tshopID\t|\tName\t|\tSalary\t|\tGender\t|\tPhone\t|\t")
                    for rows in result1:
                        stringList = ""
                        # print(rows)
                        stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                            # print(rows[1])
                                # from left to right
                        for j in range(len(rows)):                        
                            stringList += str(rows[j])
                            stringList += "\t|\t"                                                        
                        put_text(stringList)                   
                        
##########################################################################################################################                                                                
        
        def button_click_exit_goods():
            clear()
            put_row([
                put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
                put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
                put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
                put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
            ])
            
            # search_option = radio("You wanna to Check", options = ["goodsID", "goodsName", "goodsPrice"], inline = True)
            put_row(
                [
            put_button(["[Refresh]"], onclick = button_click_refresh),
            put_button(["[Orders]"], onclick = button_click_order),
            put_button(["[Add +]"], onclick = button_click_add),
            put_button(["[Cut -]"], onclick = button_click_cut),
            put_button(["[Exit Main]"], onclick = button_click_exit_Tomain)
                ]
            )            
            
            start_range = 15
            end_range = 45
            count_of_numbers = 3
            random_numbers = random.sample(range(start_range, end_range + 1), count_of_numbers)            

            rand_IDboxs = []
            rand_numboxs = random_numbers
            
            # 生成随机ID
            for i in range(3):
                ele = "30"
                ele += str(rand_numboxs[i] + 3)
                ele = int(ele)
                rand_IDboxs.append(ele)
            
            rand_IDbox.sort()            
            put_text("No\t|\tGood ID\t|\tProducts Name (detailed)\t|\tPrice ($)")            
            
            with conn.cursor() as cursor:
                m1 = rand_IDboxs[0]
                m2 = rand_IDboxs[1]
                m3 = rand_IDboxs[2]
                # i4 = rand_IDbox[3]
                sql = f"SELECT goodsID, goodsName, goodsPrice FROM goods WHERE ((goodsID = {m1}) OR (goodsID = {m2}) OR (goodsID = {m3})) ORDER BY goodsID ASC"   
                cursor.execute(sql)
                result = cursor.fetchall()            

            import randGoods            
            site1 = randGoods.imgList[rand_numboxs[0] + 3]
            site2 = randGoods.imgList[rand_numboxs[1] + 3]
            site3 = randGoods.imgList[rand_numboxs[2] + 3]
            print("img" + str(site1) + str(site2) + str(site3))            
            # 展示随机推荐产品信息
            for rows in result:
                stringList = ""
                # print(rows)
                # stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                    # print(rows[1])
                        # from left to right
                for j in range(len(rows)):                        
                    stringList += str(rows[j])
                    stringList += "\t|\t"                        
                        
                put_row([
                    put_text(stringList),                
                    # put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='400px', height='150px')
                ])         
                # put_text(" - - - -" * 18)         

            # 展示随机推荐的产品图片
            put_row([
                put_image(open(site1, 'rb').read(), width='300px', height='150px'),
                put_text(" "),
                put_image(open(site2, 'rb').read(), width='300px', height='150px'),
                put_text(""),
                put_image(open(site3, 'rb').read(), width='300px', height='150px')
            ])   
                     
            # put_button(["Exit Goods Page"], onclick = button_click_exit_goods)
            search_option = radio("You wanna to Check", options = ["goodsID", "goodsName", "goodsPrice"], inline = True)            
            
            put_text("Search: [{}]".format(search_option) + "\t -- {}".format(datetime.datetime.now()))
            # put_button(["Exit Goods Page"], onclick = button_click_exit_goods)            
            
                            
        clear()
        put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='200px'), 
            put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='200px'), 
        ])
        
        put_text('')
        
        
        def button_click_refresh():
            time.sleep(0.1)
            clear()
            put_row([
                put_image(open("IMG_MainPage/img_GoodsPage/p1.png", 'rb').read(), width='310px', height='220px'), 
                put_image(open("IMG_MainPage/img_GoodsPage/p2.jpeg", 'rb').read(), width='310px', height='220px'), 
                put_image(open("IMG_MainPage/img_GoodsPage/p3.jpeg", 'rb').read(), width='310px', height='220px'), 
                put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='310px', height='220px'), 
            ])    
            
            put_row([ 
            put_button(["[Refresh]"], onclick = button_click_refresh),
            put_button(["[Exit Main]"], onclick = button_click_exit_Tomain)
            ])
            
            start_range = 15
            end_range = 45
            count_of_numbers = 3

            random_numbers = random.sample(range(start_range, end_range + 1), count_of_numbers)
            
            # print(random_numbers) # List
            
            rand_IDboxs = []
            rand_numboxs = random_numbers
            
            # 生成随机ID
            for i in range(3):
                ele = "30"
                ele += str(rand_numboxs[i] + 3)
                ele = int(ele)
                rand_IDboxs.append(ele)
            
            rand_IDbox.sort()
            
            put_text("No\t|\tGood ID\t|\tProducts Name (detailed)\t|\tPrice ($)")
            
            print("rand_IDbox:" + str(rand_IDboxs))
            
            with conn.cursor() as cursor:
                m1 = rand_IDboxs[0]
                m2 = rand_IDboxs[1]
                m3 = rand_IDboxs[2]
                # i4 = rand_IDbox[3]
                sql = f"SELECT goodsID, goodsName, goodsPrice FROM goods WHERE ((goodsID = {m1}) OR (goodsID = {m2}) OR (goodsID = {m3})) ORDER BY goodsID ASC"   
                cursor.execute(sql)
                result = cursor.fetchall()
            
            print("result:" + str(result))   

            import randGoods            
            site1 = randGoods.imgList[rand_numboxs[0] + 3]
            site2 = randGoods.imgList[rand_numboxs[1] + 3]
            site3 = randGoods.imgList[rand_numboxs[2] + 3]
            print("img" + str(site1) + str(site2) + str(site3))      
                  
            # 展示随机推荐产品信息
            for rows in result:
                stringList = ""
                # print(rows)
                stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                    # print(rows[1])
                        # from left to right
                for j in range(len(rows)):                        
                    stringList += str(rows[j])
                    stringList += "\t|\t"                        
                        
                put_row([
                    put_text(stringList),                
                    # put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='400px', height='150px')
                ])         
                # put_text(" - - - -" * 18)         

            # 展示随机推荐的产品图片
            put_row([
                put_image(open(site1, 'rb').read(), width='300px', height='150px'),
                put_text(" "),
                put_image(open(site2, 'rb').read(), width='300px', height='150px'),
                put_text(""),
                put_image(open(site3, 'rb').read(), width='300px', height='150px')
            ])            
            
            search_option = radio("You wanna to Check", options = ["goodsID", "goodsName", "goodsPrice"], inline = True)
            
            put_text("Search: [{}]".format(search_option) + "\t -- {}".format(datetime.datetime.now()))
            # put_button(["Exit Goods Page"], onclick = button_click_exit_goods)

        def button_click_add():
            clear()
            put_row([
                put_image(open("IMG_MainPage/img_GoodsPage/s1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_MainPage/img_GoodsPage/s2.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_MainPage/img_GoodsPage/s3.png", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_MainPage/img_GoodsPage/s4.webp", 'rb').read(), width='310px', height='220px'),

            ])
            
            put_column([
            put_button(["[Exit Main]"], onclick = button_click_exit_Tomain)
            ])

            # 运用SQL查询目前最大的仓库号
            with conn.cursor() as cursor:
                sql = f"SELECT MAX(warehouseID), MIN(warehouseID), MAX(goodsID), MIN(goodsID) FROM goods"
                cursor.execute(sql)
                result = cursor.fetchall()
            
            # print("SQL Result:" + str(result))
            min_id1 = 0
            max_id1 = 0
            
            max_id2 = 0
            
            for i in result:
                max_id1 = i[0]
                min_id1 = i[1]
                max_id2 = i[2]
                
            inputs = input_group(
                "Add Goods",
                [
                input("Input Goods Name", name = "name", placeholder="e.g: Apple Vision Pro+"),
                input("Input Goods ID (Range: 3050+)!", name = "ID", placeholder="e.g: {} (Recommended)".format(max_id2 + 1)),
                input("Input Goods Price ($)", name = "price", placeholder="e.g: 189.9"),
                input("Input Goods WarehouseID (Range [{}~{}])!".format(min_id1, max_id1), name = "wareID", placeholder="e.g: {}~{}".format(min_id1, max_id1))
            ])
            
            # Using SQL to add the goods into the dataBase
            with conn.cursor() as cursor:
                goodsID = inputs["ID"]
                goodsName = inputs["name"]
                goodsPrice = inputs["price"]
                warehouseID = inputs["wareID"]
                                
                sql = f"""INSERT INTO goods (goodsID, goodsPrice, goodsName, warehouseID) 
                VALUES ({goodsID}, {goodsPrice}, '{goodsName}', {warehouseID});                
                """
                cursor.execute(sql)
                conn.commit()
                result = cursor.fetchall()
            
            put_text("\n")
            put_text("\t\t\t\tID\t|\tName\t|\tPrice ($)\t|\twareID")
            put_text("Add Successfully: {} / {} / {} / ({}) -- {}".format(
                inputs["ID"],
                inputs["name"],
                inputs["price"],
                inputs["wareID"],
                datetime.datetime.now()
            ))
            
            uploaded_file = file_upload(label='Please select Image for products', accept='image/*')

            import randGoods
            a = len(randGoods.imgList)
            
            if uploaded_file:
                # 获取上传文件的名称和内容
                file_name = input("Setting Name for products:", placeholder="e.g: p{}.jpg".format(a))
                
                uploaded_file_name = uploaded_file['filename']
                file_content = uploaded_file['content']

                # 设置保存图片的文件夹路径
                save_folder = 'IMG_MainPage/img_randGoods'
                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)

                # 保存图片到指定文件夹
                save_path = os.path.join(save_folder, file_name)
                
                with open(save_path, 'wb') as f:
                    f.write(file_content)

                # print("Path:" + str(save_path))
                import randGoods
                randGoods.add_image_path(save_path)
                # randGoods.imgList.append(save_path)
                
                # 显示保存成功的消息
                nowTime = datetime.datetime.now()
                put_text(f'Image Successfully Saved:{save_path} -- {nowTime}')        
                
                # 添加网页的地址加入到数据库
                with conn.cursor() as cursor:
                    sql1 = f"SELECT * FROM websiteBox"                        
                    cursor.execute(sql1)
                    result = cursor.fetchall()
                    
                    a = len(result)
                    
                    sql2 = f"INSERT INTO websiteBox(webNumber, website) VALUES ({a}, '{save_path}')"
                    cursor.execute(sql2)
                    conn.commit()
                                                                    
            
        def button_click_cut():
            clear()
            put_row([
                put_image(open("IMG_MainPage/img_GoodsPage/s1.jpeg", 'rb').read(), width='310px', height='200px'),
                put_image(open("IMG_MainPage/img_GoodsPage/s2.jpeg", 'rb').read(), width='310px', height='200px'),
                put_image(open("IMG_MainPage/img_GoodsPage/s3.png", 'rb').read(), width='310px', height='200px'),
                put_image(open("IMG_MainPage/img_GoodsPage/s4.webp", 'rb').read(), width='310px', height='200px'),

            ])
            
            put_column([
            put_button(["[Exit Main]"], onclick = button_click_exit_Tomain),
            ])            
            
            # 查询goodsID范围
            with conn.cursor() as cursor:
                sql = f"SELECT MAX(goodsID), MIN(goodsID) FROM goods"
                cursor.execute(sql)
                result = cursor.fetchall()
            
                # print("SQL Result:" + str(result))
            min_id = 0
            max_id = 0
            
            for i in result:
                max_id = i[0]
                min_id = i[1]
                               
                                           
            inputs = input_group(
                "Cut Goods",
                [
                input("Input Goods Name", name = "name", placeholder = "e.g: Canon EOS 6D"),
                input("Input Goods ID", name = "ID", placeholder = "{}~{}".format(min_id, max_id)),                
            ])
            
               
            # 执行删除指令
            with conn.cursor() as cursor:
                goodsID = int(inputs["ID"].strip())
                goodsName = inputs["name"].strip()
                sql = f"SELECT * FROM goods WHERE ((goodsID = {goodsID}) OR (goodsName = '{goodsName}')) ORDER BY goodsID ASC"   
                cursor.execute(sql)
                result = cursor.fetchall()      

            put_text("\t\t\t\t\t\t\t\t\t{} results found".format(len(result)))
            # put_text("No\t|\tGoods ID\t|\tPrices\t|\tGoods Name\t|\twarehouseID")
            
            # print out the result
            for rows in result:
                stringList = ""
                stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                # from left to right
                for j in range(len(rows)):                        
                    stringList += str(rows[j])
                    stringList += "\t|\t"                        
                        
                put_text(stringList)                
                
            print(int(inputs["ID"][len(inputs["ID"]) - 2 : len(inputs["ID"])]))
            print(int(inputs["ID"][len(inputs["ID"]) - 2 : len(inputs["ID"])]))


            import randGoods
            answer = int(inputs["ID"][len(inputs["ID"]) - 2 : len(inputs["ID"])])
            site = randGoods.imgList[answer]
            
            put_row([
            put_image(open("IMG_MainPage/img_GoodsPage/delete-online.webp", 'rb').read(), width='400px', height='220px'),
            # put_text("-->"),            
            put_image(open(site, 'rb').read(), width='400px', height='220px'),
            ])            
            
                
            # put_text('\n')
            
            # Verify: input Your ID to conduct!
            inputs = input_group(
                "Really sure DELECT?",
                [input("Verify", name = "verf", placeholder = "input Your ID to conduct!")]
            )
            
            
            
            # for rows in result:
            #     stringList = ""
            #     stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
            #     # from left to right
            #     for j in range(len(rows)):                        
            #         stringList += str(rows[j])
            #         stringList += "\t|\t"                        
                        
            #     put_text(stringList)                
        
        def button_click_modifer():
            clear()
            put_row([
                put_image(open("IMG_MainPage/img_GoodsModifer/p2.jpeg", 'rb').read(), width='310px', height='180px'),
                put_image(open("IMG_MainPage/img_GoodsModifer/p1.webp", 'rb').read(), width='310px', height='180px'),            
                put_image(open("IMG_MainPage/img_GoodsModifer/p3.webp", 'rb').read(), width='310px', height='180px'),
                put_image(open("IMG_MainPage/img_GoodsModifer/p4.jpeg", 'rb').read(), width='310px', height='180px'),

            ])
            
            put_column([
            put_button(["[Exit Main]"], onclick = button_click_exit_Tomain),
            ])            
            
            inputs0 = input_group(
                "Check Goods",
                [input("Input Goods ID", name = "id", placeholder="Input ID Check!")]
            )
            
            
            checkedID = int(inputs0["id"].strip())
            
            with conn.cursor() as cursor:
                sql = f"SELECT * FROM goods WHERE goodsID = {checkedID}"   
                cursor.execute(sql)
                result = cursor.fetchall()
                            
                put_text("\t\t\t\t\t\t\t\t{} results found!".format(len(result)))
                # put_text("No\t|\tPrice\t|\tGoods Name\t|\twarehouseID")
                
                for rows in result:
                    stringList = ""
                # print(rows)
                    stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                    # print(rows[1])
                        # from left to right
                    for j in range(len(rows)):                        
                        stringList += str(rows[j])
                        stringList += "\t|\t"                        
                        
                    put_row([
                        put_text(stringList),                
                    # put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='400px', height='150px')
                    ])  
            
            import randGoods
            
            # 对应goods的标号
            answer = int(inputs0["id"][len(inputs0["id"]) - 2: len(inputs0["id"])])
            print(answer)
            
            website = randGoods.imgList[answer]
            
            put_image(open(website, 'rb').read(), width='500px', height='200px')
            
            inputs = input_group(
                "Modifer Goods",
                [
                input("Reset Goods Name", name = "name", placeholder="Reset Name"),
                input("Reset Goods Price ($)", name = "price", placeholder="Reset Price")
            ])
            
            # SQL to reset name / price
            # UPDATE goods SET goodsName = 'New Product' WHERE goodsID = 1;
            with conn.cursor() as cursor:
                
                a = int(inputs0["id"][len(inputs0["id"]) - 2: len(inputs0["id"])])
                
                a = int(str("30" + str(a)))
                
                b = inputs["name"].strip()
                c = float(inputs["price"].strip())
                
                # print("a = " + str(a))
                
                sql = f"UPDATE goods SET goodsName = '{b}', goodsPrice = {c} WHERE goodsID = {a}"  
                cursor.execute(sql)
                result = cursor.fetchall()                
                conn.commit()
            
            put_text("\t\t\t\t\t\t\t\t Modified Result: -- {}".format(datetime.datetime.now()))
            with conn.cursor() as cursor:
                sql = f"SELECT * FROM goods WHERE goodsID = {a}"  
                cursor.execute(sql)
                result = cursor.fetchall()
            
            print("result " + str(result))
            
            for rows in result:
                stringList = ""
                # print(rows)
                stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                    # print(rows[1])
                        # from left to right
                for j in range(len(rows)):                        
                    stringList += str(rows[j])
                    stringList += "\t|\t"                        
                        
                put_row([
                        put_text(stringList),                
                    ])             
            
            
                
            
        put_row([                                   
        put_button(["[Refresh]"], onclick = button_click_refresh),
        put_button(["[Orders]"], onclick = button_click_order),
        put_button(["[Add +]"], onclick = button_click_add),
        put_button(["[Cut -]"], onclick = button_click_cut),
        put_button(["[Modifer]"], onclick = button_click_modifer),
        put_button(["[Exit Main]"], onclick = button_click_exit_Tomain)
        ])

        
        put_text("\t\t\t\t\t\tDaily Recommend -- {}".format(datetime.datetime.now()))
        
        ## 每日推荐
        rand_IDbox = []
        
        start_range = 15
        end_range = 45
        count_of_numbers = 3       
         
        rand_numbox = random.sample(range(start_range, end_range + 1), count_of_numbers)
        
        for i in range(3):
            ele = "30"
            # num = random.randint(10, 50)
            ele += str(rand_numbox[i])
            ele = int(ele)
            rand_IDbox.append(ele)
            # rand_numbox.append(num)
        
        print("rand_box"+ str(rand_numbox))
        print(rand_IDbox)
        
        put_text("No\t|\tGood ID\t|\tProducts Name (detailed)\t|\tPrice ($)")
        
        with conn.cursor() as cursor:
            i1 = rand_IDbox[0]
            i2 = rand_IDbox[1]
            i3 = rand_IDbox[2]
            # i4 = rand_IDbox[3]
            sql = f"SELECT goodsID, goodsName, goodsPrice FROM goods WHERE ((goodsID = {i1}) OR (goodsID = {i2}) OR (goodsID = {i3}))"   
            cursor.execute(sql)
            result = cursor.fetchall()
        
        print(result)        
        import randGoods        
        site1 = randGoods.imgList[rand_numbox[0]]
        site2 = randGoods.imgList[rand_numbox[1]]
        site3 = randGoods.imgList[rand_numbox[2]]
        
        # 展示随机推荐产品信息
        for rows in result:
            stringList = ""
            # print(rows)
            stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
            for j in range(len(rows)):                        
                stringList += str(rows[j])
                stringList += "\t|\t"                        
                    
            put_row([
                put_text(stringList),                
                # put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='400px', height='150px')
            ])         
            # put_text(" - - - -" * 18)         
        # 展示随机推荐的产品图片
        put_row([
            put_image(open(site1, 'rb').read(), width='300px', height='150px'),
            put_text(" "),
            put_image(open(site2, 'rb').read(), width='300px', height='150px'),
            put_text(""),
            put_image(open(site3, 'rb').read(), width='300px', height='150px')
        ])            
        
        
        search_option = radio("You wanna to Check", options = ["goodsID", "goodsName", "goodsPrice"], inline = True)
        
        put_text("Search: [{}]".format(search_option) + "\t -- {}".format(datetime.datetime.now()))
        # put_button(["Exit Goods Page"], onclick = button_click_exit_goods)

        # 运用SQL查询目前最大的goodsID号
        with conn.cursor() as cursor:
            sql = f"SELECT MAX(warehouseID), MIN(warehouseID) FROM goods"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            # print("SQL Result:" + str(result))
        min_id = 0
        max_id = 0
            
        for i in result:
            max_id = i[0]
            min_id = i[1]

                        
                        
        if (search_option == "goodsID"):
            inputs = input_group(
                "Search ID",
                [input("Input Goods ID", name = "goodsID", placeholder="{}~{}".format(min_id, max_id))]                
            )
            
            goodsID = int(inputs["goodsID"].strip())    
            
            with conn.cursor() as cursor:
                sql1 = f"SELECT * FROM goods WHERE goodsID = {goodsID}"   
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
            put_text("\n")
            put_text("\t\t\t\t\t\t\t\t\t\t{} results found".format(len(result1)))
            put_text("No\t|\tGoods ID\t|\tPrices\t|\tGoods Name\t|\twarehouseID")
                                
            with conn.cursor() as cursor:
                sql1 = f"SELECT * FROM goods WHERE goodsID = {goodsID}"    
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
                for rows in result1:
                    stringList = ""
                    print(rows)
                    stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
                    for j in range(len(rows)):                        
                        stringList += str(rows[j])
                        stringList += "\t|\t"                        
                    
                    put_text(stringList)         
                    put_text(" - - - -" * 18)     
                    
                    
        if (search_option == "goodsName"):
            inputs = input_group(
                "Search Name",
                [input("Input Goods Name", name = "goodsName", placeholder="Apple AirPods Pro")]                
            )
            
            goodsName = (inputs["goodsName"].strip())    
            
            with conn.cursor() as cursor:
                sql1 = f"SELECT * FROM goods WHERE goodsName = '{goodsName}'"   
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
            put_text("\n")
            put_text("\t\t\t\t\t\t\t\t\t\t{} results found".format(len(result1)))
            put_text("No\t|\tGoods ID\t|\tPrices\t|\tGoods Name\t|\twarehouseID")
                                            
            with conn.cursor() as cursor:
                sql1 = f"SELECT * FROM goods WHERE goodsName = '{goodsName}'"    
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
                for rows in result1:
                    stringList = ""
                    print(rows)
                    stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
                    for j in range(len(rows)):                        
                        stringList += str(rows[j])
                        stringList += "\t|\t"                        
                    
                    put_text(stringList)         
                    put_text(" - - - -" * 18)          

                
        if (search_option == "goodsPrice"):
                    # 运用SQL查询目前最大的goodsID号
            with conn.cursor() as cursor:
                sql = f"SELECT MAX(warehouseID), MIN(warehouseID) FROM goods"
                cursor.execute(sql)
                result = cursor.fetchall()
            
            # print("SQL Result:" + str(result))
            min_id = 0
            max_id = 0
            
            for i in result:
                max_id = i[0]
                min_id = i[1]
            
            inputs = input_group(
                "Search Price",
                [input("Input Goods Price (min)", name = "goodsMinPrice", placeholder="{}+".format(min_id)),                
                input("Input Goods Price (max)", name = "goodsMaxPrice", placeholder="{}-".format(max_id))]  
            )
            
            goodsMinPrice = int(inputs["goodsMinPrice"].strip())                        
            goodsMaxPrice = int(inputs["goodsMaxPrice"].strip())                        
            
            with conn.cursor() as cursor:
                sql1 = f"SELECT * FROM goods WHERE ((goodsPrice < {goodsMaxPrice}) AND (goodsPrice > {goodsMinPrice})) ORDER BY goodsPrice DESC"    
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
            put_text("\n")
            put_text("\t\t\t\t\t\t\t\t\t\t{} results found".format(len(result1)))
            put_text("No\t|\tGoods ID\t|\tPrices\t|\tGoods Name\t|\twarehouseID")
            
            
            with conn.cursor() as cursor:
                sql1 = f"SELECT * FROM goods WHERE ((goodsPrice < {goodsMaxPrice}) AND (goodsPrice > {goodsMinPrice}))"    
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
                for rows in result1:
                    stringList = ""
                    print(rows)
                    stringList += "•" + str(result1.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
                    for j in range(len(rows)):                        
                        stringList += str(rows[j])
                        stringList += "\t|\t"                        
                    
                    put_text(stringList)         
                    put_text(" - - - -" * 18)                                                                                                                               
        
        pass
    
    def button_click_warehouse(a):
        clear()
        # Show the image
        put_row([
            put_image(open("IMG_MainPage/img_Warehouses/ps1.jpg", 'rb').read(), width='310px', height='220px'),                    
            put_image(open("IMG_MainPage/img_Warehouses/ps2.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_MainPage/img_Warehouses/ps3.jpeg", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_MainPage/img_Warehouses/ps4.avif", 'rb').read(), width='310px', height='220px')    
        ])
        
        def button_click_exit_Tomain():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ])
        
            put_text("\n")    
        # Shop (fake main)
            put_row([        
            put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")    
            
            # end fake Main Page    
            pass
        
        put_text("")
        put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
        
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM warehouses"
            cursor.execute(sql)
            result = cursor.fetchall()
            
        put_text("\n")
        put_text("No\t|\twarehouseID\t|\tAddress (Detailed Address Region)\t|\tCapacity\t|\tsupplyID\t|")
                    
        for rows in result:
            stringList = ""
            # print(rows)
            stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
            for j in range(len(rows)):                        
                stringList += str(rows[j])
                stringList += "\t|\t"                        
                    
            put_row([
                put_text(stringList),                
                # put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='400px', height='150px')
            ])              
        
        
                    
        pass
    
    def button_click_courier(a):
        clear()
        put_row([
            put_image(open("IMG_MainPage/img_Courier/p1.jpeg", 'rb').read(), width='310px', height='220px'),                    
            put_image(open("IMG_MainPage/img_Courier/p2.webp", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_MainPage/img_Courier/p3.webp", 'rb').read(), width='310px', height='220px'),
            put_image(open("IMG_MainPage/img_Courier/p4.jpeg", 'rb').read(), width='310px', height='220px')    
        ])
        
        def button_click_exit_Tomain():
            clear()
            put_row([
                put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='220px'),
                put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='220px'),       
            ])
        
            put_text("\n")    
        # Shop (fake main)
            put_row([        
            put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
            put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
            ])
            
            put_text("")

        # Staff
            put_row([        
                put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
                put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
            ])
            put_text("")

        # Goods
            put_row([        
                put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
                put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
            ])
            put_text("")
            
        # Suplyer    
            put_row([        
                put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
                put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
            ])
            put_text("")
            
        # Courier    
            put_row([        
                put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
                put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
                put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
            ])
            put_text("")    
            
            # end fake Main Page    
            pass
         
        put_text("\n")        
        put_button(["[Exit MainPage]"], onclick = button_click_exit_Tomain)
        
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM couriers"
            cursor.execute(sql)
            result = cursor.fetchall()
            
        put_text("\n")
        put_text("No\t|\tcourierID\t|\tcourierName\t|\tPhoneNumber\t|\tlicensePlate\t|")
                    
        for rows in result:
            stringList = ""
            # print(rows)
            stringList += "•" + str(result.index(rows) + 1) + "\t|\t"
                # print(rows[1])
                    # from left to right
            for j in range(len(rows)):                        
                stringList += str(rows[j])
                stringList += "\t|\t"                        
                    
            put_row([
                put_text(stringList),                
                # put_image(open("IMG_MainPage/img_GoodsPage/p5.avif", 'rb').read(), width='400px', height='150px')
            ])              
                        
        pass
    
    
    
    put_text("\n")
    
    # Shop (True Main)
    put_row([        
        put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
        put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
        put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
        ])
    put_text("")

    # Staff
    put_row([        
            put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
            put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
        ])
    put_text("")

    # Goods
    put_row([        
            put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
            put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
        ])
    put_text("")
        
    # Suplyer    
    put_row([        
            put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
            put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
        ])
    put_text("")
        
    # Courier    
    put_row([        
            put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
            put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
        ])
    put_text("")
                        
MainPage()    
# button_click_staff()