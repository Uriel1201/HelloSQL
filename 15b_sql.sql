/*
15. Team Standings.

Writing a query to return the scores of
each team */ 

select * from teams_p15;
select * from matches_p15;

create table hostp_p15 as
select host_team as team_id, 
    sum (case when host_goals > guest_goals then 3
         when host_goals = guest_goals then 1
         else 0 end) as points
    from matches_p15
    group by host_team;

create table guestp_p15 as
select guest_team as team_id, 
    sum (case when host_goals < guest_goals then 3
         when host_goals = guest_goals then 1
         else 0 end) as points
    from matches_p15
    group by guest_team;

select * from hostp_p15;
select * from guestp_p15;

select a.team_name, b.points + c.points as score 
    from teams_p15 a 
    left join hostp_p15 b 
    on a.team_id = b.team_id
    left join guestp_p15 c 
    on a.team_id = c.team_id
order by 2 desc, 1;
