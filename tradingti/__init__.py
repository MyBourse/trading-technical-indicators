'''
File name: __init__.py
    Trading Technical Indicators open source library, in python.
    `tradingti` package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 08.02.2020

Python Version: 3.6
'''

__version__ = '0.0.2'

from ._constants import *
from .utils._system_information import showSystemInfo
from .utils._library_information import showLibraryInfo

__all__ = ['utils', 'indicators', 'TRADE_SIGNALS']