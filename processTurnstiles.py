''' 
Jonathan L Chu, 2020 for Metis SF20_DS18

Module to download and process
MTA turnstiles data for use in pandas
'''

import pandas as pd
import numpy as np

def get_data(week_nums):
    '''
    Downloads MTA turnstiles data from site, for specified week_nums.
    Returns pandas dataframe of raw data
    '''
    url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_{}.txt"
    dfs = []
    for week_num in week_nums:
        file_url = url.format(week_num)
        dfs.append(pd.read_csv(file_url))
    return pd.concat(dfs)

def processTurnstiles(df):
    '''
    Reads in raw MTA turnstile data as a pd dataframe
    Converts 'DATE' and 'TIME' cols to Datetime objects,
    adds 'ENTRIES_DIFF' col of count of entries (calculated 
    from 'ENTRIES' running total)

    Please be careful about the automatic outlier removal here
    
    Returns: pandas DataFrame
    '''
    weekdays = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    bins = [-1,3,7,11,15,19,24] #use a negative number at the beginning to ensure we do not lose midnight
    
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)
    
    # Convert Date and Time to Datetime objects
    df['DATETIME']= pd.to_datetime(  df['DATE'] +' '+ df['TIME'] )
    df['DATE'] = pd.to_datetime(df['DATE'])
    # Add weekday column. DOF = "day of week"
    df['DOF'] = [weekdays[df['DATETIME'][1].weekday()] for dstring in df.DATE.tolist()]
    
    # Add bins to organize entires by Hour of Day (HOD)
    df['HOD'] = [r.hour for r in df.TIMESTAMP] #hod = "hour of day"
    df['HODBIN'] = pd.cut(df['HOD'], bins)
    
    # Drop dupes
    df = df.drop_duplicates()
    
    # Create Station ID using Station Name and Line Name
    # sort each linename, since subway lines aren't listed in a consistent order
    lines = [''.join(sorted(line)) for line in df['LINENAME']] 
    df['STATION_ID']=df['STATION'] + "_" + pd.Series(lines)
    
    # Calculate Entry count from cumulative 'ENTRIES' column
    df['ENTRIES_DIFF']=( df.groupby(['STATION_ID','UNIT','SCP'],as_index=False)['ENTRIES']
                           .transform(pd.Series.diff)['ENTRIES']
                       )
    # Replace NaN/empties in 'ENTRIES_DIFF' with 0
    df.fillna(value={'ENTRIES_DIFF': 0}, inplace=True)
    
    # Convert 'ENTRIES_DIFF' to int()
    df = df.astype({'ENTRIES_DIFF': 'int32'}, copy=False)
    
    # Convert negative entries to positive values (from turnstiles counting down instead of up)
    df['ENTRIES_DIFF']=df['ENTRIES_DIFF'].abs()
    
    # Remove Outliers
    df = df[df.groupby(['STATION_ID','SCP'])['ENTRIES_DIFF'].apply(lambda x: np.abs(x - x.mean()) / x.std() < 3)]
    
    return df

def readProcessedData(path):
    '''
    Reads in ALREADY PROCESSED turnstile data from 'file' and drops old index,
    then converts DATETIME and DATE columns to datetime objects
    '''
    df = pd.read_csv(path)
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)
    
    # Convert Date and Time to Datetime objects
    df['DATETIME']= pd.to_datetime(  df['DATETIME'] )
    df['DATE'] = pd.to_datetime(df['DATE'])
    return df
