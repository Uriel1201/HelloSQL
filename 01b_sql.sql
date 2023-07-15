/* 
1. Cancellation Rates.

Writing a query to return the publication and cancellation 
rate for each user. */

select * from users_p1; 

create table totals_p1 as
select user_id, sum(case when action='start' then 1 else 0 end) as starts,
sum(case when action='cancel' then 1 else 0 end) as cancels,
sum(case when action='publish' then 1 else 0 end) as publishes
from users_p1
group by user_id
order by user_id;

select * from totals_p1;

select user_id, 1.0*publishes/starts as publish_rate, 1.0*cancels/starts as cancel_rate
from totals_p1;
