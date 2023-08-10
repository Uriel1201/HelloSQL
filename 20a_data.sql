/*
20. Three in a row

Writing a query to return a
table showing the date and visitor count
of high-attendance periods, defined as
three consecutive entries (not
necessarily consecutive dates) with
more than 100 visitors.
*/

create table attendance_p20 (event_date date, visitors integer);

insert into attendance_p20 with names as ( 
    select '01-JAN-20', 10   from dual union all
    select '04-JAN-20', 109  from dual union all
    select '05-JAN-20', 150  from dual union all
    select '06-JAN-20', 99   from dual union all 
    select '07-JAN-20', 145  from dual union all  
    select '08-JAN-20', 1455 from dual union all 
    select '11-JAN-20', 199  from dual union all 
    select '12-JAN-20', 188  from dual
) select * from names;
