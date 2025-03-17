import datetime
import pandas as pd

products = {}
exit = False
customers = {}
sales = {}


def menu():
    """ This is the main function named as menu to call all the other functions """
    exit = False
    while exit == False:
        inp = int(input(
            "Enter:\n"
            "1  - Add Product\n"
            "2  - Update Product\n"
            "3  - Remove Product\n"
            "4  - Get Product Details\n"
            "5  - List Products\n"
            "6  - Create Sale\n"
            "7  - Get Sales History\n"
            "8  - Identify Low Stock Items\n"
            "9  - Calculate Revenue\n"
            "10 - Calculate Average Transaction\n"
            "11 - Identify Best Selling products\n"
            "12 - Exit\n"
            "Your choice: "
        ))
        if inp == 1:
            add_product()
        elif inp == 2:
            update_product()
        elif inp == 3:
            remove_product()
        elif inp == 4:
            get_product()
        elif inp == 5:
            list_products()
        elif inp == 6:
            create_sale()
        elif inp == 7:
            get_sales_history()
        elif inp == 8:
            identify_low_stock_items()
        elif inp == 9:
            calculate_revenue()
        elif inp == 10:
            calcaulate_average_transaction()
        elif inp == 11:
            identify_best_selling_products()
        elif inp == 12:
            print('Program exit')
            exit = True


def add_product():
    """ Function to add the product in the product dictionary """
    p_id = (input('enter product id'))
    p_name = input("enter product name")
    p_category = input("enter product category")
    p_price = int(input('enter product price'))
    p_quantity = int(input('enter product quantity'))
    products[p_id] = {'name': p_name, 'category': p_category, 'price': p_price, 'quantity': p_quantity}


def update_product():
    """ Function to Update the product field by specific key"""
    id_ = input('enter product id:')
    if id_ in products:
        field = input('enter which field you want to update')
        if field == 'name':
            updated_name = input('Enter updated name')
            products[id_][field] == updated_name
        if field == 'category':
            updated_category = input('Enter updated category')
            products[id_][field] == updated_category
        if field == 'price':
            updated_price = input('Enter updated price')
            products[id_][category] == updated_price
        if field == 'quantity':
            updated_quantity = input('Enter updated quantity')
            products[id_][field] == updated_quantity
        else:
            print('incorrect field')
    else:
        print('incorrect product id')
        print("________________________________________________________")


def remove_product():
    id_ = (input('enter product id:'))
    if id_ in products:
        products.pop(id_)


def get_product():
    """Function to get the production information"""
    p_id = input("Enter product ID: ")
    if p_id in products:
        print(products[p_id])
    else:
        print("Product not found.")


def list_products(sort_by="name"):
    """Function to list all the products available"""
    prod = sorted(products.items(), key=lambda x: x[1][sort_by])
    print(prod)


def create_sale():
    """ Function to create a sale from the products"""
    amount = 0
    exit = False
    while exit == False:
        c_id = input('enter customer id or press 1 for exit:')
        if c_id == '1':
            exit = True
        if c_id not in customers:
            name = input('enter customer name')
            contact = input('enter customer contact')
            customers[c_id] = {'name': name, 'contact': contact, 'purchase_history': []}
        p_id = input('Enter product id')
        quantity = int(input('Enter the quantity'))
        if p_id not in products or products[p_id]['quantity'] < quantity:
            print('Incorrect product id or quantity you are asking is not available')
            continue
        else:
            products[p_id]['quantity'] -= quantity
            amount = quantity * products[p_id]['price']
        transaction_id = (len(sales) + 1)
        sales[transaction_id] = {"transaction_date": datetime.datetime.today(), 'product_id': p_id,
                                 "quantity": quantity, "total_amount": amount}
        customers[c_id]['purchase_history'].append(transaction_id)


def get_sales_history():
    """ Function to find the sales between specific dates"""
    st_date = pd.to_datetime(input("enter start date"))
    end_date = pd.to_datetime(input("enter end date"))
    for key, value in sales.items():
        if st_date < value['transaction_date'] and end_date > value['transaction_date']:
            print(f"sales history: date = {value['transaction_date']}, total amount = {value['total_amount']}")
        else:
            print('no sales between these dates')


def identify_low_stock_items():
    threshold = int(input("Enter stock threshold: "))
    low_stock = {}

    for p_id in products:
        if products[p_id]['quantity'] < threshold:
            low_stock[p_id] = products[p_id]
    print(f"Low Stock Products: {low_stock}")


def calculate_revenue():
    revenue = 0
    for sale_id, sale_details in sales.items():
        revenue += sale_details['total_amount']
    print(f'total revenue generated till now is {revenue}$')


def calcaulate_average_transaction():
    total_sales = 0
    sum_amount = 0

    for key, value in sales.items():
        total_sales += 1
        sum_amount += value['total_amount']
    average_transaction = sum_amount // total_sales
    print(f'average transaction is {average_transaction}')


def identify_best_selling_products():
    best_products = {}
    for i in products.keys():
        total = 0
        for sale_id, sale_details in sales.items():
            if sale_details['product_id'] == i:
                total += sale_details['total_amount']
        best_products[i] = total
    print(sorted(best_products.items(), key=lambda x: x[1], reverse=True))



menu()