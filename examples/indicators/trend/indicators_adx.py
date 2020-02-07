'''
File name: indicators_adx.py
    Example code rlated to the tradingti.indicator package.
    ADX Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 06.02.2020

Python Veadxon: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in paadxng the dates from csv
register_matplotlib_converters()

from tradingti.indicators import ADX
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the ADX indicator
adx = ADX(df.sort_index(ascending = True).loc['2012-01-01':, 
    ['High', 'Low', 'Close', 'Adj Close']])

# Save the plot of the calculated Technical Indicator
adx.getTiPlot().savefig('../figures/indicators_adx_example.png')

print('- Graph ../figures/indicators_adx_example.png saved.')

# Get ADX calculated data
print('\nADX data:\n', adx.getTiData())

# Get ADX value for a specific date
print('\nADX value at 2012-09-06:', adx.getTiValue('2012-09-06'))

# Get the most recent ADX value
print('\nADX value at', df.index[0], ':', adx.getTiValue())

# Get signal from ADX
signal = adx.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
