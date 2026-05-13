# Write your MySQL query statement below
select user_id, name , mail 
from Users 
where mail REGEXP '^[a-zA-Z][A-Za-z0-9_.-]*@leetcode\\.com$'
and mail like binary '%@leetcode.com';
