/*Most Frequent Item
write a
query to return the most frequent item
ordered on each date.*/

create table items  (dates date, item varchar (9));

insert into items with  
names as ( 
    select '01-jan-20', 'apple' from dual union all  
    select '01-jan-20', 'apple' from dual union all  
    select '01-jan-20', 'pear' from dual union all  
    select '01-jan-20', 'pear' from dual union all  
    select '02-jan-20', 'pear' from dual union all  
    select '02-jan-20', 'pear' from dual union all  
    select '02-jan-20', 'pear' from dual union all 
    select '02-jan-20', 'orange' from dual)  
    select * from names;

select *  from items;


create table counts as 
       select dates, item, count(*) as counts 
       from items
       group by dates, item 
       order by dates;

select * from counts;
