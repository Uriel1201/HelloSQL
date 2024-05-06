/* 
08. Upgrade Rate by Product Action

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
) select * from names;

insert into events_p8 with names as (
     select 1, 'F1', '1-Mar-20'  from dual union all
     select 2, 'F2', '2-Mar-20'  from dual union all
     select 2, 'P',  '12-Mar-20' from dual union all
     select 3, 'F2', '15-Mar-20' from dual union all
     select 4, 'F2', '15-Mar-20' from dual union all
     select 1, 'P',  '16-Mar-20' from dual union all
     select 3, 'P',  '22-Mar-20' from dual
) select * from names;
