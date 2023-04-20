import json
from datetime import datetime

# Read in the product and order JSON files
with open('products.json', 'r') as ourProducts:
    products = json.load(ourProducts)

with open('orders.json', 'r') as ourOrders:
    orders = json.load(ourOrders)

# Join the two JSON files on the product_id field
joinedJson = []
for product in products:
    for order in orders:
        if product['productid'] == order['product_id']:
            joinedJson.append({**product, **order})

# Filter for products ordered in the same year as their release year  j['orderDate'][:4]
ourOrderDate = datetime.strptime(joined['order_date'], '%Y-%m-%dT%H:%M:%S.%f%z').year
same_year = [joined for joined in joinedJson if joined['releasedate'] == ourOrderDate]

# Extract the brandName and categoryName of the matching products
matching_products = [(joined['brandname'], joined['categoryname']) for joined in same_year]

# Print the results
print('Products ordered in the same year as their release year:')
for brand, category in matching_products:
    print(f'{brand} {category}')
