/*
02. Changes in Net Worth

Writing a query to return the change in net worth for each user, 
ordered by decreasing net change. */

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
