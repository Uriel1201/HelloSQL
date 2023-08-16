/*
23. Rolling Sum Salary.
writing a query to return a table that displays, for
each month in the first half of the year,
the rolling sum of the employee’s salary
for that month and the following two
months. */ 

select * from salary_p23;

select a.months, (a.salary + b.salary + c.salary) as rolling
from salary_p23 a 
    left join salary_p23 b 
    on a.months = b.months - 1
 left join salary_p23 c 
    on a.months = c.months - 2
    where a.months <= 6
order by 1;
