
import sqlite3
import qrcode

cart=[]

def read_from_database():
    global connection, my_cursor, PRODUCTS
    connection = sqlite3.connect("store.db")
    my_cursor = connection.cursor()
    PRODUCTS = my_cursor.execute("SELECT * FROM PRODUCTS").fetchall()

def show_menu():
    print("0-QRcode")
    print("1-add")
    print("2-Edit")
    print("3-Remove")
    print("4-search")
    print("5-show list")
    print("6-buy")
    print("7-Exit")

def add():
    name=input("enter name: ")
    price=int(input("enter price: "))
    count=int(input("enter count: "))
    my_cursor.execute(f"INSERT INTO PRODUCTS(name, price, count) VALUES('{name}', '{price}', '{count}')")
    connection.commit()
    print("product was inserted successfully")

def edit():
    code=int(input("enter product code: "))
    for product in PRODUCTS:
        if code==product[0]:
            print("code=", product[0],", name=", product[1],", price=", product[2],", count=", product[3])
            name=input("enter new name to edit: ")
            if name!='':
                my_cursor.execute(f"UPDATE products SET name='{name}' WHERE code='{code}'")

            price=input("enter new price to edit: ")
            if price!='':
                my_cursor.execute(f"UPDATE products SET price= '{price}' WHERE code= '{code}'")

            count=input("enter new count to edit: ")
            if count!='':
                my_cursor.execute("UPDATE products SET count='{count}' WHERE code= '{code}'")
            
            connection.commit()

            print("The product edited successfully")
            break

    else:
        print("your product code wasn't found!")
    
def remove():
    code=int(input("enter product code:"))

    for product in PRODUCTS:
        if product[0]==code:
            my_cursor.execute(f"DELETE FROM products WHERE code='{code}'")
            connection.commit()
            print("your chosen product had been successfully deleted!")
            break
    else:
     print("your product code was not found!")


def search():
    user_input=input("type product's code or name")
    for data in my_cursor.execute(f"SELECT * FROM products WHERE code={user_input} or name={user_input}"):
        print(data)

def show_list():
    print("code\t\tname\tprice\tcount")
    for data in my_cursor.execute(f"SELECT * FROM products"):
        print(data)

def buy():
  
    while True:
        product_code=input("enter your desired product code or enter exit to quit:")
        if product_code=="exit":
            break
        for product in PRODUCTS:
            if product[0]==int(product_code):
                product_number=int(input("enter the number of product you want: "))
                if int(product_number)<= product[3]:
                       product_name=product[1]
                       product_price=product[2]
                       product_count=product_number
                       cart_item=(product_code, product_name, product_price, product_count)
                       cart.append(cart_item)
                       my_cursor.execute(f"UPDATE products SET count= '{product[3]- product_number}' WHERE code='{product_code}'")
                       connection.commit()
                else:
                    print("insufficient inventory!")
                break
        else:
            print("your desired product doesnt exist!")

    print("===================================================")
    total_cost=0
    print("name \t\t\t\t\t price \t\t\t\t\t count")
    for product in cart:
        print(product[1], "\t\t", product[2],"\t\t", product[3])
        total_cost+=product[2]* product[3]
    print("===================================================")
    print("Total cost:" , total_cost , "\n")
    print(" Thank you for your shopping!  \n")

def make_qrcode():
    product_code=input("enter your product code to generate QRcode: ")
    for product in PRODUCTS:
        if product[0]==product_code:
            q=qrcode.make("code: " + str(product[0])+ "\n" + "name: " + product[1] + "\n" + "price: " + str(product[2]))
            q.save("product data to qrcode.png")
            print("QRcode was successully made!")
            break
    else:
        print("your product code was not found!")

print("welcome to my store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice=int(input("enter your choice: "))

    if choice==0:
        make_qrcode()
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:  
        buy()
    elif choice==7:
        connection.commit()
        exit(0)

    else:
        print("Incorrect input(mesle adam vared kon!)")