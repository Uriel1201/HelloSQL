# %%
# !! {"metadata":{
# !!   "id": "jGvogQ5nRWt5"
# !! }}
"""

"""

# %%
# !! {"metadata":{
# !!   "id": "YpBxJE_ORYO8",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715387708398,
# !!     "user_tz": 360,
# !!     "elapsed": 659,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np

data = {'id'    : [1,2,3,4,5,6],
        'score' : [3.5,3.65,4.0,3.85,4.0,3.65]
       }

scores = pd.DataFrame(data)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 237
# !!   },
# !!   "id": "mSl71diUSqaN",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715387710830,
# !!     "user_tz": 360,
# !!     "elapsed": 204,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "6a2e9b87-4752-4b34-ef5a-954caeb5eb36"
# !! }}
scores

# %%
# !! {"metadata":{
# !!   "id": "EFxWpyAKYOnk",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715390102973,
# !!     "user_tz": 360,
# !!     "elapsed": 182,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def rank_serie(serie):
    copy = np.array(serie.drop_duplicates())
    count_list = [np.sum(copy >= s) for s in serie]
    array_list = np.array(list(zip(serie, count_list)))
    return array_list

# %%
# !! {"metadata":{
# !!   "id": "TnEtR58lI3NB",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715390211233,
# !!     "user_tz": 360,
# !!     "elapsed": 166,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
score_id = scores['score']
rank_score = pd.DataFrame(rank_serie(score_id), columns=['score', 'rank'])

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 237
# !!   },
# !!   "id": "N9VmSFTxN9a0",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715390213270,
# !!     "user_tz": 360,
# !!     "elapsed": 191,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "fb4b6777-5c23-45e1-9ddb-53ca48986c3f"
# !! }}
rank_score

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyO5EmT3itbVwBrJuEn86hXy"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
