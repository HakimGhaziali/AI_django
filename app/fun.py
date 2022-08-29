from pprint import pprint

import sklearn.datasets
import sklearn.metrics
import autosklearn.regression
import numpy as np

X= np.random.rand(3,2)
y = np.random.rand(3,2)


automl = autosklearn.regression.AutoSklearnRegressor(
    time_left_for_this_task=120,
    per_run_time_limit=30,
)
automl.fit(X, y, dataset_name='diabetes')




def funn():
    
    return automl.leaderboard()
