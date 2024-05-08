/* 
09. Most Friended.

Returning a list of
users and their corresponding friend
count. Assuming that only
unique friendships are displayed. */

create table friends_p9 (user_1 integer, user_2 integer);

insert into friends_p9 with names as (
    select 1, 2 from dual union all 
    select 1, 3 from dual union all 
    select 1, 4 from dual union all 
    select 2, 3 from dual
) select * from names;
