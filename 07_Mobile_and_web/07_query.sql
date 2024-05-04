/* 
07. Mobile and Web Visitors.

Returning the
fraction of users who only visited
mobile, only visited web, and visited
both. */

select * from mobile_p7;
select * from web_p7;

create table visitors_p7 as
select distinct m.user_id as mobile, w.user_id as web 
       from mobile_p7 m
       full outer join web_p7 w
       on m.user_id = w.user_id
       order by 1;

select * from visitors_p7;

select avg(case when mobile is not null and web is null then 1 else 0 end
          ) as mobile_fraction,
       avg(case when mobile is null and web is not null then 1 else 0 end
          ) as web_fraction,
       avg(case when mobile is not null and web is not null then 1 else 0 end
          ) as both_fraction
       from visitors_p7;
