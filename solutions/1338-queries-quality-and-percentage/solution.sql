/* Write your T-SQL query statement below */

select query_name , 
       round(sum(cast(rating as decimal(10,2))/position)/count(*) , 2) as quality ,
        round(avg(
            case when rating < 3 then 100.0 else 0.0 end
        ) ,2) as poor_query_percentage
from Queries
group by query_name

