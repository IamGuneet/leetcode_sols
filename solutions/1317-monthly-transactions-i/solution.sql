/* Write your T-SQL query statement below */
with approved_data as (
select format(trans_date,'yyyy-MM') as month , country,sum(amount) as approved_total_amount , count(*) as approved_count
from 
    Transactions
where state = 'approved'
group by format(trans_date,'yyyy-MM'), country
)
,
raw_data as (
select 
    format(t.trans_date,'yyyy-MM') as month ,
    t.country ,
     count(*) as trans_count ,
     sum(t.amount) as trans_total_amount
from Transactions t
group by format(t.trans_date ,'yyyy-MM'),t.country
)

select r.month,
        r.country,
       r.trans_count,
       coalesce(a.approved_count,0) as approved_count,
       r.trans_total_amount,
       coalesce(a.approved_total_amount,0) as approved_total_amount
 from 
    raw_data r
left join 
    approved_data a
on 
    r.month = a.month 
    and
     (r.country = a.country or (r.country is null and a.country is null))
