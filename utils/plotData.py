import matplotlib.dates as dates
import matplotlib.pyplot as plt
import os
from datetime import datetime, timezone, timedelta
from pandas.plotting import register_matplotlib_converters

def plotDaily(dayData, ylabel="Data", xlabel="Date", title="Daily Data", todayCol = '', maxCol = '', dayLimiter = 30, fmt = 'bo', saveFmt = ''):
    register_matplotlib_converters()

    today = datetime.now().date()

    # Break dictionary into key list 
    days = list(dayData.keys())
    values = list(dayData.values())
    
    # Plot result
    plt.plot_date(days, values,fmt=fmt, tz=None, xdate=True)
    
    # Mark today with a vertical line
    if not todayCol == '':
        plt.axvline(x=today, color = todayCol, label = str(today))
        plt.legend()
    if not maxCol == '':
        plt.axhline(y=max(values), color = 'b', label = str(max(values)))
        plt.legend()
    # Limit plot to be within $dayLimiter days of today
    axes = plt.gca()
    axes.set_xlim([min(days), today + timedelta(days=dayLimiter)])
    
    # Label and show plot
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if not saveFmt == '':
        fname = os.getcwd() + os.path.sep + 'media' + os.path.sep + title.replace(' ', '_') + '.' + saveFmt
        plt.savefig(fname = fname, format=saveFmt)
    
    plt.show()