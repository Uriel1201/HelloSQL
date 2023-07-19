/* 
05. Super Users.

A company defines its super users as
those who have made at least two
transactions. 
Writing a query to return, for each user, the
date when they become a super user, ordered by oldest super users first.
Users who are not super users should
also be present in the table. */

create table users_p5 (user_id integer, product_id integer, transaction_date date);

insert into users_p5 with names as (
    select 1, 101, '12-feb-20' from dual union all 
    select 2, 105, '13-feb-20' from dual union all 
    select 1, 111, '14-feb-20' from dual union all 
    select 3, 121, '15-feb-20' from dual union all 
    select 1, 101, '16-feb-20' from dual union all 
    select 2, 105, '17-feb-20' from dual union all 
    select 4, 101, '16-feb-20' from dual union all 
    select 3, 105, '15-feb-20' from dual
  ) select * from names;
