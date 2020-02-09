'''
File name: indicators_sso.py
    Example code rlated to the tradingti.indicator package.
    SSO Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 29.01.2020

Python Version: 3.6
'''

import pandas as pd
from tradingti.indicators import SSO

# Future Warning matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the OBV indicator
sso = SSO(df[df.index >= '2012-01-01'])

# Save the plot of the calculated Technical Indicator
sso.getTiPlot().savefig('../figures/indicators_sso_example.png')
print('- Graph ../figures/indicators_sso_example.png saved.')

# Get SSO calculated data
print('\nSSO data:\n', sso.getTiData())

# Get SSO value for a specific date
print('\nSSO value at 2012-09-06:', sso.getTiValue('2012-09-06'))

# Get the most recent SSO value
print('\nSSO value at', df.index[0], ':', sso.getTiValue())

# Get signal from SSO
print('\nSignal:', sso.getSignal())
