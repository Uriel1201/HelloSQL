/* 11. Birthday Attendance.

writing a query to return the fraction of students,
rounded to two decimal places, who
attended school on their birthday. */

create table attendance_p11 (student_id integer, school_date date, attendance char);

create table students_p11 (student_id integer, school_id integer, grade integer, date_birth date);

insert into students_p11 with names as  (
    select 1, 2, 5, '3-Apr-12' from dual union all 
    select 2, 1, 4, '4-Apr-13' from dual union all 
    select 3, 1, 3, '5-Apr-14' from dual union all 
    select 4, 2, 4, '3-Apr-13' from dual
) select * from names;

insert into attendance_p11 with names as  (
    select 1, '3-Apr-20', 'F' from dual union all 
    select 2, '3-Apr-20', 'T' from dual union all 
    select 3, '3-Apr-20', 'T'  from dual union all 
    select 1, '4-Apr-20', 'T' from dual union all 
    select 2, '4-Apr-20', 'T' from dual union all 
    select 3, '4-Apr-20', 'T' from dual union all 
    select 1, '5-Apr-20', 'F' from dual union all 
    select 2, '5-Apr-20', 'T' from dual union all 
    select 3, '5-Apr-20', 'T' from dual union all 
    select 4, '5-Apr-20', 'T' from dual 
) select * from names;

select * from attendance_p11;
select * from students_p11;

create table birthday_att_p11 as 
select s.student_id, a.attendance as birthday_attendance
       from attendance_p11 a
       inner join students_p11 s
       on a.student_id = s.student_id
       and extract (day from a.school_date) = extract (day from s.date_birth)
       and extract (month from a.school_date) = extract (month from s.date_birth);

select * from birthday_att_p11;

select round (avg (case when birthday_attendance = 'T' then 1 else 0 end), 2) as birthday_attendance_rate
       from birthday_att_p11;
