# -*- coding: utf-8 -*-

##############################################################################################################
### Authors: Smit Mehta
### Python:  Version 3.7.3
### Details: Initial EDA on the brownfields_data_with_county_geoid
### Updates: 
###          
##############################################################################################################

# importing libraries
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# reading in the raw data
df = pd.read_csv('data/brownfields_data_with_county_geoid.csv')


# cleaning up the column names for easier future use
def format_colname(colname):
    colname = colname.lower()
    colname = colname.replace('#', 'num')
    colname = colname.replace('%', 'pct')
    colname = colname.replace('-', '_')
    colname = colname.replace(':', '')
    colname = colname.replace(' ', '_')
    colname = colname.replace('/', '_')
    colname = colname.replace('(', '')
    colname = colname.replace(')', '')
    colname = colname.replace('[', '')
    colname = colname.replace(']', '')
    colname = colname.replace('?', '')
    return colname


colnames = list(df.columns)
newcolnames = list()
for eachcol in colnames:
    newcolnames.append(format_colname(eachcol))


# switch the column names
df.columns = newcolnames


