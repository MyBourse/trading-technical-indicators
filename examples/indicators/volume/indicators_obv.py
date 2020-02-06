'''
File name: indicators_obv.py
    Example code rlated to the tradingti.indicator package.
    OBV Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 06.02.2020

Python Veobvon: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in paobvng the dates from csv
register_matplotlib_converters()

from tradingti.indicators import OBV
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the OBV indicator
obv = OBV(df.sort_index(ascending = True).loc['2012-01-01':, 
    ['Volume', 'Adj Close']])

# Save the plot of the calculated Technical Indicator
obv.getTiPlot().savefig('../figures/indicators_obv_example.png')

print('- Graph ../figures/indicators_obv_example.png saved.')

# Get OBV calculated data
print('\nOBV data:\n', obv.getTiData())

# Get OBV value for a specific date
print('\nOBV value at 2012-09-06:', obv.getTiValue('2012-09-06'))

# Get the most recent OBV value
print('\nOBV value at', df.index[0], ':', obv.getTiValue())

# Get signal from OBV
signal = obv.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
