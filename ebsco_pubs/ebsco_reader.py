import csv
from datetime import datetime, timezone, timedelta
import io
import pandas as pd
import xml.etree.ElementTree as ET
from utils import dictToDf
import numpy as np

def read_data(fileName, setTag = ""):
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

    entries = parseEbscoXml(fileName, setTag)

    print("Cleaning data...")
    dailyCount = buildDailyPublishCount(entries)

    # Convert to pandas DF with dats as row names
    countDf = dictToDf.convert(dailyCount).transpose()

    # Add missing dates
    countDf = countDf.reindex(pd.date_range(countDf.index[0], countDf.index[-1]), 
        fill_value=0)

    countDf = buildDailyPublishSum(countDf)

    countDf = countDf.rename(columns={0: "Publications"})

    # Return combined DataFrame
    return countDf

def parseEbscoXml(fileName, setTag = ""):
    print("Reading EBSCO search data...")

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
    today = datetime.today().date()
    # Build sum by date
    dailyCount = {}
    for entry in entries:
        # Get the current date
        date = entry['datePublished']

        # Don't accept future publications
        if date < today:       
            # Intiialize a sum if necessary
            if not date in dailyCount:
                dailyCount[date] = 0
                
            # Add to the daily sum
            dailyCount[date] += 1 

    return dailyCount

def buildDailyPublishSum(count):
    count.index = [i.date() for i in count.index]
    i0 = count.index[0]

    count['Total Published'] = [count.loc[i0:i].sum()[0] for i in count.index]

    return count