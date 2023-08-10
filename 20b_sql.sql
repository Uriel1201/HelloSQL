/*
20. Three in a row

Writing a query to return a
table showing the date and visitor count
of high-attendance periods, defined as
three consecutive entries (not
necessarily consecutive dates) with
more than 100 visitors.
*/

select * from attendance_p20;

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

create table dates_p20 as
select day1 as event_date 
    from threes_p20 
union 
select day2 as event_date
    from threes_p20
union 
select day3 as event_date
    from threes_p20;

select * from dates_p20;

select a.event_date, b.visitors
 from dates_p20 a 
    left join attendance_p20 b 
    on a.event_date = b.event_date;
