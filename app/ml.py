import numpy as np
import sklearn as sk
from numpy import random
from sklearn import linear_model


regr = linear_model.LinearRegression()

# Train the model using the training sets


X = random.rand(30,4)

Y = random.rand(30,1)


def fun1(m,n,b,v):
    
    regr.fit(X,Y)
    diabetes_y_pred = regr.predict([(m,n,b,v)])

    return diabetes_y_pred

