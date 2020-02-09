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
from tradingti.indicators import RSI

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the RSI indicator
rsi = RSI(df[df.index >= '2012-01-01'])

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
print('\nSignal:', rsi.getSignal())
