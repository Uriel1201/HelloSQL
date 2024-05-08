/* 
09. Most Friended.

Returning a list of
users and their corresponding friend
count. Assuming that only
unique friendships are displayed. */

select * from friends_p9;

create table numbers_p9 as
select user_1 from friends_p9
              union all
select user_2 from friends_p9
              order by 1;

select * from numbers_p9;

select user_1 as user_id,
       count(*) as number_of_friends
                from numbers_p9
                group by user_1
                order by 2 desc, user_1; 
