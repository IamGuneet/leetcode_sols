# Write your MySQL query statement below
with ranked_salary as (
    select e.id ,e.name as Employee ,e.salary ,d.name as Department , dense_rank() over(partition by d.id order by salary desc) as rnk
    from Employee e 
    join Department d 
    on e.departmentId = d.id
)

select Department, Employee , Salary 
from ranked_salary 
where rnk < 4


