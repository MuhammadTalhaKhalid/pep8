Sample data for testing:
products = {
    "P001": {"name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 10},
    "P002": {"name": "Smartphone", "category": "Electronics", "price": 800, "quantity": 15},
    "P003": {"name": "Tablet", "category": "Electronics", "price": 500, "quantity": 20},
    "P004": {"name": "Headphones", "category": "Accessories", "price": 100, "quantity": 30},
    "P005": {"name": "Keyboard", "category": "Accessories", "price": 50, "quantity": 25}
}

customers = {
    "C001": {"name": "Alice", "contact": "123-456-7890", "purchase_history": []},
    "C002": {"name": "Bob", "contact": "987-654-3210", "purchase_history": []}
}

sales = {
    1: {"transaction_date": pd.to_datetime('2024-03-01'), "product_id": "P001", "quantity": 1, "total_amount": 1200},
    2: {"transaction_date": pd.to_datetime("2024-03-02"), "product_id": "P002", "quantity": 2, "total_amount": 1600},
    3: {"transaction_date": pd.to_datetime("2024-03-03"), "product_id": "P003", "quantity": 1, "total_amount": 500}
}
Instructions for running the system:
1: Run the script python inventory_management.py
2: call the function menu()
3: press keywords as per requirements 

Challenges faced:
1:handling multiple functions single time
2:taking care of data types for all inputs
3: Error handling while taking wrong inputs 
