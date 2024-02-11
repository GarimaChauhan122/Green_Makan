
import json
import pickle

import numpy as np

__heating_model = None
__cooling_model = None
__data_columns = None



def get_estimated_heating_load(relative_compactness,wall_area,roof_area,overall_height,orientation,glazing_area,glazing_area_distribution):
    x= np.zeros(7)
    x[0] = relative_compactness
    x[1] = wall_area
    x[2] = roof_area
    x[3] = overall_height
    x[4] = orientation
    x[5] = glazing_area
    x[6] = glazing_area_distribution

    return round(__heating_model.predict([x])[0], 2)

def get_estimated_cooling_load(relative_compactness,wall_area,roof_area,overall_height,orientation,glazing_area,glazing_area_distribution):
    x= np.zeros(7)
    x[0] = relative_compactness
    x[1] = wall_area
    x[2] = roof_area
    x[3] = overall_height
    x[4] = orientation
    x[5] = glazing_area
    x[6] = glazing_area_distribution

    return round(__cooling_model.predict([x])[0], 2)


def load_saved_models():

    print("loading saved models...start")

    global __data_columns

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __heating_model
    global __cooling_model

    with open("./artifacts/building_heating.pickle", 'rb') as f:
        __heating_model = pickle.load(f)


    with open("./artifacts/building_cooling.pickle", 'rb') as f:
        __cooling_model = pickle.load(f)

    print("loading saved models...done")


def trial():
    print("hello world")

if __name__ == '__main__':
    trial()
    load_saved_models()
    print(get_estimated_heating_load(0.98,294,110.25,7,2,0,0))
    print(get_estimated_cooling_load(0.98,294,110.25,7,2,0,0))
    print(get_estimated_heating_load(0.86,588,147,7,4,0.1,3))
    print(get_estimated_cooling_load(0.86,588,147,7,4,0.1,3))