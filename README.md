# DBMS Project

## Project Overview

 1. Background
 2. Features Overview
 3. Project Development
 4. File Introduction
 5. Design Diagram
 6. Code Implementation
 7. Function Display Demo
---

## 1. BackGround
- **Manage Your Store**: More and more graduates wants to make *Self-employment*, and the need for building up a **simple** and **conductor-friendly** operating management system. Thus, this project wanna to build up an easy-conduct  system help to manage both **shops**, **staffs**, **goods**, **orders**, **warehouses**, **courier**

- **Object**:  People who use Store Management System

- **Aiming**: Make it simple and easy-conduct !

## 2. Features Overview

 1. Register & Login
	 - 1.1 **Design Yourself** 
	 - 1.2 **DIY Shops Info**
 2. Shop Management
	 - 2.1 View
	 - 2.2  **Search**
 3. Staffs Management View & Modify
	 - 3.1 View
		 - Overview ALL
		 - **Filter View** (fitting AVG)
		 - Search		 
	 - 3.2 Edit 
		 - Add & Drop
		 - Modify Staff Info
 4. Goods Managerment
	 - 4.1 **Daily Recommend**
	 - 4.2 **Auto Refresh Recommend** 
	 - 4.3 **Add**
	 - 4.4 Drop
	 - 4.5 Modify
	 - 4.6 **Search**

5. Warehouse Management
	- View

6.  Courier Management
	- View


## 3. Project Development
- Coding: Python (3.11.8) + MySQL
- Output: Console + **Pyweb**
- IDE: Visual Studio Code (Version 1.31.1)
- Data: DataBase **pre-generated** By Tools

## 4. File Introduction

 - *Connection_xxx.py*: Cheking **MySQL Connection** success or not?
 - *Design_xxx.py*: **Design Page** and rough Function
 - *ImportPackage_.py*:  Import Package
 - **Version2_final.py**: **Final product for project (most perfect one!)**

## 5. Design Diagram
ER-Diagram:
![ER-Diagram](/imgs/2024-05-15/VaWrI70MsckLpA4d.jpeg)


## 6. Code Implementation
### 6.1 SQL Connection:
```python.3.11
# Connection MySQL
conn = pymysql.connect(
host = '172.30.168.171', # Host name, default is 127.0.0.1
user = 'root@localhost', # Username
passwd = 'Audi139id5', # Password
port = 3306, # Port, default is 3306
db = 'store1', # Database name
charset = 'utf8', # Character encoding)
```
### 6.2 Packages:
```python.3.11
# Package Using Pyweb
from pywebio.input import input, radio
from pywebio.input import *
from pywebio.output import put_buttons, put_text, put_image, clear
from pywebio.output import *
from pywebio import start_server
from pywebio.session import run_js
from pywebio.input import checkbox
from pywebio.output import put_text, put_html
import datetime
import time
import pymysql
```
### 6.3 SQL Tables
```sql
USE store1;
GRANT ALL PRIVILEGES ON store1.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

create table suppliers(
 supplierID integer,
 supplierPhone char(30),
 supplierAddress char(255),
 primary key (supplierID));
 
create table warehouses(
	warehouseID integer,
    warehouseAddress char(255),
    WarehouseCapacity integer,
    supplierID integer,
    primary key (warehouseID),
    foreign key (supplierID) references suppliers(supplierID));

create table goods(
 goodsID integer,
 goodsPrice double,
 goodsName char(50),
 -- goodsAmount integer,
 warehouseID integer,
    primary key (goodsID),
    foreign key (warehouseID) references warehouses(warehouseID));

create table websiteBox(
webNumber INTEGER,
website VARCHAR(100));

create table shops(
	shopID integer,
    shopName char(30),
    shopAddress char(255),
    primary key (shopID));   

create table staff (
    staffID integer,
    shopID integer,
    staffName char(30),
    salary double,
    gender char(10),
    staffPhone char(30),
    primary key (staffID),
    foreign key(shopID) references shops(shopID));

create table customer(
 customerID integer,
 customerPhone char(20),
 customerName char(30),
 primary key (customerID));

create table orders (
    orderID integer,
    customerID integer,
    orderQuantity integer,
    orderDate date,
    goodsID integer,
    shopID integer,
    staffID integer,
    primary key (orderID),
    foreign key (goodsID) references goods(goodsID),
    foreign key (shopID) references shops(shopID),
    foreign key (staffID) references staff(staffID),
    foreign key (customerID) references customer(customerID));

create table couriers(
    courierID integer,
    courierName char(30),
    courierPhone char(30),
    licensePlate char(30),
    primary key (courierID));             
```

