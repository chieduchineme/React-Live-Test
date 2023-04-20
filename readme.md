# Data Processing Challenge
Thank you for your interest in the Data Engineer/Scientist position at Safeguard Global. 
As part of the selection process, we would like you to complete a take-home task to demonstrate 
your skills in working with data. The goal of this project is to test your ability to work with data sources, 
transform and query the data.

## Expectation
- Write one or more jobs to address the given requirements
- Everything should be running inside Docker containers. Please provide a script or docker-compose file that computes everything with a single command
- You can only use Python for this project

## Problems
### Problem 1
 Please calculate the followings with (one or more) job(s):
 - net sales amount. Note that there are three order statuses: created, cancelled and returned
 - net sales average price
 - gross sales amount (total sales)
 - gross sales average price (total sales)
 - average sales amount for the last 5 days of sales (Note that the sales do not have to be 5 consecutive calendar days)
 - the location with the highest sales

### Problem 2
In `orders` dataset, for each `product_id` please calculate price change (i.e., if the price of order is increased, you can write `rise`. If the price of order is decreased, you can write `fall`.)

Sample Input:
```
+-------------+------+-------------------+
|product_id   |price |order_date         |
+-------------+------+-------------------+
|<some-id-1>  |3.00  |2021-01-22 01:20:32|
|<some-id-1>  |3.00  |2021-01-22 02:50:20|
|<some-id-1>  |3.25  |2021-01-22 03:45:10|
|<some-id-2>  |3.25  |2021-01-22 13:45:10|
|<some-id-2>  |3.25  |2021-01-22 14:45:10|
|<some-id-2>  |3.45  |2021-01-22 15:45:10|
|<some-id-1>  |3.25  |2021-01-22 04:57:24|
|<some-id-1>  |2.99  |2021-01-22 05:44:47|
|<some-id-1>  |2.99  |2021-01-22 06:34:43|
|<some-id-1>  |3.50  |2021-01-22 07:05:29|
+-------------+------+-------------------+
```

Sample Output:
```
+-------------+------+-------------------+--------+
|product_id   |price |order_date         |change  |
+-------------+------+-------------------+--------+
|<some-id-1>  |3.25  |2021-01-22 03:45:10|rise    |
|<some-id-1>  |2.99  |2021-01-22 05:44:47|fall    |
|<some-id-1>  |3.50  |2021-01-22 07:05:29|rise    |
|<some-id-2>  |3.45  |2021-01-22 15:45:10|fall    |
+-------------+------+-------------------+--------+
```
### Problem 3
Which products are ordered in the same year as their release date?

## Evaluation Criteria
- Performance
- Code quality
- Tests
- Documentation
