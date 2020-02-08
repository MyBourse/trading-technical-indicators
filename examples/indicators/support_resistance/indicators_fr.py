'''
File name: indicators_ema.py
    Example code rlated to the tradingti.indicator package.
    FR Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import pandas as pd
from tradingti.indicators import FR

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the FR indicator
fr = FR(df[df.index >= '2012-01-01'])

# Save the plot of the calculated Technical Indicator
fr.getTiPlot().savefig('../figures/indicators_fr_example.png')

print('- Graph ../figures/indicators_fr_example.png saved.')

# Get FR calculated data
print('\nFR data:\n', fr.getTiData())

# Get FR value for a specific date
print('\nFR value at 2012-09-06:', fr.getTiValue('2012-09-06'))

# Get the most recent FR value
print('\nFR value at', df.index[0], ':', fr.getTiValue())

# Get signal from FR
print('\nSignal:', fr.getSignal())