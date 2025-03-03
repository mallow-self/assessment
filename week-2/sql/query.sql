show databases;
use ecommerce1;

-- late orders
SELECT orderNumber,orderDate,requiredDate,shippedDate 
FROM orders
WHERE shippedDate > requiredDate;

-- List orders from Paris placed between April 2003 to June 2003 along with their customer details.
select c.customerNumber, c.customerName, c.phone, c.city, o.orderNumber, o.orderDate,o.status
from orders as o 
join customers as c 
on o.customerNumber = c.customerNumber
where c.city = "Paris" and o.orderDate between "2003-04-01" and "2003-06-30";

-- Identify the top 5 customers who have made the highest purchases (generated the highest revenue).
-- select * from customers;
-- select * from payments order by amount desc limit 5;
select c.customerNumber, c.customerName, sum(p.amount) as total_spent
from payments as p
join customers as c
on p.customerNumber = c.customerNumber
group by c.customerNumber, c.customerName
order by total_spent desc limit 5;