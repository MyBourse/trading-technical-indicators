'''
File name: indicators_ema.py
    Example code rlated to the tradingti.indicator package.
    BB Trading Indicator.
           
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

from tradingti.indicators import BB
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the BB indicator, long term
bb = BB(df.sort_index(ascending = True).loc['2012-01-01':, ['Adj Close']], 
    term = 'long')

# Save the plot of the calculated Technical Indicator
bb.getTiPlot().savefig('../figures/indicators_bb_long_example.png')

print('- Graph ../figures/indicators_bb_long_example.png saved.')

# Calculate the BB indicator, short term
bb = BB(df.sort_index(ascending = True).loc['2012-01-01':, ['Adj Close']], 
    term = 'short')

# Save the plot of the calculated Technical Indicator
bb.getTiPlot().savefig('../figures/indicators_bb_short_example.png')

print('- Graph ../figures/indicators_bb_short_example.png saved.')


# Calculate the BB indicator, medium term
bb = BB(df.sort_index(ascending = True).loc['2012-01-01':, ['Adj Close']], 
    term = 'medium')

# Save the plot of the calculated Technical Indicator
bb.getTiPlot().savefig('../figures/indicators_bb_medium_example.png')

print('- Graph ../figures/indicators_bb_medium_example.png saved.')

# Get BB calculated data
print('\nBB data:\n', bb.getTiData())

# Get BB value for a specific date
print('\nBB value at 2012-09-06:', bb.getTiValue('2012-09-06'))

# Get the most recent BB value
print('\nBB value at', df.index[0], ':', bb.getTiValue())

# Get signal from BB
signal = bb.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')