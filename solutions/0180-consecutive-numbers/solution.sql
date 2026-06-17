# Write your MySQL query statement below
select distinct num as ConsecutiveNums from 
(
    select num,
    lead(num) over(order by id) as prev,
    lag(num) over(order by id) as nex
    from Logs
) as log_seq
where num = prev and num = nex
