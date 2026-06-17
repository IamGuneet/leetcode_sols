# Write your MySQL query statement below
with salary_ranked as (
    select d.name as Department ,e.departmentId ,e.name as Employee , e.salary as Salary , 
    dense_rank() over(partition by e.departmentId order by salary desc) as rnk
    from Employee e 
    join Department d on
    e.departmentId = d.id
)
select Department , Employee, Salary 
from salary_ranked 
where rnk <2
