/*
3. Most Frequent Item

writing a query to return the most frequent item
ordered on each date. */

create table items_p3 (dates date, item varchar (9));

insert into items_p3 with names as ( 
    select '01-jan-20', 'apple'  from dual union all  
    select '01-jan-20', 'apple'  from dual union all  
    select '01-jan-20', 'pear'   from dual union all  
    select '01-jan-20', 'pear'   from dual union all  
    select '02-jan-20', 'pear'   from dual union all  
    select '02-jan-20', 'pear'   from dual union all  
    select '02-jan-20', 'pear'   from dual union all 
    select '02-jan-20', 'orange' from dual
    ) select * from names;

select *  from items_p3;


create table counts_p3 as 
       select dates, item, count(*) as counts 
       from items_p3
       group by dates, item 
       order by dates;

select * from counts_p3;

create table ranks_p3 as
select dates, item, rank() over
       (partition by dates order by counts desc) rank
        from counts_p3;

select * from ranks_p3;

select dates, item
       from ranks_p3
       where rank = 1;
