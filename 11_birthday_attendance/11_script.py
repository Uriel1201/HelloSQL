# %%
# !! {"metadata":{
# !!   "id": "Bq2WE66SREAb"
# !! }}
"""
#11. Birthday attendance
Given the following two tables, write a query to return the fraction of students, rounded to two decimal places, who attended school  (attendance = 1) on their birthday.
"""

# %%
# !! {"metadata":{
# !!   "id": "_xSryJl3RFRT"
# !! }}
import pandas as pd
import numpy  as np

data1 = {'student_id'    : [1,2,3,1,2,3,1,2,3,4],
        'school_date'    : ['03-APR-20',
                            '03-APR-20',
                            '03-APR-20',
                            '04-APR-20',
                            '04-APR-20',
                            '04-APR-20',
                            '05-APR-20',
                            '05-APR-20',
                            '05-APR-20',
                            '05-APR-20'],
         'attendance'    : ['F','T','T','T','T','T','F','T','T','T']
        }

data2 = {'student_id'    : [1,2,3,4],
         'school_id'     : [2,1,1,2],
         'grade'         : [5,4,3,4],
         'date_birth'    : ['03-APR-12',
                            '04-APR-13',
                            '05-APR-14',
                            '03-APR-13']
                        # '15-OCT-20',
                        # '29-OCT-20',
                        # '31-OCT-20']
        }

attendance  = pd.DataFrame(data1)
students    = pd.DataFrame(data2)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "AQ5L1vg2R_6g",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715208699471,
# !!     "user_tz": 360,
# !!     "elapsed": 214,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "cfec3d33-2800-471a-8c74-e2ee12f1d368"
# !! }}
attendance['school_date'] = pd.to_datetime(attendance['school_date'])
students['date_birth'] = pd.to_datetime(students['date_birth'])

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 383
# !!   },
# !!   "id": "fitvy3htShD3",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715208701786,
# !!     "user_tz": 360,
# !!     "elapsed": 210,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "0178fcb4-0323-4e35-eaa8-e7efa931e177"
# !! }}
attendance

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 194
# !!   },
# !!   "id": "CG3mBfkJSkQ2",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715208705001,
# !!     "user_tz": 360,
# !!     "elapsed": 223,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "aad0bd10-fd64-4fc6-c75c-1cd14a1e8858"
# !! }}
students

# %%
# !! {"metadata":{
# !!   "id": "oM-sO8NKTS9M"
# !! }}
attendance['day'] = attendance['school_date'].dt.day
attendance['month'] = attendance['school_date'].dt.month
attendance = attendance[['student_id', 'day', 'month', 'attendance']]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 383
# !!   },
# !!   "id": "9A-8tUxZT-Ei",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715208714732,
# !!     "user_tz": 360,
# !!     "elapsed": 200,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "884188ca-1fd8-4aea-e9a4-9a6b89be956b"
# !! }}
attendance

# %%
# !! {"metadata":{
# !!   "id": "S9vuaC9HUORN"
# !! }}
students['day'] = students['date_birth'].dt.day
students['month'] = students['date_birth'].dt.month
student_births = students[['student_id', 'day', 'month']]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "upiNeOGzbAot",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715208989914,
# !!     "user_tz": 360,
# !!     "elapsed": 205,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "771f8a61-8973-4b2b-f13b-53e07af12c9a"
# !! }}
student_births

# %%
# !! {"metadata":{
# !!   "id": "78NF9Us1bJhL"
# !! }}
attendance.set_index(['student_id', 'day', 'month'], inplace = True, drop = True)
student_births.set_index(['student_id', 'day', 'month'], inplace = True, drop = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 414
# !!   },
# !!   "id": "H7QKf3uVb0fy",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715209198301,
# !!     "user_tz": 360,
# !!     "elapsed": 221,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "9280228d-0e96-469a-9dc5-c0615e9704c5"
# !! }}
attendance

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 188
# !!   },
# !!   "id": "ipX6DRzSb2tB",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715209246103,
# !!     "user_tz": 360,
# !!     "elapsed": 195,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "cb1bcbfd-a99d-4b92-f75f-8eb0ae04e3b1"
# !! }}
student_births

# %%
# !! {"metadata":{
# !!   "id": "1AyOzSx4cEBP"
# !! }}
birthday_attendance = pd.concat([attendance, student_births], axis = 1, join = 'inner')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 194
# !!   },
# !!   "id": "c4ZZO8L_ccrt",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715209563586,
# !!     "user_tz": 360,
# !!     "elapsed": 205,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "8e20d54a-f059-4687-c270-6ad0db8e0b6a"
# !! }}
birthday_attendance

# %%
# !! {"metadata":{
# !!   "id": "X6QojevyewYI"
# !! }}
i = np.where(birthday_attendance['attendance'] == 'T', 1.0, 0.0).sum() / len(birthday_attendance)
d = {'rate' : [i]}
birthday_attendance_rate = pd.DataFrame(d)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 80
# !!   },
# !!   "id": "DdZsX7e8f94C",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715210323754,
# !!     "user_tz": 360,
# !!     "elapsed": 203,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "f853dfd4-3625-44c2-db5f-ab14d75e5095"
# !! }}
birthday_attendance_rate.round(2)

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyPqt3zbrFFkhAdrmU1xKRuY"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
