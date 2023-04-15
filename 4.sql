/* Time Difference Between Latest Actions

writing a query to return for each user the
time elapsed between the last action
and the second-to-last action, in
ascending order by user ID. */ 

create table users (id integer, actions varchar (10), action_date date);

insert into users with names as (
    select 1, 'Start', '13-feb-20' from dual union all 
    select 1, 'Cancel', '13-feb-20' from dual union all 
    select 2, 'Start', '11-feb-20' from dual union all 
    select 2, 'Publish', '14-feb-20' from dual union all 
    select 3, 'Start', '15-feb-20' from dual union all 
    select 3, 'Cancel', '15-feb-20' from dual union all 
    select 4, 'Start', '18-feb-20' from dual union all 
    select 1, 'Publish', '19-feb-20' from dual)
    select * from names;

select * from users;

create table numbers as
select id, action_date, 
       row_number() over (partition by id order by action_date desc) lasts
       from users;

select * from numbers;

create table number1 as
select id, action_date
       from numbers 
       where lasts = 1;

create table number2 as
select id, action_date 
       from numbers  
       where lasts = 2;

select * from number1;
select * from number2;

select a.id, (a.action_date - b.action_date) days_elapsed
       from number1 a
       left join number2 b
       on a.id = b.id
       order by a.id;
