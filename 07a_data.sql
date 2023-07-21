/* 
07. Mobile and Web Visitors.

Returning the
fraction of users who only visited
mobile, only visited web, and visited
both. */

create table mobile_p7 (user_id integer, page_url char);
create table web_p7    (user_id integer, page_url char);

insert into mobile_p7 with names as (
    select 1,  'A' from dual union all 
    select 2,  'B' from dual union all 
    select 3,  'C' from dual union all 
    select 4,  'A' from dual union all 
    select 9,  'B' from dual union all 
    select 2,  'C' from dual union all 
    select 10, 'B' from dual
) select * from names;

insert into web_p7 with names as (
    select 6, 'A' from dual union all 
    select 2, 'B' from dual union all 
    select 3, 'C' from dual union all 
    select 7, 'A' from dual union all 
    select 4, 'B' from dual union all 
    select 8, 'C' from dual union all 
    select 5, 'B' from dual
) select * from names;
