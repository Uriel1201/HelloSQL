#<cc-imports>

import subprocess
sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/functions_df.p'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>


# pip install pandas
# pip install numpy
# pip install SQLAlchemy
# pip install cx_Oracle

import pandas as pd
import numpy  as np
import functions_df as fdf
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table = """select * from employee_p14;"""
  employee = pd.read_sql(table, engine)
  employee.sort_values(by = ['id', 'pay_month'], inplace = True)
  employee['rank'] = employee.groupby('id')['pay_month'].transform(fdf.desc_row_num)
  no_last_month = employee[['id', 'salary']][employee['rank'] > 1]
  cumm_salary = fdf.basic_cummulative(no_last_month, 'id', 'salary')
  cumm_salary
  cumm_salary.iloc[-1]
  
except SQLAlchemyError as e:
  print(e)
