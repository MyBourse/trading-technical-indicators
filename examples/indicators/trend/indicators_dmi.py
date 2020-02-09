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
from tradingti.indicators import DMI

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the DMI indicator
dmi = DMI(df[df.index >= '2012-01-01'])

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
print('\nSignal:', dmi.getSignal())
