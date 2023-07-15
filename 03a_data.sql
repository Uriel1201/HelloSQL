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
