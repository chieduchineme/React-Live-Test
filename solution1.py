import datetime
import json

with open('orders.json', 'r') as ourOrders:
    sales = json.load(ourOrders)

# print(ordersJson)

# calculate net sales amount
net_sales_amount = 0
for sale in sales:
    if sale['status'] == 'Created':
        net_sales_amount += sale['price']
    elif sale['status'] == 'Cancelled':
        net_sales_amount -= sale['price']
    elif sale['status'] == 'Returned':
        net_sales_amount -= sale['price']
print('Net Sales Amount:', net_sales_amount)

# calculate net sales average price
net_sales_prices = [sale['price'] for sale in sales if sale['status'] != 'Cancelled']
net_sales_avg_price = mean(net_sales_prices)
print('Net Sales Average Price:', net_sales_avg_price)


# calculate gross sales amount and gross sales average price
gross_sales_amount = 0
for sale in sales:
    gross_sales_amount += sale['price']
gross_sales_avg_price = gross_sales_amount / len(sales)

print('Gross Sales Amount:', gross_sales_amount)
print('Gross Sales Average Price:', gross_sales_avg_price)

# calculate average sales amount for the last 5 days of sales
last_five_days_sales = []
for sale in sales:
    sale_date = datetime.datetime.strptime(sale['order_date'], '%Y-%m-%dT%H:%M:%S.%f%z')
    days_since_sale = (datetime.datetime.now() - sale_date).days
    if days_since_sale < 5:
        last_five_days_sales.append(sale['price'])
avg_last_five_days_sales = sum(last_five_days_sales) / len(last_five_days_sales)

print('Average Sales Amount for Last 5 Days:', avg_last_five_days_sales)

# find location with highest sales
max_sales = 0
max_location = ''
for sale in sales:
    if sale['price'] > max_sales:
        max_sales = sale['price']
        max_location = sale['location']

print('Location with highest sales:', max_location)