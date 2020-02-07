'''
File name: indicators_dmi.py
    Example code rlated to the tradingti.indicator package.
    DMI Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 06.02.2020

Python Vedmion: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in padming the dates from csv
register_matplotlib_converters()

from tradingti.indicators import DMI
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the DMI indicator
dmi = DMI(df.sort_index(ascending = True).loc['2012-01-01':, 
    ['High', 'Low', 'Close', 'Adj Close']])

# Save the plot of the calculated Technical Indicator
dmi.getTiPlot().savefig('../figures/indicators_dmi_example.png')

print('- Graph ../figures/indicators_dmi_example.png saved.')

# Get DMI calculated data
print('\nDMI data:\n', dmi.getTiData())

# Get DMI value for a specific date
print('\nDMI value at 2012-09-06:', dmi.getTiValue('2012-09-06'))

# Get the most recent DMI value
print('\nDMI value at', df.index[0], ':', dmi.getTiValue())

# Get signal from DMI
signal = dmi.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
