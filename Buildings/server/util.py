import json
import pickle
import numpy as np

__facility_type = None
__data_columns = None
__model = None


def get_facility_type():
    return __facility_type


def get_estimated_site_eui(facility_type,year_factor,floor_area,elevation,avg_temp,cooling_degree_days,heating_degree_days,precipitation_inches):
    try:
        loc_index= __data_columns.index(facility_type.lower())

    except:
        loc_index= -1
    x= np.zeros(len(__data_columns))
    x[0] = year_factor
    x[1] = floor_area
    x[2] = elevation
    x[3] = avg_temp
    x[4] = cooling_degree_days
    x[5] = heating_degree_days
    x[6] = precipitation_inches
    if loc_index>=0:
        x[loc_index]=1


    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __facility_type

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __facility_type = __data_columns[7:]

    global __model

    with open("./artifacts/building_site_eui.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


def trial():
    print("hello world")

if __name__ == '__main__':
    trial()
    load_saved_artifacts()
    print(get_facility_type())
    print(get_estimated_site_eui('Grocery_store_or_food_market',1,61412,2.4,56.85,115,2960,16.59))

