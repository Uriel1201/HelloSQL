/* 
05. Super Users.

A company defines its super users as
those who have made at least two
transactions. 
writing a query to return, for each user, the
date when they become a super user, ordered by oldest super users first.
Users who are not super users should
also be present in the table. */

select * from users_p5;

create table ranks_p5 as
select user_id, transaction_date,
       row_number() over (partition by user_id order by transaction_date) user_ranks
       from users_p5;

select * from ranks_p5;

create table allusers_p5 as
select distinct(user_id)
       from users_p5;

select * from allusers_p5;

create table supers_p5 as
select user_id, transaction_date 
       from ranks_p5
       where user_ranks = 2;

select * from supers_p5;

select a.user_id, (b.transaction_date) superuser_date
       from allusers_p5 a
       left join supers_p5 b
       on a.user_id = b.user_id 
       order by 2;
