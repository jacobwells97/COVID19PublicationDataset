#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os
import io
from datetime import datetime

def buildDataset(path):
    '''
    Reads Johns Hopkins data to build global sums for cases, deaths, recovered for each day.
    Stores in a pandas df with format:
    {datetime.date: [confirmed, deaths, recovered]}
    '''
    # Build paths to Johns Hopkins data
    slash = os.path.sep
    cPath = path + "time_series_covid19_confirmed_global.csv"
    dPath = path + "time_series_covid19_deaths_global.csv"
    rPath = path + "time_series_covid19_recovered_global.csv"
    
    # Read JHU csv's into pandas dataframes
    cDf = pd.read_csv(cPath)
    dDf = pd.read_csv(dPath)
    rDf = pd.read_csv(rPath)
    
    cDaily = {}
    dDaily = {}
    rDaily = {}

    for date in cDf:     
        if not (date == 'Province/State' or date == 'Country/Region' or date == 'Lat' or date == 'Long'):
            # Convert date string to datetime object
            dateSplit = date.split('/')
            month = dateSplit[0]
            day = dateSplit[1]
            year = dateSplit[2]
            
            # Sum counts across all regions to get global count
            cSumGlob = sum(cDf[date])
            dSumGlob = sum(dDf[date])
            rSumGlob = sum(rDf[date])
            
            # Log 1st row = global cases, 2nd row = global deaths, 3rd row = global recovered under current date
            dt = datetime(2000+int(year), int(month), int(day)).date()
            cDaily[dt] = cSumGlob
            dDaily[dt] = dSumGlob
            rDaily[dt] = rSumGlob

    return cDaily, dDaily, rDaily

