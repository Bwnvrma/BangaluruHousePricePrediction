import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print('loading saved artifacts... Start')
    global __data_columns
    global __locations
    global __model

    with open("./Artifacts/columns.json ", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./Artifacts/bangaluru_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print('Loading the saved Artifacts is done.')

def get_location_names():
    load_saved_artifacts()
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('ist phase jp nagar', 1000, 3, 3))
    print(get_estimated_price('kalhalli', 1000, 2, 2))
    print(get_estimated_price('ejipura', 1000, 2, 2))