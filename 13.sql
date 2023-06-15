create table scores_p13 (id integer, score number);

insert into scores_p13 with names as (
    select 1, 3.50 from dual union all 
    select 2, 3.65 from dual union all 
    select 3, 4.00 from dual union all 
    select 4, 3.85 from dual union all 
    select 5, 4.00 from dual union all 
    select 6, 3.65 from dual
) select * from names;

select * from  scores_p13;

select s1.id, s1.score, count (distinct s2.score) as rank
    from scores_p13 s1 
    left join scores_p13 s2 
    on s1.score <= s2.score
    group by s1.id, s1.score
    order by 3;
