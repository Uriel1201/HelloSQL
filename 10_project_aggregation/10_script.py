# %%
# !! {"metadata":{
# !!   "id": "GVbsMX9zgdSw"
# !! }}
"""
#10 Project Aggregation
The projects table contains three columns: task_id, start_date, and end_date. The difference between end_date and start_date is 1 day for each row in the table. If task end dates are consecutive they are part of the same project. Projects do not overlap. Write a query to return the start and end dates of each project, and the number of days it took to complete. Order by ascending project duration, and ascending start date in the case of a tie.
"""

# %%
# !! {"metadata":{
# !!   "id": "zDg79swagdgW"
# !! }}
import pandas as pd
import numpy  as np

data = {'task_id'    : [1,2,3,4,5,6,7],
        'start_date' : ['01-OCT-20',
                        '02-OCT-20',
                        '03-OCT-20',
                        '13-OCT-20',
                        '14-OCT-20',
                        '28-OCT-20',
                        '30-OCT-20'],
         'end_date'  : ['02-OCT-20',
                        '03-OCT-20',
                        '04-OCT-20',
                        '14-OCT-20',
                        '15-OCT-20',
                        '29-OCT-20',
                        '31-OCT-20']
        }

projects = pd.DataFrame(data)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 289
# !!   },
# !!   "id": "-tbqB1qcg1hO",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715143411142,
# !!     "user_tz": 360,
# !!     "elapsed": 372,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "43e73119-69a7-493d-a9a1-8d0305b512c9"
# !! }}
projects

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "V3TtJpebg7d5",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715143562440,
# !!     "user_tz": 360,
# !!     "elapsed": 243,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "9f0e5866-d72a-497c-8d92-c9ef03064c90"
# !! }}
projects['start_date'] = pd.to_datetime(projects['start_date'])
projects['end_date'] = pd.to_datetime(projects['end_date'])

# %%
# !! {"metadata":{
# !!   "id": "Om-URAGNhd1Q",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715146725080,
# !!     "user_tz": 360,
# !!     "elapsed": 509,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "eb0662b5-3f0c-48b4-b513-2a3ba599bf77",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 410
# !!   }
# !! }}
projects

# %%
# !! {"metadata":{
# !!   "id": "i_I8cyD5tm7v",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148354812,
# !!     "user_tz": 360,
# !!     "elapsed": 159,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
openings = pd.DataFrame(projects[~projects.start_date.isin(projects['end_date'])]['start_date'])
openings.reset_index(inplace = True, drop = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "90RA2xxUzSAf",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148356970,
# !!     "user_tz": 360,
# !!     "elapsed": 201,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "2bca232c-31fb-475d-ceba-dcb151cd204e"
# !! }}
openings

# %%
# !! {"metadata":{
# !!   "id": "I1nL_okswGjh",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148439029,
# !!     "user_tz": 360,
# !!     "elapsed": 150,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
endings = pd.DataFrame(projects[~projects.end_date.isin(projects['start_date'])]['end_date'])
endings.reset_index(inplace = True, drop = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "o7xsgC5PwrVu",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148441212,
# !!     "user_tz": 360,
# !!     "elapsed": 14,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "cdd297fe-60df-4af5-eaf8-dc101bbdcd1d"
# !! }}
endings

# %%
# !! {"metadata":{
# !!   "id": "-vtxi08e0Gt3",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148655678,
# !!     "user_tz": 360,
# !!     "elapsed": 193,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
project_durations = pd.concat([openings, endings], axis = 1, join = 'inner')

# %%
# !! {"metadata":{
# !!   "id": "4j8bV0MI05vm",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148771654,
# !!     "user_tz": 360,
# !!     "elapsed": 199,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
project_durations['project_duration'] = project_durations['end_date'] - project_durations['start_date']

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 264
# !!   },
# !!   "id": "AOKbtVs51VaD",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715148869255,
# !!     "user_tz": 360,
# !!     "elapsed": 214,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "52124ba8-e5ab-42b5-fb21-1d135a475197"
# !! }}
project_durations.sort_values(by = 'project_duration', ascending = False)

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOFpbHkp4XWkGBpkrID/wPY"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
