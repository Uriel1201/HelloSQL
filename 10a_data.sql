/* 
10. Project Aggregation 

Writing a query to return the start and end
dates of each project, and the number of
days it took to complete. */

create table projects_p10 (task_id integer, start_date date, end_date date);

insert into projects_p10 with names as (
    select 1, '01-Oct-20', '02-Oct-20' from dual union all
    select 2, '02-Oct-20', '03-Oct-20' from dual union all
    select 3, '03-Oct-20', '04-Oct-20' from dual union all
    select 4, '13-Oct-20', '14-Oct-20' from dual union all
    select 5, '14-Oct-20', '15-Oct-20' from dual union all
    select 6, '28-Oct-20', '29-Oct-20' from dual union all
    select 7, '30-Oct-20', '31-Oct-20' from dual
) select * from names;
