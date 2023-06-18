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

create table index_p20 as
select row_number() over (order by event_date) as id, event_date, visitors 
    from attendance_p20;

select * from index_p20;

create table threes_p20 as 
select a.event_date as day1, b.event_date as day2, c.event_date as day3
    from index_p20 a 
inner join index_p20 b
    on a.id + 1 = b.id
inner join index_p20 c 
    on a.id + 2 = c.id
    where a.visitors >= 100 
    and   b.visitors >= 100
    and   c.visitors >= 100;

select * from threes_p20;
