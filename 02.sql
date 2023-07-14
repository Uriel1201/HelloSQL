/*Changes in Net Worth

Writing a query to return the change in net worth for each use
r, ordered by decreasing net change.*/

create table transactions_p2 (sender integer, receiver integer, amount decimal, transaction_date date);

insert into transactions_p2 with names as
(select 5,2,10,'12-feb-20' from dual union all
 select 1,3,15,'13-feb-20' from dual union all
 select 2,1,20,'13-feb-20' from dual union all
 select 2,3,25,'14-feb-20' from dual union all
 select 3,1,20,'15-feb-20' from dual union all
 select 3,2,15,'15-feb-20' from dual union all
 select 1,4,5,'16-feb-20'  from dual)
 select * from names;

select * from transactions_p2; 

create table debited_p2 as
select sender, sum(amount) as debited
from transactions_p2
group by sender
order by sender;

create table credited_p2 as
select receiver, sum(amount) as credited
from transactions_p2
group by receiver
order by receiver;

select * from debited_p2;
select * from credited_p2;

select coalesce(d.sender,c.receiver) as user_id,
coalesce(c.credited,0)-coalesce(d.debited,0) as net_change
from credited_p2 c
full outer join debited_p2 d
on c.receiver=d.sender
order by 2 desc; 
