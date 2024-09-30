from pymongo import MongoClient
import certifi

# ------------ Táblák ------------

customers = [
    {"CustomerID": 1, "FirstName": "John", "LastName": "Doe", "Email": "johndoe@example.com", "Phone": "123-456-7890"},
    {"CustomerID": 2, "FirstName": "Jane", "LastName": "Smith", "Email": "janesmith@example.com",
     "Phone": "123-456-7891"},
    {"CustomerID": 3, "FirstName": "Emily", "LastName": "Johnson", "Email": "emilyj@example.com",
     "Phone": "123-456-7892"},
    {"CustomerID": 4, "FirstName": "Michael", "LastName": "Brown", "Email": "michaelb@example.com",
     "Phone": "123-456-7893"},
    {"CustomerID": 5, "FirstName": "Linda", "LastName": "Davis", "Email": "lindad@example.com",
     "Phone": "123-456-7894"},
    {"CustomerID": 6, "FirstName": "Robert", "LastName": "Wilson", "Email": "robertw@example.com",
     "Phone": "123-456-7895"},
    {"CustomerID": 7, "FirstName": "Maria", "LastName": "Garcia", "Email": "mariag@example.com",
     "Phone": "123-456-7896"},
    {"CustomerID": 8, "FirstName": "James", "LastName": "Martinez", "Email": "jamesm@example.com",
     "Phone": "123-456-7897"},
    {"CustomerID": 9, "FirstName": "Lisa", "LastName": "Robinson", "Email": "lisar@example.com",
     "Phone": "123-456-7898"},
    {"CustomerID": 10, "FirstName": "Paul", "LastName": "Walker", "Email": "paulw@example.com",
     "Phone": "123-456-7899"},
    {"CustomerID": 11, "FirstName": "Laura", "LastName": "Allen", "Email": "lauraa@example.com",
     "Phone": "123-456-7810"},
    {"CustomerID": 12, "FirstName": "Kevin", "LastName": "Young", "Email": "keviny@example.com",
     "Phone": "123-456-7811"},
    {"CustomerID": 13, "FirstName": "Sarah", "LastName": "Hill", "Email": "sarahh@example.com",
     "Phone": "123-456-7812"},
    {"CustomerID": 14, "FirstName": "Brian", "LastName": "Scott", "Email": "brians@example.com",
     "Phone": "123-456-7813"},
    {"CustomerID": 15, "FirstName": "Nancy", "LastName": "Lopez", "Email": "nancylopez@example.com",
     "Phone": "123-456-7814"},
    {"CustomerID": 16, "FirstName": "Mark", "LastName": "Lee", "Email": "markl@example.com", "Phone": "123-456-7815"},
    {"CustomerID": 17, "FirstName": "Sandra", "LastName": "Harris", "Email": "sandrah@example.com",
     "Phone": "123-456-7816"},
    {"CustomerID": 18, "FirstName": "Jason", "LastName": "Clark", "Email": "jasonc@example.com",
     "Phone": "123-456-7817"},
    {"CustomerID": 19, "FirstName": "Karen", "LastName": "Lewis", "Email": "karenl@example.com",
     "Phone": "123-456-7818"},
    {"CustomerID": 20, "FirstName": "Jeff", "LastName": "Walker", "Email": "jeffw@example.com", "Phone": "123-456-7819"}
]
products = [
    {"ProductID": 100, "ProductName": "Keyboard", "Category": "Electronics", "Price": 29.99, "StockQuantity": 150},
    {"ProductID": 101, "ProductName": "Wireless Mouse", "Category": "Electronics", "Price": 19.99,
     "StockQuantity": 200},
    {"ProductID": 102, "ProductName": "HDMI Cable", "Category": "Accessories", "Price": 10.99, "StockQuantity": 300},
    {"ProductID": 103, "ProductName": "LED Monitor", "Category": "Electronics", "Price": 129.99, "StockQuantity": 100},
    {"ProductID": 104, "ProductName": "USB-C Adapter", "Category": "Accessories", "Price": 24.99, "StockQuantity": 180},
    {"ProductID": 105, "ProductName": "External HDD 1TB", "Category": "Storage", "Price": 59.99, "StockQuantity": 120},
    {"ProductID": 106, "ProductName": "Smartphone 11Pro", "Category": "Mobile Phones", "Price": 999.99,
     "StockQuantity": 75},
    {"ProductID": 107, "ProductName": "Bluetooth Speaker", "Category": "Audio", "Price": 99.99, "StockQuantity": 110},
    {"ProductID": 108, "ProductName": "Smartwatch 4", "Category": "Wearables", "Price": 199.99, "StockQuantity": 90},
    {"ProductID": 109, "ProductName": "DSLR Camera", "Category": "Photography", "Price": 449.99, "StockQuantity": 60},
    {"ProductID": 110, "ProductName": "Tripod Stand", "Category": "Photography", "Price": 45.99, "StockQuantity": 150},
    {"ProductID": 111, "ProductName": "Router 5G", "Category": "Electronics", "Price": 129.99, "StockQuantity": 85},
    {"ProductID": 112, "ProductName": "Laptop Pro 15", "Category": "Electronics", "Price": 1249.99,
     "StockQuantity": 40},
    {"ProductID": 113, "ProductName": "Graphic Tablet", "Category": "Accessories", "Price": 199.99,
     "StockQuantity": 125},
    {"ProductID": 114, "ProductName": "Gaming Chair", "Category": "Furniture", "Price": 249.99, "StockQuantity": 50},
    {"ProductID": 115, "ProductName": "Desk Lamp", "Category": "Furniture", "Price": 39.99, "StockQuantity": 200},
    {"ProductID": 116, "ProductName": "Bookshelf", "Category": "Furniture", "Price": 89.99, "StockQuantity": 80},
    {"ProductID": 117, "ProductName": "Wall Charger", "Category": "Accessories", "Price": 29.99, "StockQuantity": 250},
    {"ProductID": 118, "ProductName": "Portable SSD 500GB", "Category": "Storage", "Price": 99.99,
     "StockQuantity": 100},
    {"ProductID": 119, "ProductName": "Fitness Band", "Category": "Wearables", "Price": 59.99, "StockQuantity": 150}
]
orders = [
    {"OrderID": 200, "CustomerID": 1, "OrderDate": "2022-09-15", "Total": 349.97, "Status": "Shipped"},
    {"OrderID": 201, "CustomerID": 3, "OrderDate": "2022-09-16", "Total": 49.98, "Status": "Pending"},
    {"OrderID": 202, "CustomerID": 5, "OrderDate": "2022-09-17", "Total": 1099.98, "Status": "Shipped"},
    {"OrderID": 203, "CustomerID": 2, "OrderDate": "2022-09-18", "Total": 1499.98, "Status": "Delivered"},
    {"OrderID": 204, "CustomerID": 10, "OrderDate": "2022-09-19", "Total": 199.98, "Status": "Cancelled"},
    {"OrderID": 205, "CustomerID": 7, "OrderDate": "2022-09-20", "Total": 59.98, "Status": "Shipped"},
    {"OrderID": 206, "CustomerID": 8, "OrderDate": "2022-09-21", "Total": 299.97, "Status": "Pending"},
    {"OrderID": 207, "CustomerID": 6, "OrderDate": "2022-09-22", "Total": 249.98, "Status": "Shipped"},
    {"OrderID": 208, "CustomerID": 12, "OrderDate": "2022-09-23", "Total": 299.97, "Status": "Delivered"},
    {"OrderID": 209, "CustomerID": 15, "OrderDate": "2022-09-24", "Total": 124.98, "Status": "Cancelled"},
    {"OrderID": 210, "CustomerID": 14, "OrderDate": "2022-09-25", "Total": 349.97, "Status": "Shipped"},
    {"OrderID": 211, "CustomerID": 9, "OrderDate": "2022-09-26", "Total": 199.99, "Status": "Pending"},
    {"OrderID": 212, "CustomerID": 4, "OrderDate": "2022-09-27", "Total": 499.99, "Status": "Delivered"},
    {"OrderID": 213, "CustomerID": 20, "OrderDate": "2022-09-28", "Total": 249.98, "Status": "Shipped"},
    {"OrderID": 214, "CustomerID": 11, "OrderDate": "2022-09-29", "Total": 99.98, "Status": "Cancelled"},
    {"OrderID": 215, "CustomerID": 17, "OrderDate": "2022-09-30", "Total": 299.97, "Status": "Shipped"},
    {"OrderID": 216, "CustomerID": 18, "OrderDate": "2022-10-01", "Total": 249.98, "Status": "Delivered"},
    {"OrderID": 217, "CustomerID": 16, "OrderDate": "2022-10-02", "Total": 349.97, "Status": "Shipped"},
    {"OrderID": 218, "CustomerID": 19, "OrderDate": "2022-10-03", "Total": 99.99, "Status": "Cancelled"},
    {"OrderID": 219, "CustomerID": 13, "OrderDate": "2022-10-04", "Total": 199.99, "Status": "Pending"}
]
order_details = [
    {"DetailID": 300, "OrderID": 200, "ProductID": 100, "Quantity": 1, "PriceAtTimeOfOrder": 29.99},
    {"DetailID": 301, "OrderID": 200, "ProductID": 101, "Quantity": 2, "PriceAtTimeOfOrder": 19.99},
    {"DetailID": 302, "OrderID": 201, "ProductID": 102, "Quantity": 1, "PriceAtTimeOfOrder": 10.99},
    {"DetailID": 303, "OrderID": 202, "ProductID": 103, "Quantity": 1, "PriceAtTimeOfOrder": 129.99},
    {"DetailID": 304, "OrderID": 203, "ProductID": 104, "Quantity": 1, "PriceAtTimeOfOrder": 24.99},
    {"DetailID": 305, "OrderID": 204, "ProductID": 105, "Quantity": 1, "PriceAtTimeOfOrder": 59.99},
    {"DetailID": 306, "OrderID": 205, "ProductID": 106, "Quantity": 1, "PriceAtTimeOfOrder": 999.99},
    {"DetailID": 307, "OrderID": 206, "ProductID": 107, "Quantity": 1, "PriceAtTimeOfOrder": 99.99},
    {"DetailID": 308, "OrderID": 207, "ProductID": 108, "Quantity": 1, "PriceAtTimeOfOrder": 199.99},
    {"DetailID": 309, "OrderID": 208, "ProductID": 109, "Quantity": 1, "PriceAtTimeOfOrder": 449.99},
    {"DetailID": 310, "OrderID": 209, "ProductID": 110, "Quantity": 1, "PriceAtTimeOfOrder": 45.99},
    {"DetailID": 311, "OrderID": 210, "ProductID": 111, "Quantity": 1, "PriceAtTimeOfOrder": 129.99},
    {"DetailID": 312, "OrderID": 211, "ProductID": 112, "Quantity": 1, "PriceAtTimeOfOrder": 1249.99},
    {"DetailID": 313, "OrderID": 212, "ProductID": 113, "Quantity": 1, "PriceAtTimeOfOrder": 199.99},
    {"DetailID": 314, "OrderID": 213, "ProductID": 114, "Quantity": 1, "PriceAtTimeOfOrder": 249.99},
    {"DetailID": 315, "OrderID": 214, "ProductID": 115, "Quantity": 1, "PriceAtTimeOfOrder": 39.99},
    {"DetailID": 316, "OrderID": 215, "ProductID": 116, "Quantity": 1, "PriceAtTimeOfOrder": 89.99},
    {"DetailID": 317, "OrderID": 216, "ProductID": 117, "Quantity": 1, "PriceAtTimeOfOrder": 29.99},
    {"DetailID": 318, "OrderID": 217, "ProductID": 118, "Quantity": 1, "PriceAtTimeOfOrder": 99.99},
    {"DetailID": 319, "OrderID": 218, "ProductID": 119, "Quantity": 1, "PriceAtTimeOfOrder": 59.99}
]


