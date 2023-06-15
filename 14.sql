create table employee_p14 (id integer, pay_month integer, salary integer);

insert into employee_p14 with names as (
    select 1 i, 1, 20 from dual union all 
    select 2 i, 1, 20 from dual union all 
    select 1 i, 2, 30 from dual union all 
    select 2 i, 2, 30 from dual union all 
    select 3 i, 2, 40 from dual union all 
    select 1 i, 3, 40 from dual union all 
    select 3 i, 3, 60 from dual union all 
    select 1 i, 4, 60 from dual union all 
    select 3 i, 4, 70 from dual
) select * from names;

select * from employee_p14;

create table ranks_p14 as
select id, pay_month, salary, rank () over (partition by id order by pay_month desc) as rank
from employee_p14;

select * from ranks_p14;

create table order_p14 as
select a.id, a.pay_month, a.salary, b.salary as cumulative, a.rank
from ranks_p14 a 
    left join ranks_p14 b 
    on a.id = b.id and a.pay_month >= b.pay_month
    order by 1, 2;

select * from order_p14;

select id, pay_month, salary, sum (cumulative) as cumulative_sum 
    from order_p14 
    where rank > 1
    group by id, pay_month, salary 
    order by 1, 2;
