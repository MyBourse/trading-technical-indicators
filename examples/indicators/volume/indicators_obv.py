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
from tradingti.indicators import OBV

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the OBV indicator
obv = OBV(df[df.index >= '2012-01-01'])

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
print('\nSignal:', obv.getSignal())
