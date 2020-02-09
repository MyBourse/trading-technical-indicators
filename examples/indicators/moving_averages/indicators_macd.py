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
from tradingti.indicators import MACD

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the OBV indicator
macd = MACD(df[df.index >= '2012-01-01'])

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
print('\nSignal:', macd.getSignal())