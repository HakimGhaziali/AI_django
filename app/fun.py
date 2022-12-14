from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from autosklearn.regression import AutoSklearnRegressor
from autosklearn.metrics import mean_absolute_error as auto_mean_absolute_error
# load dataset



def fun():
    
    url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/auto-insurance.csv'
    dataframe = read_csv(url, header=None)
    data = dataframe.values
    data = data.astype('float32')
    X, y = data[:, :-1], data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    model = AutoSklearnRegressor(time_left_for_this_task=5*60, per_run_time_limit=30, n_jobs=8)
    model.fit(X_train, y_train)
    print(model.sprint_statistics())
    y_hat = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_hat)

    return mae
