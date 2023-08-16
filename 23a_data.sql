/*
23. Rolling Sum Salary.
writing a query to return a table that displays, for
each month in the first half of the year,
the rolling sum of the employee’s salary
for that month and the following two
months. */ 

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
