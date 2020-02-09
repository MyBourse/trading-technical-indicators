'''
File name: indicators_ema.py
    Example code rlated to the tradingti.indicator package.
    SD Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import pandas as pd
from tradingti.indicators import SD

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the SD indicator
sd = SD(df[df.index >= '2012-01-01'], periods = 20)

# Save the plot of the calculated Technical Indicator
sd.getTiPlot().savefig('../figures/indicators_sd_20_example.png')

print('- Graph ../figures/indicators_sd_20_example.png saved.')

# Get SD calculated data
print('\nSD data:\n', sd.getTiData())

# Get SD value for a specific date
print('\nSD value at 2012-09-06:', sd.getTiValue('2012-09-06'))

# Get the most recent SD value
print('\nSD value at', df.index[0], ':', sd.getTiValue())

# Get signal from SD
print('\nSignal:', sd.getSignal())
        