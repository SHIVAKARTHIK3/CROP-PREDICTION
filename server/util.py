import pickle

import pandas as pd

__model=None

__data_columns=None
Data=pd.read_csv("C:/Users/SHIVA KARTHIK P/OneDrive/Desktop/final_crop.csv")
selected_state=dict(zip(Data["State"],Data["state_n"]))
selected_crop=dict(zip(Data['Crop'],Data['crop_n']))
selected_season=dict(zip(Data['Season'],Data['season_n']))
selected_soil=dict(zip(Data['Soil'],Data['soil_n']))
def predict_crop(state, rainfall, season, soil):
    global __model
    state_n = selected_state[state]
    season_n = selected_season[season]
    soil_n = selected_soil[soil]
    crop_names = set(Data['Crop'])
    crop_list = [*crop_names]
    crop_list.sort()
    with open("C:/crop_prediction/server/artifacts/Crop_prediction.pickle", "rb") as f:
        __model = pickle.load(f)
    val = __model.predict([[state_n, rainfall, season_n, soil_n ]])
    val = int(val)
    return crop_list[val]
def get_state_names():
    global __states
    s_names=set(Data['State'])
    state_list=[*s_names, ]
    state_list.sort()
    __states=state_list
    return __states
def get_soil_names():
    global __soil
    soil_names=set(Data['Soil'])
    soil_list=[*soil_names, ]
    soil_list.sort()
    __soil=soil_list
    return __soil

if __name__=='__main__':
    print(predict_crop("Andaman and Nicobar Islands",	2950,	"Whole Year",	"RedsandyLoam"))
