'''
File name: __init__.py
    Trading Technical Indicators open source library, in python.
    `indicators` package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 03.02.2020

Python Version: 3.6
'''

from ._trend import SMA, EMA, MACD
from ._momentum import FSO, SSO, RSI
from ._volatility import BB, SD
from ._support_resistance import FR

__all__ = ['SMA', 'EMA', 'MACD', 'FSO', 'SSO', 'RSI', 'BB', 'SD', 'FR']