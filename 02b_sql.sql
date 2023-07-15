/*Changes in Net Worth

Writing a query to return the change in net worth for each use
r, ordered by decreasing net change.*/

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
