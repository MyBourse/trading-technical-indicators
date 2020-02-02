'''
File name: indicators_fso.py
    Example code rlated to the tradingti.indicator package.
    IC Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 29.01.2020

Python Version: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in paicng the dates from csv
register_matplotlib_converters()

from tradingti.indicators import IC
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the IC indicator
ic = IC(df.sort_index(ascending = True).loc['2012-01-01':, ['High', 'Low', 'Close', 'Adj Close']])

# Save the plot of the calculated Technical Indicator
ic.getTiPlot().savefig('../figures/indicators_ic_example.png')

print('- Graph ../figures/indicators_ic_example.png saved.')

# Get IC calculated data
print('\nIC data:\n', ic.getTiData())

# Get IC value for a specific date
print('\nIC value at 2012-09-06:', ic.getTiValue('2012-09-06'))

# Get the most recent IC value
print('\nIC value at', df.index[0], ':', ic.getTiValue())

# Get signal from IC
signal = ic.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')