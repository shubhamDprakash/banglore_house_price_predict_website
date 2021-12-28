
import pickle
import json
import numpy as np

__data_columns = None
__model = None

def load_saved_artifacts():
    global __data_columns
    global __model
    if __data_columns is None:
        with open("artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
    if __model is None:
        with open('artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)

def predict_price(area_type, Immediately_availabile, location, bhk, sqft, bath, balcony):   
    __data_columns_np = np.array(__data_columns) 
    try:
        loc_index = np.where(__data_columns_np==location)[0][0]
    except:
        loc_index = -1
    try:
        area_type_index = np.where(__data_columns_np==area_type)[0][0]
    except:
        area_type_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    availability = lambda x : int(x=='yes')
    x[4] = availability(Immediately_availabile)
    if loc_index >= 0:
        x[loc_index] = 1
    if area_type_index >= 0:
        x[area_type_index] = 1

    return __model.predict([x])[0]


def get_location_and_areatype_names():
    locations = __data_columns[5:-3]
    area_type = __data_columns[-3:]
    return (locations,area_type)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_and_areatype_names())
    print(predict_price('carpet  area', 'yes','1st phase jp nagar',2, 1000, 2, 1))
    print(predict_price('built-up  area', 'No','ambalipura',2, 1000, 2, 1))