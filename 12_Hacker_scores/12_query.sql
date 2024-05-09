/* 
12. Hacker Scores.

Writing  a
query to return the hacker ID, name, and
total score (the sum of maximum scores
for each challenge completed) ordered by descending score, and by ascending
hacker ID in the case of score tie. Do not
display entries for hackers with a score
of zero. */ 

select * from hackers_p12;
select * from submissions_p12;

create table ranks_p12 as
select hacker_id, score, rank() over(partition by hacker_id, challenge_id order by score desc) as rank_score
    from submissions_p12
    order by 1, 3;

select * from ranks_p12;

create table scores_p12 as
select h.hacker_id, h.name, r.score as scores
    from hackers_p12 h 
    left join ranks_p12 r 
    on h.hacker_id = r.hacker_id
    where rank_score = 1
    order by 1;

select * from scores_p12;

select hacker_id, name, sum (scores) as total_score 
    from scores_p12
    group by hacker_id, name
    having sum (scores) > 0
    order by 3 desc, 1;
