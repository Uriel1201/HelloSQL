"""
#11. Birthday attendance
Given the following two tables, write a query to return the fraction of students, 
rounded to two decimal places, who attended school  (attendance = 1) on their birthday.
"""

attendance['school_date'] = pd.to_datetime(attendance['school_date'])
students['date_birth'] = pd.to_datetime(students['date_birth'])

attendance['day'] = attendance['school_date'].dt.day
attendance['month'] = attendance['school_date'].dt.month
attendance = attendance[['student_id', 'day', 'month', 'attendance']]

students['day'] = students['date_birth'].dt.day
students['month'] = students['date_birth'].dt.month
student_births = students[['student_id', 'day', 'month']]

attendance.set_index(['student_id', 'day', 'month'], inplace = True, drop = True)
student_births.set_index(['student_id', 'day', 'month'], inplace = True, drop = True)

birthday_attendance = pd.concat([attendance, student_births], axis = 1, join = 'inner')

i = np.where(birthday_attendance['attendance'] == 'T', 1.0, 0.0).sum() / len(birthday_attendance)
d = {'rate' : [i]}
birthday_attendance_rate = pd.DataFrame(d)

birthday_attendance_rate.round(2)
