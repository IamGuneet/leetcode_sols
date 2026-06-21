# Write your MySQL query statement below
with filtered_table as (
    select id, visit_date , people, 
        id - row_number() over(order by id) rnk
        from Stadium
        where people>=100
)

select id, visit_date, people
    from filtered_table
    where rnk in (
        select 
            rnk
            from filtered_table
            group by rnk
            having count(*) >= 3
    )        
    order by visit_date asc
