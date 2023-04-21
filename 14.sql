/* 14. Cumulative Salary Sum.

Writing a query to get, for each month, the
cumulative sum of an employee’s salary
over a period of 3 months, excluding the
most recent month. */

create table employee_p14 (id integer, pay_month integer, salary integer);

insert into employee_p14 with names as  (
    select 1 i, 1 p, 20 s from dual union all 
    select 2 i, 1 p, 20 s from dual union all 
    select 1 i, 2 p, 30 s from dual union all 
    select 2 i, 2 p, 30 s from dual union all 
    select 3 i, 2 p, 40 s from dual union all 
    select 1 i, 3 p, 40 s from dual union all 
    select 3 i, 3 p, 60 s from dual union all 
    select 1 i, 4 p, 60 s from dual union all 
    select 3 i, 4 p, 70 s from dual 
) select * from names;

select * from employee_p14;

create table ranks_p14 as
select id, pay_month, salary, 
    rank () over (partition by id order by pay_month desc) as rank
from employee_p14
    order by 4;

select * 
    from ranks_p14;

/* Dropping the last recent month and adding the first 3 months */
create table months_p14 as
select * 
    from ranks_p14 
    where rank > 1 and pay_month <= 3
    order by id, pay_month;

select * from months_p14;

select a.id, a.pay_month, a.salary, sum (b.salary) as cumulative_salary
    from months_p14 a 
    left join months_p14 b
    on a.id = b.id and
    a.pay_month >= b.pay_month
    group by a.id, a.pay_month, a.salary
    order by a.id, a.pay_month;
