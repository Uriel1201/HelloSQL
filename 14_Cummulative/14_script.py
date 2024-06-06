#<cc-imports>

import subprocess
sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/functions_df.p'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>



import pandas as pd
import numpy  as np
import functions_df as fdf


employee.sort_values(by = ['id', 'pay_month'], inplace = True)
employee['rank'] = employee.groupby('id')['pay_month'].transform(fdf.desc_row_num)
no_last_month = employee[['id', 'salary']][employee['rank'] > 1]
cumm_salary = fdf.basic_cummulative(no_last_month, 'id', 'salary')
cumm_salary
cumm_salary.iloc[-1]
