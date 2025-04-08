import pymysql
from pywebio.input import input, radio
from pywebio.input import *
from pywebio.output import put_buttons, put_text, put_image, clear
from pywebio.output import *
from pywebio import start_server
from pywebio.session import run_js
import time
import datetime
import random

conn = pymysql.connect(
    host='172.30.168.171',  # 连接名称，默认127.0.0.1
    user='root@localhost',  # 用户名
    passwd='Audi139id5',  # 密码
    port=3306,  # 端口，默认为3306
    db='store1',  # 数据库名称
    charset='utf8',  # 字符编码
)

def RegisterPage():
        put_image(open("IMG_LoginPage/180387505.jpg", 'rb').read(), width='1200px', height='350px')                
            
        put_text("\n");
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
        global inputs0
    
        inputs0 = input_group(
       "\tRegister page", # page Name
       [
           # input("Input Your Age", name = "age"),
           input("Please Input City", name = "city"),                                 
           input("Please Input Account\n", name = "account"),
           input("Please Input Password", type = PASSWORD, name = "password"),
           input("Please Verify Password", type = PASSWORD, name = "verfPassword")
       ]
       )
        
        # time.sleep(0.3)
        clear()
        put_image(open("IMG_LoginPage/180387505.jpg", 'rb').read(), width='1200px', height='350px')
        times = 1
        
        while (True):
            if (inputs0["password"] != inputs0["verfPassword"]):                                
                inputs0 = input_group(
                    "Reput Page",
                    [
                    input("Please Input Password", type = PASSWORD, name = "password"),
                    input("Please Verify Password", type = PASSWORD, name = "verfPassword")
                    ]
                )
                
                if (inputs0["password"] != inputs0["verfPassword"]):
                    put_text("Error x{}\t—— {}".format(times, datetime.datetime.now()))
                    times += 1
                # clear()
            
            else:
                put_text("\t\t\t\t\t\t\t\t\t\t\tCorrect !!!")
                time.sleep(1.5)                
                clear()
                break
def LoginPage():
    
    def button_click_loc(a):
        import geocoder
        # 获取自己所在地区的位置信息
        location = geocoder.ip('me')
        if location.ok:
            put_text("Yours: Latitude {}ºN \t Longitude {}ºE (China Mainland)\t-- {}".format(location.lat, location.lng, datetime.datetime.now()))
    
    # (10001, 'ElectroMart', '123 Main Street, Anytown, USA'),
    put_row([
        put_image(open("IMG_LoginPage/Photo1.jpeg", 'rb').read(), width='310px', height='290px'),
        put_image(open("IMG_LoginPage/Photo4.jpeg", 'rb').read(), width='310px', height='290px'),
        put_image(open("IMG_LoginPage/Photo2.webp", 'rb').read(), width='310px', height='290px'),
        put_image(open("IMG_LoginPage/Photo3.jpeg", 'rb').read(), width='310px', height='290px'),       
    ])
    
    put_text("")
    put_buttons(["Location"], onclick = button_click_loc)
    
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

    global selected_country
    selected_country = select("Select Region:", country_options)
    
    global inputs1    
    inputs1 = input_group(
        "Design Your Shop",
        [
        input("Please Input ShopName:", name = "shopName"),
        input("•1  Input City:", name = "City"),
        input("•2  Input Town:", name = "Town"),
        input("•3  Input Street:", name = "Street")        
        ]
        )
    
    put_text(inputs1["shopName"])
    put_text(str(selected_country) + " / " + inputs1["City"] + " / " + inputs1["Town"] + " / " + inputs1["Street"])
    
    global input_info
    input_info = str(selected_country) + " " + inputs1["City"] + " " + inputs1["Town"] + " " + inputs1["Street"]


try:
    with conn.cursor() as cursor:

        LoginPage()
        # 插入上商店的信息
        
        shopID = random.randint(10050, 19999)
        shopName = inputs1["shopName"]
                
        shopAddress = str(inputs1["City"] + "," + inputs1["Town"] + "," + inputs1["Street"] + str(selected_country))
        
        # shopAddress = shopAddress.decode('utf-8')
        
        
        sql = f"INSERT INTO shops(shopID, shopName, shopAddress) VALUES ({shopID}, '{shopName}', '{shopAddress}')"
        cursor.execute(sql)
        conn.commit()
                            
    #        # input("Input Your Age", name = "age"),
    #        input("Please Input staffID", name = "staffID"),                      
    #        input("Please Register shopID\n", name="shopID"),
    #        input("Please Input staffName\n", name = "staffName"),
    #        input("Please Input salary\n", name = "salary"),
    #        input("Please Input gender\n", name = "gender"),
    #        input("Please Input phone\n", name = "staffPhone")
    #     ]
    #     )
    # # print(inputs1)
    # # print(inputs1["city"]) // OK
    
    # # INSERT INTO goods (goodsID, goodsPrice, goodsName, warehouseID) VALUES
    
    #     id1 = inputs9["staffID"]
    #     id2 = inputs9["shopID"]
    #     name1 = inputs9["staffName"]
    #     sa = inputs9["salary"]
    #     ge = inputs9["gender"]
    #     ph = inputs9["staffPhone"]    
        
    #     # intert self-input data
    #     sql = f"INSERT INTO staff (staffID, shopID, staffName, salary, gender, staffPhone) \
    #             VALUES ({id1}, {id2}, '{name1}', {sa}, '{ge}', '{ph}')"        
    #     cursor.execute(sql)
    #     result = cursor.fetchall()

    #     # check data
    #     sql1 = f"SELECT * FROM staff"    
    #     cursor.execute(sql1)
    #     result1 = cursor.fetchall()
        # for rows in result1:
        #     stringList = ""
        #     print(rows)
        #     stringList += str(result1.index(rows) + 1) + ">\t"
        # # print(rows[1])
        #     # from left to right
        #     for j in range(len(rows)):
        #         # pass
        #         # print(j)
                
        #         stringList += str(rows[j])
        #         stringList += "\t"
                
            
        #     put_text(stringList)         
        #     put_text("_ _ _" * 17)
        
        # conn.commit()
        
                
finally:
    # 关闭连接    
    # for i in result1:
    #         print(i)   
    conn.close() 
# for i in result:
#     print(i)    