/* Rank Without Rank.

Writing a query to rank scores in the
following table without using a window
function. */ 

create table scores_p13 (id integer, score number); 

insert into scores_p13 with names as (
    select 1, 3.50 from dual union all 
    select 2, 3.65 from dual union all 
    select 3, 4.00 from dual union all 
    select 4, 3.85 from dual union all 
    select 5, 4.00 from dual union all 
    select 6, 3.65 from dual
) select * from names;

select * from scores_p13;

create table u_scores_p13 as 
select distinct score 
    from scores_p13
    order by 1 desc;

select * from u_scores_p13;

select s.id, s.score, count (u.score) as rank
    from scores_p13 s 
    inner join u_scores_p13 u
    on s.score <= u.score
    group by s.score, s.id
    order by 3;
