# %%
# !! {"metadata":{
# !!   "id":"cc-imports"
# !! }}

#<cc-imports>

import subprocess

# %%
# !! {"metadata":{
# !!   "id": "IE8M2McxGiy2"
# !! }}
"""

"""

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "EKtTYA_cGjwC",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704662561,
# !!     "user_tz": 360,
# !!     "elapsed": 320,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "504073f2-ee23-45dc-8bce-bcf625f80e08"
# !! }}
sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/functions_df.p'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>


# %%
# !! {"metadata":{
# !!   "id": "Mgncsu1RGpHJ",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704670717,
# !!     "user_tz": 360,
# !!     "elapsed": 807,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np
import functions_df as fdf

data = {'id'        : [1,2,1,2,3,1,3,1,3],
        'pay_month' : [1,1,2,2,2,3,3,4,4],
        'salary'    : [20,20,30,30,40,40,60,60,70]
        }

employee = pd.DataFrame(data)

# %%
# !! {"metadata":{
# !!   "id": "HwzTQ-VNGs2-",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704675929,
# !!     "user_tz": 360,
# !!     "elapsed": 198,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
employee.sort_values(by = ['id', 'pay_month'], inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 332
# !!   },
# !!   "id": "gxOrjQGNGuVi",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704677965,
# !!     "user_tz": 360,
# !!     "elapsed": 220,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "3c2c3a43-a059-417e-b78d-ebbd115f8be0"
# !! }}
employee

# %%
# !! {"metadata":{
# !!   "id": "uqmifFhAGy6o",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704682306,
# !!     "user_tz": 360,
# !!     "elapsed": 223,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
employee['rank'] = employee.groupby('id')['pay_month'].transform(fdf.desc_row_num)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 352
# !!   },
# !!   "id": "Z_Xk9O9vG0mv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704684415,
# !!     "user_tz": 360,
# !!     "elapsed": 201,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "be2091be-9585-496e-afa9-3e349d218c94"
# !! }}
employee

# %%
# !! {"metadata":{
# !!   "id": "a9pfyBGuG4fz",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704690485,
# !!     "user_tz": 360,
# !!     "elapsed": 216,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
no_last_month = employee[['id', 'salary']][employee['rank'] > 1]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 238
# !!   },
# !!   "id": "xEAlnmI5G7wi",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704693030,
# !!     "user_tz": 360,
# !!     "elapsed": 236,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "1aa173e3-b8c5-440e-805e-2195cba36ce0"
# !! }}
no_last_month

# %%
# !! {"metadata":{
# !!   "id": "TxSdG4N_G9DW",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704702831,
# !!     "user_tz": 360,
# !!     "elapsed": 165,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
cumm_salary = fdf.basic_cummulative(no_last_month, 'id', 'salary')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 143
# !!   },
# !!   "id": "waZxBydeHKNT",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704705064,
# !!     "user_tz": 360,
# !!     "elapsed": 196,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "8fac3677-04c6-4dca-82a9-57ade7ffb46d"
# !! }}
cumm_salary

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "u4ga-1xLH5RL",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717704719771,
# !!     "user_tz": 360,
# !!     "elapsed": 174,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "1be128ce-3f15-4f6e-e477-fc7d72701bd9"
# !! }}
cumm_salary.iloc[-1]

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyPNXiGeq7Al2a8SIKCbABHy"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
