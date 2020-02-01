'''
File name: indicators_sma.py
    Example code rlated to the tradingti.indicator package.
    SMA Trading Indicator.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 26.01.2020

Python Version: 3.6
'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
# Converters used in parsing the dates from csv
register_matplotlib_converters()

from tradingti.indicators import SMA
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the SMA indicator for sma period = 200
sma = SMA(df['Adj Close'].to_frame(), sma_periods = [200])

# Save the plot of the calculated Technical Indicator
sma.getTiPlot().savefig('../figures/indicators_sma_200_example.png')
print('- Graph ../figures/indicators_sma_200_example.png saved.')

# Calculate the SMA indicator for the default sma periods (short term sma = 50,
# long term sma = 200) 
sma = SMA(df[['Adj Close']])

# Save the plot of the calculated Technical Indicator
sma.getTiPlot().savefig('../figures/indicators_sma_50_200_example.png')
print('- Graph ../figures/indicators_sma_50_200_example.png saved.')

# Get SMA calculated data
print('\nSMA data:\n', sma.getTiData())

# Get SMA value for a specific date
print('\nSMA value at 2012-09-06:', sma.getTiValue('2012-09-06'))

# Get the most recent SMA value
print('\nSMA value at', df.index[0], ':', sma.getTiValue())

# Get signal from SMA
signal = sma.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')


