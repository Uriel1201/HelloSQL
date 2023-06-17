create table stations_p17 (id integer, city varchar (20), states varchar (20), latitude number, longitude number);

insert into stations_p17 with names as (
    select 1, 'Asheville',      'North Carolina', 35.6, 82.6  from dual union all 
    select 2, 'Burlington',     'North Carolina', 36.1, 79.4  from dual union all
    select 3, 'Chapel Hill',    'North Carolina', 35.9, 79.1  from dual union all
    select 4, 'Davidson',       'North Carolina', 35.5, 80.8  from dual union all
    select 5, 'Elizabeth City', 'North Carolina', 36.3, 76.3  from dual union all
    select 6, 'Fargo',          'North Dakota',   46.9, 96.8  from dual union all
    select 7, 'Grand Forks',    'North Dakota',   47.9, 97.0  from dual union all
    select 8, 'Hettinger',      'North Dakota',   46.0, 102.6 from dual union all
    select 9, 'Inkster',        'North Dakota',   48.2, 97.6  from dual
) select * from names;

create table N_p17 as
select states, count (*) as n
    from stations_p17 
    group by states;

select * from N_p17;

select a.states, a.latitude, case when mod (b.n,2) = 0 then 0 else 1 end as reminder 
    from stations_p17 a 
    left join N_p17 b
    on a.states = b.states 
    order by 1, 2;
