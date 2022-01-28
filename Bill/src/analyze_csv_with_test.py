import pandas as pd
import os
import datetime

# filename = 'L2A_Sendewicz.csv'
# emptyfilename = 'csv_data/file_with_no_data.csv'

testEpochTime = 1600763816518

def read_csv(filename):
    df = pd.read_csv(filename)
    return df

def test_read_csv():
    assert read_csv(filename).empty == False

def test_read_empty_csv():
    assert read_csv(emptyfilename).empty == True

def convert_epoch_to_human_readable(epochTime):
    hr_date = datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%Y-%m-%d %H:%M:%S.%f')
    return hr_date

def get_year(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%Y')

def test_get_year():
    assert get_year(testEpochTime) == "2020"

def get_month(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%m')

def test_get_month():
    assert get_month(testEpochTime) == "09"

def get_day(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%d')

def test_get_day():
    assert get_day(testEpochTime) == "22"

def get_hour(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%H')

def test_get_hour():
    assert get_hour(testEpochTime) == "08"

def get_minutes(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%M')

def test_get_minutes():
    assert get_minutes(testEpochTime) == "36"

def get_seconds(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%S')

def test_get_seconds():
    assert get_seconds(testEpochTime) == "56"

def get_milliseconds(epochTime):
    return datetime.datetime.fromtimestamp((epochTime/1000.0)).strftime('%f')

def test_get_milliseconds():
    assert get_milliseconds(testEpochTime) == "518000"
