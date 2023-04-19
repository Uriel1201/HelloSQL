/* Time Difference Between Latest Actions

writing a query to return for each user the
time elapsed between the last action
and the second-to-last action, in
ascending order by user ID. */ 

create table users_p4 (id integer, actions varchar (10), action_date date);

insert into users_p4 with names as (
    select 1, 'Start', '13-feb-20' from dual union all 
    select 1, 'Cancel', '13-feb-20' from dual union all 
    select 2, 'Start', '11-feb-20' from dual union all 
    select 2, 'Publish', '14-feb-20' from dual union all 
    select 3, 'Start', '15-feb-20' from dual union all 
    select 3, 'Cancel', '15-feb-20' from dual union all 
    select 4, 'Start', '18-feb-20' from dual union all 
    select 1, 'Publish', '19-feb-20' from dual
) select * from names;

select * from users;

create table numbers_p4 as
select id, action_date, 
       row_number() over (partition by id order by action_date desc) as
       rank_action
       from users_p4;

select * from numbers_p4;

create table n1_p4 as
select id, action_date as last_action
       from numbers_p4
       where rank_action = 1;

create table n2_p4 as
select id, action_date as second_last_action
       from numbers_p4  
       where rank_action = 2;

select * from n1_p4;
select * from n2_p4;

select a.id, (a.last_action - b.second_last_action) as elapsed_days 
       from n1_p4 a
       left join n2_p4 b
       on a.id = b.id
       order by a.id;