### 6.4 SQL  Implement Example (Partly!)
1. **INSERT**: add data into database
```python.3.11
# add website data into database
with conn.cursor() as cursor:
for num, i in zip( range(len(randGoods.imgList) + 1),randGoods.imgList):
	ele1 = num
	ele2 = i
	sql = f"INSERT INTO websiteBox (webNumber, website) VALUES ({ele1}, '{ele2}');"
	cursor.execute(sql)
	conn.commit()
	
# add loginInfo into database
with conn.cursor() as cursor:
	sql = f"INSERT INTO loginInfo (loginID, loginPassword) VALUES ({loginID}, {loginPassword})"
	cursor.execute(sql)
	conn.commit()
	result = cursor.fetchall()	
```

2. **Divide**: divide different salary into certain range
```python
# Divide salary ranges
rangeList = ['4500 ~ 5000', '5000 ~ 5500', '5500 ~ 6000', '6000 ~ 6500', '6500 ~ 7000', '7000 ~ 7500', '7500 ~ 8000', '8000 ~10000', 'More 10000+']
countList = []

with conn.cursor() as cursor:
	rangeList = ['4500 ~ 5000', '5000 ~ 5500', '5500 ~ 6000', '6000 ~ 6500', '6500 ~ 7000', '7000 ~ 7500', '7500 ~ 8000', '8000 ~10000', 'More 10000+']
	countList = []
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
```

3. **Compute**: SQL to compute values and **update values** in real time
(like: *recommend user* the next input should be what?)
```python.3.11
# compute next warehouseID, and it's updates in real time
with conn.cursor() as cursor:
	sql = f"SELECT MAX(warehouseID), MIN(warehouseID), MAX(goodsID), MIN(goodsID) FROM goods"
	cursor.execute(sql)
	result = cursor.fetchall()

# compute range and it's updates in real time
with conn.cursor() as cursor:
	sql = f"SELECT MAX(goodsID), MIN(goodsID) FROM goods"
	cursor.execute(sql)
	result = cursor.fetchall()	
	min_id = 0
	max_id = 0

for i in result:
	max_id = i[0]
	min_id = i[1]

# compute range for warehouse, know created continuous list number
with conn.cursor() as cursor:
	sql = f"SELECT MAX(warehouseID), MIN(warehouseID), MAX(goodsID), MIN(goodsID) FROM goods"
	cursor.execute(sql)
	result = cursor.fetchall()
	min_id1 = 0
	max_id1 = 0
	max_id2 = 0
	
for i in result:
	max_id1 = i[0]
	min_id1 = i[1]
	max_id2 = i[2]
```
4. **Search & Filter**: search certain information then filter
```python.3.11
# filter out certain shop with similar name structure
with conn.cursor() as cursor:
	shopAddress = inputs['searchCop'].strip()
	sql1 = f"SELECT * FROM shops WHERE shopName LIKE '%{shopAddress}%'"
	cursor.execute(sql1)
	result1 = cursor.fetchall()

# filter out AVG
with conn.cursor() as cursor:
	sql = f"SELECT * FROM staff WHERE salary < {avg_value} ORDER BY salary DESC"
	cursor.execute(sql)
	result = cursor.fetchall()
```

## 7. Display Demo

**a> RegisterPage**:  
- Input reminder(tips)
- Reverify Password
- Login Data Storage (stored in MySQL Database)
![Register](/imgs/2024-05-15/4BlIAZyPt8oX3L9e.png)

