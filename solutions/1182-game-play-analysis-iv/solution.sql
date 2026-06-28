# Write your MySQL query statement below
with consecutive_login as (
        select player_id , event_date ,
        lag(event_date) over(partition by player_id order by event_date asc) as prev_day,
        dense_rank() over(partition by player_id order by event_date asc) as rnk
        from Activity 
)

select 
    round(
        count( distinct
            (case when datediff(event_date,prev_day) = 1 and rnk = 2 then player_id end ))/
            count(distinct player_id),2) as fraction
    from consecutive_login

