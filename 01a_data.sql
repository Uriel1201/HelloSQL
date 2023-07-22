/* 
01. Cancellation Rates.

Writing a query to return the publication and cancellation 
rate for each user. */

create table users_p1 (user_id integer, action varchar(9), dates date);

insert into users_p1 with names as (
  select 1,'start',  '01-jan-20'   from dual union all
  select 1,'cancel', '02-jan-20'   from dual union all
  select 2,'start',  '03-jan-20'   from dual union all
  select 1,'start',  '03-jan-20'   from dual union all
  select 1,'publish','04-jan-20'   from dual union all
  select 2,'publish','04-jan-20'   from dual union all
  select 3,'start',  '05-jan-20'   from dual union all
  select 3,'cancel', '06-jan-20'   from dual union all
  select 4,'start',  '07-jan-20'   from dual
  ) select * from names;
