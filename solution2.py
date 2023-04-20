import json

# Read in the order JSON files
with open('orders.json', 'r') as ourOrders:
    orders = json.load(ourOrders)

output = []
for product_id in set([order['product_id'] for order in orders]):
    prices = [order['price'] for order in orders if order['product_id'] == product_id]
    changes = ['-' if i == 0 else 'rise' if i > 0 else 'fall' for i in [prices[i] - prices[i-1] for i in range(len(prices))]]
    for i, order in enumerate(orders):
        if order['product_id'] == product_id:
            order['change'] = changes[i]
            output.append(order)

# Write into the output file
with open('output.json', 'w') as outputOrders:
    json.dump(output, outputOrders)
