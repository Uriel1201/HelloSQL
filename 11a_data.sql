create table attendance_p11 (student_id integer, school_date date, attendance char);
create table students_p11 (student_id integer, school_id integer, grade integer, date_birth date);

insert into students_p11 with names as (
    select 1, 2, 5, '3-Apr-12' from dual union all 
    select 2, 1, 4, '4-Apr-13' from dual union all 
    select 3, 1, 3, '5-Apr-14' from dual union all 
    select 4, 2, 4, '3-Apr-13' from dual
) select * from names;

insert into attendance_p11 with names as (
    select 1, '3-Apr-20', 'F' from dual union all 
    select 2, '3-Apr-20', 'T' from dual union all 
    select 3, '3-Apr-20', 'T' from dual union all 
    select 1, '4-Apr-20', 'T' from dual union all 
    select 2, '4-Apr-20', 'T' from dual union all 
    select 3, '4-Apr-20', 'T' from dual union all 
    select 1, '5-Apr-20', 'F' from dual union all 
    select 2, '5-Apr-20', 'T' from dual union all 
    select 3, '5-Apr-20', 'T' from dual union all 
    select 4, '5-Apr-20', 'T' from dual 
) select * from names;
