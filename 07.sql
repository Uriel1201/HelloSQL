/* Mobile and Web Visitors.

returning the
fraction of users who only visited
mobile, only visited web, and visited
both. */

create table mobile_p7  (user_id integer, page_url char);
create table web_p7  (user_id integer, page_url char);

insert into mobile_p7 with names as  (
    select 1, 'A' from dual union all 
    select 2, 'B' from dual union all 
    select 3, 'C' from dual union all 
    select 4, 'A' from dual union all 
    select 9, 'B' from dual union all 
    select 2, 'C' from dual union all 
    select 10, 'B' from dual
)
select * from names;

insert into web_p7 with names as  (
    select 6, 'A' from dual union all 
    select 2, 'B' from dual union all 
    select 3, 'C' from dual union all 
    select 7, 'A' from dual union all 
    select 4, 'B' from dual union all 
    select 8, 'C' from dual union all 
    select 5, 'B' from dual
)
select * from names;

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
