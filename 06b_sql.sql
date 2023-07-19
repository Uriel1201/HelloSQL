/*  
06. Content Recommendations

Writing a query to return page recommendations
to a social media user based on the
pages that their friends have liked, but
that they have not yet marked as liked. */

select * from friends_p6;
select * from likes_p6;

create table Flikes_p6 as
    select f.user_id, f.friend, l.page_likes as friend_likes
           from friends_p6 f
           inner join likes_p6 l
           on f.friend = l.user_id;

select * from Flikes_p6;

create table equals_p6 as
select a.user_id, a.friend, a.friend_likes, 
       l.page_likes as user_likes
       from Flikes_p6 a
       left join likes_p6 l
       on a.user_id = l.user_id and a.friend_likes = l.page_likes
       order by 1, 2;

select * from equals_p6;

select distinct user_id, friend_likes as recommendation
       from equals_p6 
       where user_likes is null
       order by 1;
