/* 
10. Project Aggregation 

Writing a query to return the start and end
dates of each project, and the number of
days it took to complete. */

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
