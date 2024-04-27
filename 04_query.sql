/* 
04. Time Difference Between Latest Actions

writing a query to return for each user the
time elapsed between the last action
and the second-to-last action, in
ascending order by user ID. */ 

select * from users_p4;

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
