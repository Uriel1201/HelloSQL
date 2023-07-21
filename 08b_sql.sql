/* 
08. Upgrade Rate by Product Action

Returning the fraction of users, rounded to two
decimal places, who first accessed feature
two (type: F2 in events table) and
upgraded to premium within the first 30
days of signing up. */

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

create table BeginFromF2_p8 as
select * from rank_p8 
          where rank_date = 1 and type = 'F2';

select * from BeginFromF2_p8;

create table Premium_p8 as
select * from events_p8 
         where type = 'P';

select * from Premium_p8;

create table F2toP_users_p8 as
select a.user_id, c.join_date, b.access_date as to_Premium_date
       from BeginFromF2_p8 a 
       left join Premium_p8 b
          on a.user_id = b.user_id 
       left join users_p8 c
          on a.user_id = c.user_id
       order by 1;

select * from F2toP_users_p8;

select round (1.0 * sum (case when (to_Premium_date - join_date) <= 30 then 1 else 0 end) / count (*), 2) 
       as upgrade_rate
       from F2toP_users_p8;
