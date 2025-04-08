CREATE DATABASE /*!32312 IF NOT EXISTS*/`store1` /*!40100 DEFAULT CHARACTER SET latin1 */;

########################################################################################################################
use store1;
GRANT ALL PRIVILEGES ON store1.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

-- CREATE USER 'root@localhost'@'172.30.168.171' IDENTIFIED BY 'Audi139id5';
GRANT ALL PRIVILEGES ON store1.* TO 'root@localhost'@'172.30.168.171';
FLUSH PRIVILEGES; 

SHOW GRANTS FOR 'root'@'localhost';
GRANT ALL PRIVILEGES ON store1.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
########################################################################################################################

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
 goodsAmount integer,
 warehouseID integer,
    primary key (goodsID),
    foreign key (warehouseID) references warehouses(warehouseID));


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
    

create table onlineCustomer(
	onlineCustomerID integer,
    onlineCustomerName char(30),
	onlineCustomerPhone char(30),
    onlineCustonerAddress char(255),
    primary key (onlineCustomerID));    
    
    
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
    
    
create table onlineOrders (
    orderID integer,
    onlineCustomerID integer,
    orderQuantity integer,
    orderDate date,
    courierID integer,
    goodsID integer,
    primary key (orderID),
    foreign key (goodsID) references goods(goodsID),
    foreign key (onlineCustomerID) references onlineCustomer(onlineCustomerID),
    foreign key (courierID) references couriers(courierID));