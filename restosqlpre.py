import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="devdat", charset="utf8") #change password and username accordingly
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS resto")
cursor.execute("USE resto")

create_table_menu = '''CREATE TABLE IF NOT EXISTS menu (
    id INT  PRIMARY KEY,
    ITEM VARCHAR(60),
    COST INT);'''


create_table_revenue = '''CREATE TABLE IF NOT EXISTS revenue (
    date DATE,
    revenue INT,
    Orders INT,
    weekday varchar(20));'''

pre_menu='''insert into menu(id, ITEM, COST)  values
(1,'Tomato Soup', 50),
(2,'Veg clear soup', 55),
(3,'Vegetable Hot N Sour Soup',55),
(4,'Vegetable Manchow Soup', 60),
(5,'Paneer Tikka',  70),
(6,'Paneer Manchurian', 70),
(7,'Veg Nuggets', 75),
(8,'Mushroom Salt and Pepper', 70),
(9,'Veg Salad',100),
(10,'Veg Pasta Salad',110);'''
try:
    cursor.execute(create_table_menu)
    cursor.execute(create_table_revenue)
    cursor.execute(pre_menu)
    print("Database and tables created successfully!")
except:
    "Something went wrong"

conn.commit()
conn.close()

