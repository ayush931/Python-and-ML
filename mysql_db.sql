select * from superstore;

select * from superstore limit 10;

select count(*) from superstore;

select count(*) as total_number_of_users from superstore;

select 'Customer ID' from superstores;

select count(`Customer Name`) from superstore;

select distinct(`Customer Name`) from superstore;

select count(distinct(`Customer Name`)) from superstore;

select count(distinct(`Customer Name`)) as unique_customer_name from superstore;

select * from students;

select * from superstore;

select `Order date`, `Customer ID`, City
from superstore
limit 10;

select * from superstore
where Quantity > 5;

select `Customer Name`, Quantity
from superstore
where Quantity > 5;

select `Customer Name`, Quantity
from superstore
where Quantity <> 5;

select `Customer Name`, Quantity, `Ship Mode`
from superstore
where `Ship Mode` = "Standard Class"
limit 10;

select * from superstore
where Region = "South" and Category = "Furniture";

select * from superstore
where Sales between 500 and 900;

select `Customer Name` from superstore
where `Customer Name` like "A%";

select * from superstore
where Category in ("Furniture", "Technology");

select avg(Sales) as average_sales from superstore;

select sum(sales) as total_sales from superstore;

select min(Profit) as profit_min from superstore;

select max(Profit) as max_profit from superstore;

select round(sum(sales), 2) as total_sales from superstore
where Region = "South";

select * from superstore;

select Sales from superstore order by Sales desc;

select Sales, `Customer Name` from superstore order by `Customer Name` asc;

select Region, round(sum(Sales)) as total_sales
from superstore
group by Region;

select Region, round(sum(Sales)) as total_sales
from superstore
group by Region
order by Region desc;