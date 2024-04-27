/* 
04. Time Difference Between Latest Actions

writing a query to return for each user the
time elapsed between the last action
and the second-to-last action, in
ascending order by user ID. */ 

create table users_p4 (id integer, actions varchar (10), action_date date);

insert into users_p4 with names as (
    select 1, 'Start',   '13-feb-20' from dual union all 
    select 1, 'Cancel',  '13-feb-20' from dual union all 
    select 2, 'Start',   '11-feb-20' from dual union all 
    select 2, 'Publish', '14-feb-20' from dual union all 
    select 3, 'Start',   '15-feb-20' from dual union all 
    select 3, 'Cancel',  '15-feb-20' from dual union all 
    select 4, 'Start',   '18-feb-20' from dual union all 
    select 1, 'Publish', '19-feb-20' from dual
) select * from names;
