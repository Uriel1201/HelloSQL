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

select * from projects_p10;

create table openings_p10 as
select start_date as start_project
       from projects_p10 
       where start_date not in
          (select end_date from projects_p10)
       order by 1;

create table endings_p10 as 
select end_date as end_project
       from projects_p10 
       where end_date not in
             (select start_date from projects_p10)
       order by 1;

select * from openings_p10;
select * from endings_p10;

create table allprojects_p10 as
select start_project, min (end_project) as end_project
       from openings_p10, endings_p10
       where start_project  < end_project
       group by start_project
       order by 1;

select * from allprojects_p10;

select row_number() over (order by start_project) as project_id,
       start_project,
       end_project,
       (end_project - start_project) as duration
            from allprojects_p10
            order by 4, 2;
