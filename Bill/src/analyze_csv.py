import pandas as pd
import os
import datetime

# filename = './Bill/csv_data/L2A_Sendewicz.csv'
filename = 'L2A_Sendewicz.csv'

def read_csv(filename):
    df = pd.read_csv(filename)
    return df

def convert_epoch_to_human_readable(epochTime):
    hr_date = datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%Y-%m-%d %H:%M:%S.%f')
    return hr_date

def get_year(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%Y')

def get_month(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%m')

def get_day(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%d')

def get_hour(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%H')

def get_minutes(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%M')

def get_seconds(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%S')

def get_milliseconds(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%f')


epochTime = 1600763816518
print(convert_epoch_to_human_readable(epochTime))
print(get_year(epochTime))
print(get_month(epochTime))
print(get_day(epochTime))
print(get_hour(epochTime))
print(get_minutes(epochTime))
print(get_seconds(epochTime))
print(get_milliseconds(epochTime))