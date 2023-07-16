/*
03. Most Frequent Item

Writing a query to return the most frequent item
ordered on each date. */

select *  from items_p3;

create table counts_p3 as 
       select dates, item, count(*) as counts 
       from items_p3
       group by dates, item 
       order by dates;

select * from counts_p3;

create table ranks_p3 as
select dates, item, rank() over
       (partition by dates order by counts desc) as rank
        from counts_p3;

select * from ranks_p3;

select dates, item
       from ranks_p3
       where rank = 1;
