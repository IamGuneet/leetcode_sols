# Write your MySQL query statement below
with conditional_table as (
select pid,tiv_2016,
    count(*) over(partition by tiv_2015) as similar,
    count(*) over(partition by lat,lon) as unique_city
from Insurance
)

select 
    round(sum(tiv_2016),2) as tiv_2016
from conditional_table 
    where 
        unique_city =1
            and 
        similar > 1
