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
from tradingti.indicators import ADX

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the ADX indicator
adx = ADX(df[df.index >= '2012-01-01'])

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
print('\nSignal:', adx.getSignal())
