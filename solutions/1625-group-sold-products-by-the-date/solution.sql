/* Write your T-SQL query statement below */
select sell_date ,
        count(distinct(product)) as num_sold , 
        string_agg(product,',') within group(order by product asc ) as products
from   
    (select distinct product, sell_date from Activities ) as UniqueActivity
group by sell_date
