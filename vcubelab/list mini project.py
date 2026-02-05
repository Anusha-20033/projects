import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Smile@666",
    database="fruit_shop"
)
cursor = db.cursor()



def shop_add_new_fruit():
    fruit = input("Enter NEW fruit name: ").lower()

    cursor.execute(
        "SELECT id FROM fruits WHERE name=%s",
        (fruit,)
    )
    if cursor.fetchone():
        print("Fruit already exists! Use Update Stock option.")
        return

    qty = int(input("Enter opening stock: "))
    cp = int(input("Enter cost price: "))
    sp = int(input("Enter selling price: "))
    profit = sp - cp

    cursor.execute(
        """
        INSERT INTO fruits (name, stock, cost_price, selling_price, profit)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (fruit, qty, cp, sp, profit)
    )
    db.commit()

    print("New fruit added successfully!")

def shop_update_stock():
    fruit = input("Enter fruit name to update stock: ").lower()

    cursor.execute(
        "SELECT stock FROM fruits WHERE name=%s",
        (fruit,)
    )
    data = cursor.fetchone()

    if not data:
        print("Fruit not found! Add it first.")
        return

    print(f"Current stock: {data[0]}")
    qty = int(input("Enter quantity to ADD: "))

    if qty <= 0:
        print("Quantity must be positive!")
        return

    cursor.execute(
        "UPDATE fruits SET stock = stock + %s WHERE name=%s",
        (qty, fruit)
    )
    db.commit()

    print("Stock updated successfully!")





def shop_remove_fruit():
    fruit = input("Enter fruit name to remove: ").lower()

    cursor.execute(
        "SELECT name FROM fruits WHERE name=%s",
        (fruit,)
    )
    data = cursor.fetchone()

    if not data:
        print("Fruit not found!")
        return

    cursor.execute(
        "DELETE FROM fruits WHERE name=%s",
        (fruit,)
    )
    db.commit()

    print(f"{fruit.title()} removed from store.")



def shop_view_fruits():
    print("\n--- Shopkeeper: Store Fruits ---")

    cursor.execute("SELECT name, stock, cost_price, selling_price, profit FROM fruits")
    data = cursor.fetchall()

    if not data:
        print("No fruits available!")
        return

    for i, row in enumerate(data, start=1):
        print(f"{i}. {row[0].title()} | Stock: {row[1]} | CP: {row[2]} | SP: {row[3]} | Profit: {row[4]}")


def add_to_cart():
    print("\n--- Add Fruit to Cart ---")
    fruit = input("Enter fruit name: ").lower()

    
    cursor.execute(
        "SELECT stock, selling_price, profit FROM fruits WHERE name=%s",
        (fruit,)
    )
    data = cursor.fetchone()

    if not data:
        print("Fruit not available!")
        return

    stock, sp, profit = data

    if stock == 0:
        print("Out of stock!")
        return

    qty = int(input(f"Enter quantity (Available {stock}): "))

    if qty > stock:
        print("Not enough stock!")
        return

    total_price = sp * qty
    total_profit = profit * qty

    # 🔍 check if fruit already exists in cart
    cursor.execute(
        "SELECT quantity FROM cart WHERE fruit_name=%s",
        (fruit,)
    )
    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE cart
            SET quantity = quantity + %s,
                total_price = total_price + %s,
                total_profit = total_profit + %s
            WHERE fruit_name = %s
            """,
            (qty, total_price, total_profit, fruit)
        )
    else:
    
        cursor.execute(
            "INSERT INTO cart (fruit_name, quantity, total_price, total_profit) VALUES (%s,%s,%s,%s)",
            (fruit, qty, total_price, total_profit)
        )

    cursor.execute(
        "UPDATE fruits SET stock = stock - %s WHERE name = %s",
        (qty, fruit)
    )

    db.commit()
    print(f"{fruit.title()} added to cart!")




def remove_from_cart():
    fruit = input("Enter fruit name to remove: ").lower()

    cursor.execute(
        "SELECT quantity FROM cart WHERE fruit_name=%s",
        (fruit,)
    )
    data = cursor.fetchone()

    if not data:
        print("Fruit not in cart!")
        return

    qty = data[0]


    cursor.execute(
        "UPDATE fruits SET stock = stock + %s WHERE name = %s",
        (qty, fruit)
    )

    cursor.execute(
        "DELETE FROM cart WHERE fruit_name=%s",
        (fruit,)
    )

    db.commit()
    print("Removed from cart!")



def view_cart():
    print("\n--- Your Cart ---")
    cursor.execute("SELECT fruit_name, quantity, total_price FROM cart")
    items = cursor.fetchall()

    if not items:
        print("Cart is empty!")
        return

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item[0].title()} | Qty: {item[1]} | Price: ₹{item[2]}")



def buy_now(customer_name, customer_phone):

    cursor.execute("SELECT * FROM cart WHERE status='IN_CART'")
    items = cursor.fetchall()

    if not items:
        print("Cart empty!")
        return

    cursor.execute(
        "INSERT INTO customers (name, phone) VALUES (%s,%s)",
        (customer_name, customer_phone)
    )
    db.commit()
    customer_id = cursor.lastrowid
    total_bill = sum(i[3] for i in items)
    total_profit = sum(i[4] for i in items)
    print("\n========== BILL ==========")
    print(f"Customer Name : {customer_name}")
    print(f"Phone Number  : {customer_phone}")
    print("\nItems:")

    for item in items:
        print(f"{item[1].title()} x {item[2]} = ₹{item[3]}")

    print("---------------------------")
    print(f"TOTAL BILL   : ₹{total_bill}")
    print(f"TOTAL PROFIT : ₹{total_profit}")
    print("===========================")

    cursor.execute("""
        UPDATE cart
        SET customer_id=%s,
            status='PURCHASED',
            bill_date=NOW()
        WHERE status='IN_CART'
    """, (customer_id,))

    db.commit()
    print("Purchase saved successfully!")



def shopkeeper_menu():
    while True:
        print("\n====== SHOPKEEPER MENU ======")
        print("1. Add Fruit")
        print("2. Remove Fruit")
        print("3. View Fruits")
        print("4. update stock")
        print("5. Back to main menu")
        ch = input("Enter choice: ")
        if ch == '1':
            shop_add_new_fruit()
        elif ch == '2':
            shop_remove_fruit()
        elif ch == '3':
            shop_view_fruits()
        elif ch=='4':
            shop_update_stock()
        elif ch=='5':
            break
        else:
            print("Invalid option!")

def customer_menu():
    name = input("Enter your name: ")
    phone = input("Enter phone number: ")

    while True:
        print("\n====== CUSTOMER MENU ======")
        print("1. Add to Cart")
        print("2. Remove from Cart")
        print("3. View Cart")
        print("4. Buy Now")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == '1':
            add_to_cart()
        elif ch == '2':
            remove_from_cart()
        elif ch == '3':
            view_cart()
        elif ch == '4':
            buy_now(name, phone)
        elif ch == '5':
            break
        else:
            print("Invalid option!")




while True:
    print("\n========== MAIN MENU ==========")
    print("1. Shopkeeper")
    print("2. Customer")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        shopkeeper_menu()
    elif choice == '2':
        customer_menu()
    elif choice == '3':
        print("\nThank you for shopping!")
        break
    else:
        print("Invalid option!")
