'''
File name: indicators_ema.py
    Example code rlated to the tradingti.indicator package.
    EMA Trading Indicator.
           
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

from tradingti.indicators import EMA
import tradingti as tti

# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the EMA indicator for span period = 200
ema = EMA(df['Adj Close'].to_frame(), span_periods = [200])

# Save the plot of the calculated Technical Indicator
ema.getTiPlot().savefig('../figures/indicators_ema_200_example.png')

print('- Graph ../figures/indicators_ema_200_example.png saved.')

# Calculate the EMA indicator for the default span periods (short term ema = 26,
# long term ema = 200) 
ema = EMA(df[['Adj Close']])

# Save the plot of the calculated Technical Indicator
ema.getTiPlot().savefig('../figures/indicators_ema_50_200_example.png')
print('- Graph ../figures/indicators_ema_50_200_example.png saved.')

# Get EMA calculated data
print('\nEMA data:\n', ema.getTiData())

# Get EMA value for a specific date
print('\nEMA value at 2012-09-06:', ema.getTiValue('2012-09-06'))

# Get the most recent EMA value
print('\nEMA value at', df.index[0], ':', ema.getTiValue())

# Get signal from EMA
signal = ema.getSignal()
for key, value in tti.TRADE_SIGNALS.items(): 
    if value == signal:
        print('\nSignal:', key, '[', value, ']')
