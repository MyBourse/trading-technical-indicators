'''
File name: __init__.py
    Trading Technical Indicators open source library, in python.
    `tradingti` package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

# PEP0440: https://www.python.org/dev/peps/pep-0440/
__version__ = '0.1.dev'

from .utils._system_information import showVersions

__all__ = ['utils', 'momentum', 'support_resistance', 'trend', 'volatility',
    'volume']