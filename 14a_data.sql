/*
Writing a query to get, for each month, the
cumulative sum of an employee’s salary
over a period of 3 months, excluding the
most recent month. */ 

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
