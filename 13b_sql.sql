/* 
13. Rank Without Rank.

Writing a query to rank scores in the
following table without using a window
function. */ 

select * from  scores_p13;

select s1.id, s1.score, count (distinct s2.score) as rank
    from scores_p13 s1 
    left join scores_p13 s2 
    on s1.score <= s2.score
    group by s1.id, s1.score
    order by 3;
