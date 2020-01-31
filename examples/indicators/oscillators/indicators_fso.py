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

from tradingti.indicators import FSO
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the FSO indicator
fso = FSO(df.sort_index(ascending = True).loc['2012-01-01':, ['High', 'Low', 'Close', 'Adj Close']])

# Save the plot of the calculated Technical Indicator
fso.getTiPlot().savefig('../figures/indicators_fso_example.png')
print('- Graph ../figures/indicators_fso_example.png saved.')

# Get FSO calculated data
print('\nFSO data:\n', fso.getTiData())

# Get FSO value for a specific date
print('\nFSO value at 2012-09-06:', fso.getTiValue('2012-09-06'))

# Get the most recent FSO value
print('\nFSO value at', df.index[0], ':', fso.getTiValue())

# Get signal from FSO
signal = fso.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
