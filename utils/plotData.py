import matplotlib.dates as dates
import matplotlib.pyplot as plt
import os
from datetime import datetime, timezone, timedelta
from pandas.plotting import register_matplotlib_converters

def plotDaily(days = [], 
            valuesArr = [], 
            lineLabels = [],
            ylabel="Data", 
            xlabel="Date",
            title="Daily Data", 
            todayCol = '',
            showMax = [],
            dayLimiter = 30, 
            pltFmt = ['bo'], 
            saveFmt = ''):

    print("Creating daily plot: ", title, "...")
    register_matplotlib_converters()
    today = datetime.now().date()

    # Plot result
    i = 0
    for values in valuesArr:

        # If the user doesn't provide pltFmt, use the default
        if len(pltFmt) == 1:
            f = pltFmt[0]

        # If the user gives their own list and that list won't go out of range, use theirs
        elif (len(pltFmt) > 1):
            f = pltFmt[i]
        
        # Mark the maximum with a horizontal line, if requested
        if (not showMax == []) and showMax[i]:
            plt.axhline(y=max(values), color = f[0], linestyle = '--', label = str(int(max(values))))       
            plt.legend()

        # Perform plot
        if not lineLabels == []:
            plt.plot_date(days, values, fmt=f, tz=None, xdate=True, label = lineLabels[i])
            plt.legend()
        else:
            plt.plot_date(days, values, fmt=f, tz=None, xdate=True)

        i = i+1
    
    # Mark today with a vertical line, if requested
    if not todayCol == '':
        plt.axvline(x=today, color = todayCol, label = str(today))
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
        print("\tSaving plot to \n\t", fname, "...")
        plt.savefig(fname = fname, format=saveFmt)
    
    print("\tPrinting plot...")
    plt.show()
    print("Done.")