'''
File name: indicators_fso.py
    Example code rlated to the tradingti.indicator package.
    FSO Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 29.01.2020

Python Version: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in parsing the dates from csv
register_matplotlib_converters()

from tradingti.indicators import RSI
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the RSI indicator
rsi = RSI(df.sort_index(ascending = True).loc['2011-01-01':, ['Adj Close']])

# Save the plot of the calculated Technical Indicator
rsi.getTiPlot().savefig('../figures/indicators_rsi_example.png')

print('- Graph ../figures/indicators_rsi_example.png saved.')

# Get RSI calculated data
print('\nRSI data:\n', rsi.getTiData())

# Get RSI value for a specific date
print('\nRSI value at 2012-09-06:', rsi.getTiValue('2012-09-06'))

# Get the most recent RSI value
print('\nRSI value at', df.index[0], ':', rsi.getTiValue())

# Get signal from RSI
signal = rsi.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