---
**b> LoginPage**
- After finishing RegisterPage, comes to Shop Design Page
- Input Shop Design
- DIY Shops Info
![LoginPage](/imgs/2024-05-15/OskpCaFOpUdD4jDZ.png)

---

**c> MainPage**
- After finishing all design Part.. 
- Comes to Main Page for Functions:
	- Shops
	- Staffs
	- Goods
	- Warehouse
	- Courier

![MainPage](/imgs/2024-05-15/BvyoM5XuWy96nBS6.png)

---
**d1> Shops**

*1. ShopPage:*
- Main Shop Page **list** first 5 main shops
![shopPage](/imgs/2024-05-15/SUm2gX3tg6tEP1SR.png)

*2. Search Part:*
- Search information & type **according to Your choice**
![输入图片说明](/imgs/2024-05-15/yHYBFvv6meNz85rA.jpeg)

*3. Search Result*
- search detailed info for Shop You wanna to search!
![result](/imgs/2024-05-16/lWwxOyxmyygVuQA1.png)

---

**d2 Staffs**

*1. Staff Page*
-  View: To view overall info about Staffs
-  Edit: To modify info for Staffs
	- Salary modify
	- Store ownership
	- Others...
![staffPage](/imgs/2024-05-16/TYkTlWf5GqjqCYF1.png)

*2. View Page*
- list first 5 staffs
- Click **[View More]** button to check all staffs info 
![viewPage](/imgs/2024-05-16/9YXFuVUzuycWhKBs.png)

*3. Distribution*
![AVG](/imgs/2024-05-16/LzbTKkXdX3g2Ebqz.png)

*4. Searching Part*
- Searching according to your choice
![search](/imgs/2024-05-16/qCKCFsunp9HXjUNg.jpeg)

*5. Result Part*
- Inputs [Kento Momota] ——> Output: **Names similar** parts will be shown
- not case sensitive !
![staffSearch](/imgs/2024-05-16/xBUrx8MXiULFM41H.png)

---

**d3> Goods**

*1. Goods Page*
- [Refresh] ——> refresh **update daily Auto-Recommend**
- Search Box: **Search anything U like for Goods**
![GoodsPage](/imgs/2024-05-16/Vo8urnQSObEDTR89.jpeg)
---
*2. Add Goods*
- Input Goods Information
- **[Browse]** ——> Upload an Image for your products
- SQL work, Saving data you input
![inputs](/imgs/2024-05-16/egjit4Mg8vTanr1x.jpeg)

---

*3. Check Savings*
- p1: INSERT INTO & **Saving Goods Info**
- p2: INSERT INTO & **Saving IMG file Path**
	- Prepare for next time **directly implements**
![datasavings](/imgs/2024-05-16/1y9aBpcRtKmtRmet.jpeg)

- p3: Saving IMG file Path into File
![savings](/imgs/2024-05-16/jOY48ztKNj2ixh2E.jpeg)
---

*4. Orders Part*
- Order List: Show all Orders list, *Using them for copy*
- Then, Jump to certain Page...
	- Copy "OrderID" ——> check detailed Order info **(Order Page)**
	- Copy "CustsID" ——> check detailed Customers info **(Customers Page)**
	- Copy "GoodsID" ——> check detailed Goods info **(Goods Page)**
	- Copy "ShopsID" ——> check detailed Shops info **(Shops Page)**
	- Copy "StaffsID" ——> check detailed Staffs info **(Staffs Page)**
![orders](/imgs/2024-05-16/dLp0vblI1tsbATER.jpeg)

---

**d4> Warehouse Page**
- View basic info for Warehouse
	- ID / Address / Storage / supplyID...
![warehouse](/imgs/2024-05-16/7E5yrr6wPKes7YkF.png)
---

**d5> Courier**
- View basic info for Courier
	- ID / Name / Phone / licensePlate...
![courier](/imgs/2024-05-16/aXKLpRVH7QCM1Le0.png)

---



