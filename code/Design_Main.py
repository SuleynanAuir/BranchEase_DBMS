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
    host='172.30.168.171',  # Host name, default is 127.0.0.1
    user='root@localhost',  # Username
    passwd='Audi139id5',  # Password
    port=3306,  # Port, default is 3306
    db='store1',  # Database name
    charset='utf8',  # Character encoding
)


def MainPage():
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
        # Add Anything U like
        pass

    
    def button_click_shop(a):
        # Add Anything U like        
        pass
    
    def button_click_staff(a):
        # Add Anything U like        
        pass    
    
    def button_click_goods(a):
        # Add Anything U like        
        pass    
    
    def button_click_warehouse(a):
        # Add Anything U like        
        pass    
    
    def button_click_courier(a):
        # Add Anything U like        
        pass  
        
    # MainPage Design
    put_row([        
        put_image(open("IMG_MainPage/Shop.jpeg", 'rb').read(), width='150px', height='60px'),
        put_text("\t\t\t[Shops]\nOverview Shopping Centre Basic info\t"),
        put_buttons(["Shops", "View", "+", "-"], onclick = button_click_shop)
        ])
    put_text("")


    put_row([        
            put_image(open("IMG_MainPage/Staff.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Staffs]\nOverview Staff Labor info & Salary\t"),
            put_buttons(["Staffs", "View", "+", "-"], onclick = button_click_staff)
        ])
    put_text("")


    put_row([        
            put_image(open("IMG_MainPage/Goods.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Goods]\nOverview Goods' types / price / stock\t"),
            put_buttons(["Goods", "View", "+", "-"], onclick = button_click_goods)
        ])
    put_text("")
        

    put_row([        
            put_image(open("IMG_MainPage/Suplyer.png", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Suplyer]\nOverview Suplyer condition / stock\t"),
            put_buttons(["Supply", "View", "+", "-"], onclick = button_click_warehouse)
        ])
    put_text("")
    

    put_row([        
            put_image(open("IMG_MainPage/Courier.jpeg", 'rb').read(), width='150px', height='60px'),
            put_text("\t\t\t[Courier]\nOverview Conveying situation / period\t"),
            put_buttons(["Manage", "View", "+", "-"], onclick = button_click_courier)
        ])
    put_text("")
    
        
MainPage()    
# button_click_staff()
