select t.request_at as Day , 
 round(sum(
    case when t.status in ("cancelled_by_driver","cancelled_by_client") then 1 else 0 end
        )/count(*),
        2) as `Cancellation Rate` 
 from Trips t
 join Users u on t.client_id = u.users_id and u.banned = "No"
 join Users u1 on t.driver_id = u1.users_id and u1.banned ="No"
where t.request_at between "2013-10-01" and "2013-10-03"
group by t.request_at
order by t.request_at asc
