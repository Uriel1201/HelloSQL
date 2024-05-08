/* 
11. Birthday Attendance.

writing a query to return the fraction of students,
rounded to two decimal places, who
attended school on their birthday. */

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
