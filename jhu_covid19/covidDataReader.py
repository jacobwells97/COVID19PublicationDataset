#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import io
from datetime import datetime
from utils import dictToDf

def buildDataset(path):
    '''
    Reads Johns Hopkins data to build global sums for cases, deaths, recovered for each day.
    Stores in a pandas df with format:
    {datetime.date: [confirmed, deaths, recovered]}
    '''
    print("Building COVID-19 dataset...")
    print("\tReading JHU csv files into pandas.DataFrame...")
    cDf = pd.read_csv(path + "time_series_covid19_confirmed_global.csv")
    dDf = pd.read_csv(path + "time_series_covid19_deaths_global.csv")
    rDf = pd.read_csv(path + "time_series_covid19_recovered_global.csv")
    
    print("\tBuilding sums across regions...")
    cDf = cDf.sum(axis = 0)
    dDf = dDf.sum(axis = 0)
    rDf = rDf.sum(axis = 0)

    print("\tMerging, cleaning, and renaming sums...")
    frames = [cDf, dDf, rDf]
    result = pd.concat(frames, axis = 1)
    result = result.rename(columns={0:'confirmed', 1:'dead', 2:'recovered'})
    result = result.drop(['Lat', 'Long'], axis = 0)
    # Convert string dates to datetime objects
    for i in result.index:
        result = result.rename(index={i:strToDatetime(i)})

    print("Done.")
    # Return concatenated data
    return result

def strToDatetime(str):
    dateStr = str.split("/")
    
    # Convert the date string tokens to int, return datetime object
    return datetime(2000+int(dateStr[2]), int(dateStr[0]), int(dateStr[1])).date()