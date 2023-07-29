/* 
14. Cumulative Salary.

Writing a query to get, for each month, the
cumulative sum of an employee’s salary
over a period of 3 months, excluding the
most recent month. */ 

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
