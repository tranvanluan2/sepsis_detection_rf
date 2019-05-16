import sys
import numpy as np

import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

from utils import *


def load_sepsis_model():
    filename = 'rf_model'
    
    loaded_model = joblib.load(filename)

    return loaded_model





def get_sepsis_score(data, model):
    #read challenge data
    #data = get_data_from_file(input_file)
    # X_test, _ = prepare_input_for_lstm_crf([data], is_training=False)

    #impute missing data

    data = impute_missing_data(data)
    features = prepare_test_data_random_forest(data)
    # print(features)

    predictions = model.predict_proba([features])
    
    score = predictions[0][1]

    if score >=0.54:
        label = 1
    else:
        label = 0
    return score, label
