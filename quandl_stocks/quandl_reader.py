import quandl
from datetime import date, timedelta
import pandas as pd
import numpy as np

def read_data(quandl_api_key):
    quandl.ApiConfig.api_key = quandl_api_key
    
    print("Getting NASDAQ index data from Quandl...")
    ndq = quandl.get("NASDAQOMX/COMP-NASDAQ", trim_start='2019-11-01')

    # Extract dates and NASDAQ index values, convert to Pandas DataFrame
    ndq = ndq.loc[:,"Index Value"]

    print("Cleaning data...")
    ndq = ndq.reindex(pd.date_range(ndq.index[0], ndq.index[-1]), 
        fill_value=np.nan)
    
    # Reonvert Pandas Timestamp to datetime.date and pd.Series to pd.DataFrame
    ndq.index = [i.date() for i in ndq.index]

    # Interpolate missing values (Mostly saturdays and sundays, but there was one monday and one friday missing)
    ndq = ndq.interpolate()
    
    print("Done.")
    return ndq.to_frame()