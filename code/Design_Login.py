from pywebio.input import input, radio
from pywebio.input import *
from pywebio.output import put_buttons, put_text, put_image, clear
from pywebio.output import *
from pywebio import start_server
from pywebio.session import run_js
import datetime

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
    
    put_text(inputs1["shopName"])
    put_text(str(selected_country) + " / " + inputs1["City"] + " / " + inputs1["Town"] + " / " + inputs1["Street"])
    
    global input_info
    input_info = str(selected_country) + " " + inputs1["City"] + " " + inputs1["Town"] + " " + inputs1["Street"]

    # put_buttons(["Boys"], onclick = button_click)

LoginPage()    
    
