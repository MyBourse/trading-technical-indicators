'''
File name: indicators_ema.py
    Example code rlated to the tradingti.indicator package.
    SD Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in parsing the dates from csv
register_matplotlib_converters()

from tradingti.indicators import SD
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the SD indicator, long term
sd = SD(df.sort_index(ascending = True).loc['2012-01-01':, ['Adj Close']], 
    periods = 20)

# Save the plot of the calculated Technical Indicator
sd.getTiPlot().savefig('../figures/indicators_sd_20_example.png')

print('- Graph ../figures/indicators_sd_20_example.png saved.')

# Get SD calculated data
print('\nSD data:\n', sd.getTiData())

# Get SD value for a specific date
print('\nSD value at 2012-09-06:', sd.getTiValue('2012-09-06'))

# Get the most recent SD value
print('\nSD value at', df.index[0], ':', sd.getTiValue())

# Get signal from SD
signal = sd.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
        