# ------------ Importálás ------------
def insert_data():
    conn_string = ("mongodb+srv://kovalikdberci:123@cluster0.h5de4hj.mongodb.net/?retryWrites=true&w=majority&appName"
                   "=Cluster0")
    client = MongoClient(conn_string, tlsCAFile=certifi.where())
    db = client['Python_project']

    try:
        db.Customers.insert_many(customers)
        db.Products.insert_many(products)
        db.Orders.insert_many(orders)
        db.Order_details.insert_many(order_details)
        print("Data inserted successfully!")
    finally:
        client.close()


"""
if __name__ == "__main__":
    insert_data()
"""
client = MongoClient(
    "mongodb+srv://kovalikdberci:123@cluster0.h5de4hj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    tlsCAFile=certifi.where())
db = client['Python_project']

# ------------ Sample data ellenőrzés ----------------
"""
print("Databases:", client.list_database_names())
print("Collections in 'Python_project':", client['Python_project'].list_collection_names())


order_details_data = db.Order_details.find_one()
customers_data = db.Customers.find_one()
products_data = db.Products.find_one()
orders_data = db.Orders.find_one()

print("Sample Order Detail:", order_details_data)
print("Sample Customer:", customers_data)
print("Sample Product:", products_data)
print("Sample Order:", orders_data)

"""

# ------------ 1. Lekérdezés ----------------

from_date = "2022-09-15"
to_date = "2022-10-04"

pipeline = [
    {
        "$match": {
            "OrderDate": {"$gte": from_date, "$lte": to_date}
        }
    },
    {
        "$lookup": {
            "from": "Customers",
            "localField": "CustomerID",
            "foreignField": "CustomerID",
            "as": "CustomerDetails"
        }
    },
    {
        "$unwind": "$CustomerDetails"
    },
    {
        "$group": {
            "_id": "$CustomerID",
            "Összköltés": {"$sum": "$Total"},
            "Név": {"$first": {"$concat": ["$CustomerDetails.FirstName", " ", "$CustomerDetails.LastName"]}}
        }
    },
    {
        "$project": {
            "_id": 0,
            "Név": 1,
            "Összköltés": 1
        }
    },
    {
        "$sort": {"Összköltés": -1}
    },
    {
        "$limit": 5
    }
]

result = list(db.Orders.aggregate(pipeline))

print("1. Lekérdezés eredménye", '\n')

for customer in result:
    print(customer)

# ------------ 2. Lekérdezés ----------------

pipeline2 = [
    {
        "$lookup": {
            "from": "Order_details",
            "localField": "ProductID",
            "foreignField": "ProductID",
            "as": "OrderDetails"
        }
    },
    {
        "$unwind": "$OrderDetails"
    },
    {
        "$group": {
            "_id": "$Category",
            "TotalSales": {"$sum": {"$multiply": ["$OrderDetails.Quantity", "$OrderDetails.PriceAtTimeOfOrder"]}},
            "AveragePrice": {"$avg": "$Price"}
        }
    },
    {
        "$sort": {"TotalSales": -1}
    }
]

result2 = list(db.Products.aggregate(pipeline2))

print('\n', "2. Lekérdezés eredménye", '\n')

for category in result2:
    print("Category:", category["_id"])
    print("Total Sales:", category["TotalSales"])
    print("Average Price:", category["AveragePrice"], '\n')

# ------------ 3. Lekérdezés ----------------
low_stock = 50

pipeline3 = [
    {
        "$match": {
            "StockQuantity": {"$lt": low_stock}
        }
    },
    {
        "$project": {
            "ProductName": 1,
            "Category": 1,
            "StockQuantity": 1,
            "Price": 1
        }
    },
    {
        "$sort": {"StockQuantity": 1}
    }
]

result3 = list(db.Products.aggregate(pipeline3))

print('\n', "3. Lekérdezés eredménye", '\n')

print("Low Stock Products:")
for product in result3:
    print(
        f"Product: {product['ProductName']}, Category: {product['Category']}, Stock: {product['StockQuantity']}, "
        f"Price: ${product['Price']}")

# ------------ 4. Lekérdezés ----------------

pipeline4 = [
    {
        "$lookup": {
            "from": "Order_details",
            "localField": "ProductID",
            "foreignField": "ProductID",
            "as": "OrderDetails"
        }
    },
    {
        "$unwind": "$OrderDetails"
    },
    {
        "$group": {
            "_id": {
                "ProductID": "$ProductID",
                "ProductName": "$ProductName"
            },
            "TotalQuantitySold": {"$sum": "$OrderDetails.Quantity"}
        }
    },
    {
        "$sort": {"TotalQuantitySold": -1}

    },
    {
        "$limit": 5
    },
    {
        "$project": {
            "ProductID": "$_id.ProductID",
            "ProductName": "$_id.ProductName",
            "TotalQuantitySold": 1,
            "_id": 0
        }
    }
]

result4 = list(db.Products.aggregate(pipeline4))

print('\n', "4. Lekérdezés eredménye", '\n')

print("Top Selling Products:")
for product in result4:
    print(
        f"Product ID: {product['ProductID']}, Product Name: {product['ProductName']}, Total Sold: {product['TotalQuantitySold']}")

# ------------ 5. Lekérdezés ----------------

price_threshold = 100

pipeline5 = [
    {
        "$match": {
            "Price": {"$gt": price_threshold}
        }
    },
    {
        "$project": {
            "ProductName": 1,
            "Category": 1,
            "Price": 1,
            "StockQuantity": 1
        }
    },
    {
        "$limit": 5
    },
    {
        "$sort": {"Price": -1}
    }
]

result5 = list(db.Products.aggregate(pipeline5))

print('\n', "5. Lekérdezés eredménye", '\n')

print("High-Priced Products:")
for product in result5:
    print(
        f"Product Name: {product['ProductName']}, Category: {product['Category']}, Price: ${product['Price']}, Stock: {product['StockQuantity']}")

# ------------ CRUD műveletek ----------------

print('\n', "CRUD műveletek:", '\n')

# ------------ Create ----------------


db.Products.insert_one({
    "ProdutID": 120,
    "ProductName": "New High-End Speaker",
    "Category": "Audio",
    "Price": 450.00,
    "StockQuantity": 50
})


# ------------ Update ----------------
db.Products.update_one(
    {"ProductName": "New High-End Speaker"},
    {"$set": {"StockQuantity": 60}}
)

# ------------ Delete ----------------
"""
query = {"ProductName": "New High-End Speaker"}
result10 = db.Products.delete_many(query)
print(f"Documents deleted: {result10.deleted_count}")
"""
# ------------ Read ----------------

results = db.Products.find({"Category": "Audio"})
for product in results:
    print(product)

client.close()
