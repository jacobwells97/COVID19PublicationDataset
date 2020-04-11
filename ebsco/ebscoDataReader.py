#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
from datetime import datetime, timezone, timedelta
import io
import pandas as pd
import xml.etree.ElementTree as ET
from utils import dictToDf

def buildDataset(fileName, setTag = ""):
    '''
    Parse and process EBSCO XML search results file.

    Parameters
    ----------
    fileName : str
        Absolute path to the xml file
    setTag : str
        Optional tag for this search, i.e. 'COVID-19' or 'Ebola'

    Returns
    -------
    DataFrame
        Column headers are datetime.date objects, 
        row 0 is new publications on that date, 
        row 1 is total publications up to that date
    '''
    print("Reading EBSCO search data...")

    print("\tReading entries from XML file...")
    entries = parseEbscoXml(fileName, setTag)

    print("\tWriting entries to CSV...")
    writeCSV('csvData.csv', entries)

    print("\tBuilding daily publication counts...")
    dailyCount = buildDailyPublishCount(entries)
    
    print("\tBuilding daily publication sums...")
    dailySum = buildDailyPublishSum(dailyCount)

    print("\tConverting to Pandas DataFrames....")
    countDf = dictToDf.convert(dailyCount)
    sumDf = dictToDf.convert(dailySum)

    print("\tCombining DataFrames...")
    countDf.loc[1] = sumDf.loc[0]

    print("Done.")
    # Return combined DataFrame
    return countDf

def parseEbscoXml(fileName, setTag = ""):
    tree = ET.parse(fileName)
    records = tree.getroot()
    entries = []

    for result in records:
        # Traverse headers
        header = result.find('header')
        infoMaster = header.find('controlInfo')

        artInfo = infoMaster.find('artinfo')
        # Get title     
        tig = artInfo.find('tig')
        title = tig.find('atl').text
        
        # Get author
        aug = artInfo.find('aug')
        aus = aug.findall('au')
        authors = []
        for au in aus:
            authors.append(au.text)
        
        
        # Get journal names
        jInfo = infoMaster.find('jinfo')
        journalName = jInfo.find('jtl').text
    
        # get language
        language = infoMaster.find('language').text
        
        # Get publication info
        pubInfo = infoMaster.find('pubinfo')
        dt = pubInfo.find('dt')
        att = dt.attrib
        year = att.get('year')
        month = att.get('month')
        day = att.get('day')
        date = datetime(int(year), int(month), int(day)).date()
        
        # Pack results into new entry
        entry = {'setTag': setTag,
                'title': title,
                'authors': authors,
                'datePublished': date,
                'authors': authors,
                'language': language,
                'journalName': journalName}
        
        # Add new entry to list of entries
        entries.append(entry)

    return entries


def writeCSV(outFileName, entries):
    with io.open(outFileName,'w', encoding="utf-8", newline = '') as out:
        csv_out=csv.writer(out)
    
        csv_out.writerow(['setTag',
                          'title',
                          'authors',
                          'datePublished',
                          'language',
                          'journalName'])
        for entry in entries:
            authors = '. '.join(entry['authors'])
            row = [entry['setTag'], 
                   entry['title'], 
                   authors,
                   entry['datePublished'],
                   entry['language'],
                   entry['journalName']]
            csv_out.writerow(row)

def buildDailyPublishCount(entries):
    # Build sum by date
    dailyCount = {}
    for entry in entries:
        # Get the current date
        date = entry['datePublished']
        
        # Intiialize a sum if necessary
        if not date in dailyCount:
            dailyCount[date] = 0
            
        # Add to the daily sum
        dailyCount[date] += 1 

    return dailyCount

def buildDailyPublishSum(dailyCount):
    dailySum = {}
    # For each day
    for date in dailyCount:
        # Sum all previous day counts
        for prevDate in dailyCount:
            # If this date is before or on the current date, 
            if prevDate <= date:
                # Initialize if necessary and add to sum
                if not date in dailySum:
                    dailySum[date] = 0
                dailySum[date] += dailyCount[prevDate]

    return dailySum



# %%
