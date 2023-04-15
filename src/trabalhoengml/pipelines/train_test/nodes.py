"""
This is a boilerplate pipeline 'train_test'
generated using Kedro 0.18.7
"""
import pycaret.classification as pycc
from sklearn.metrics import f1_score ,log_loss
from pycaret.classification import * 

def train_model_lr(df,n_folds):
    pycc.setup(df, target = 'shot_made_flag')
    clf = pycc.create_model('lr', fold = n_folds)
    return clf

def train_model_ada(df,n_folds):
    pycc.setup(df, target = 'shot_made_flag')
    clf = pycc.create_model('ada', fold = n_folds)
    return clf

def report_model(clf,data_test):
    X = data_test.drop(columns=['shot_made_flag']).copy()
    y_pred = clf.predict(X)
    y_true = data_test['shot_made_flag']
    return {
        'f1_mean': {'value': float(f1_score(y_true, y_pred)), 'step':1},
        'log_loss_mean': {'value': float(log_loss(y_true, y_pred)), 'step':1},
    }
