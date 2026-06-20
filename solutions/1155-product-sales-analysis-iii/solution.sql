# Write your MySQL query statement below
select product_id, year as first_year , quantity , price 
from Sales s
where (product_id,year) in (
    select product_id ,Min(year) 
    from Sales s
    group by product_id
) 
