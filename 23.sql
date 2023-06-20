create table salary_p23 (months integer, salary number); 

insert into salary_p23 with names as (
    select 1, 2000 from dual union all 
    select 2, 3000 from dual union all 
    select 3, 5000 from dual union all 
    select 4, 4000 from dual union all 
    select 5, 2000 from dual union all 
    select 6, 1000 from dual union all 
    select 7, 2000 from dual union all 
    select 8, 4000 from dual union all 
    select 9, 5000 from dual
) select * from names;

select * from salary_p23;

select a.months, (a.salary + b.salary + c.salary) as rolling
from salary_p23 a 
    left join salary_p23 b 
    on a.months = b.months - 1
 left join salary_p23 c 
    on a.months = c.months - 2
    where a.months <= 6
order by 1;
