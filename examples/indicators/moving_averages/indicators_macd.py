'''
File name: indicators_ema.py
    Example code rlated to the tradingti.indicator package.
    MACD Trading Indicator.
           
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

from tradingti.indicators import MACD
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the MACD indicator
macd = MACD(df.sort_index(ascending = True).loc['2012-01-01':, ['Adj Close']])

# Save the plot of the calculated Technical Indicator
macd.getTiPlot().savefig('../figures/indicators_macd_example.png')

print('- Graph ../figures/indicators_macd_example.png saved.')

# Get MACD calculated data
print('\nMACD data:\n', macd.getTiData())

# Get MACD value for a specific date
print('\nMACD value at 2012-09-06:', macd.getTiValue('2012-09-06'))

# Get the most recent MACD value
print('\nMACD value at', df.index[0], ':', macd.getTiValue())

# Get signal from MACD
signal = macd.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')