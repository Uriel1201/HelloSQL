/* Upgrade Rate by Product Action

Returning the fraction of users, rounded to two
decimal places, who first accessed feature
two (type: F2 in events table) and
upgraded to premium within the first 30
days of signing up. */


create table users_p8 (user_id integer, name varchar (9), join_date date);

create table events_p8 (user_id integer, type varchar (2), access_date date);

insert into users_p8 with names as (
     select 1, 'John',   '14-Feb-20' from dual union all 
     select 2, 'Jane',   '14-Feb-20' from dual union all
     select 3, 'Jill',   '15-Feb-20' from dual union all
     select 4, 'Josh',   '15-Feb-20' from dual union all
     select 5, 'Jean',   '16-Feb-20' from dual union all
     select 6, 'Justin', '17-Feb-20' from dual union all
     select 7, 'Jeremy', '18-Feb-20' from dual
)
select * from names;

insert into events_p8 with names as  (
     select 1, 'F1', '1-Mar-20'  from dual union all
     select 2, 'F2', '2-Mar-20'  from dual union all
     select 2, 'P',  '12-Mar-20' from dual union all
     select 3, 'F2', '15-Mar-20' from dual union all
     select 4, 'F2', '15-Mar-20' from dual union all
     select 1, 'P',  '16-Mar-20' from dual union all
     select 3, 'P',  '22-Mar-20' from dual
)
select * from names;

select * from users_p8;
select * from events_p8;

create table rank_p8 as
select user_id, 
       type, 
       access_date,
       row_number() over (partition by user_id order by access_date) rank_date
           from events_p8
           order by 1;

select * from rank_p8;

create table BeginF2_p8 as
select * from rank_p8 
          where rank_date = 1 and type = 'F2';

select * from BeginF2_p8;

create table Premium_p8 as
select * from events_p8 
         where type = 'P';

select * from Premium_p8;

create table F2toP_users_p8 as
select a.user_id, c.join_date, b.access_date as to_Premium_date
from BeginF2_p8 a 
left join Premium_p8 b
on a.user_id = b.user_id 
left join users_p8 c
on a.user_id = c.user_id 
where (b.access_date - a.access_date) > 0
      or (b.access_date - a.access_date) is null
order by 1;

select * from F2toP_users_p8;
