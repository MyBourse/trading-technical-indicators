'''
File name: _library_information.py
    Prints library information about the implemented technical indicators , 
    their type and version. Inidcators version is the version of the library in
    which latest changes in their implementation applied.
       
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 08.02.2020

Python Version: 3.6
'''

import tradingti

# Library Info. To be updated prior to each release by adding the new 
# indicators and updating versions for the updated indicators.
_LIBRARY_INFO = {
    'momentum': {
        'Fast Stochastic Oscillator (FSO)': 'v0.1', 
        'Slow Stochastic Oscillator (SSO)': 'v0.1', 
        'Relative Strength Index (RSI)': 'v0.1', 
        'Ichimoku Cloud (IC)': 'v0.1'
    }, 
    
    'support and resistance': {
        'Fibonacci Retracement (FR)': 'v0.1'
    }, 
    
    'trend': {
        'Simple Moving Average (SMA)': 'v0.1', 
        'Exponential Moving Average (EMA)': 'v0.1', 
        'Moving Average Convergence Divergence (MACD)': 'v0.1', 
        'Average Directional Movement Index (ADX)': 'v0.1', 
        'Directional Movement Index (DMI)': 'v0.1'
    }, 

    'volatility': {
        'Bollinger Bands (BB)': 'v0.1', 
        'Standard Deviation (SD)': 'v0.1'
    }, 

    'volume': {
        'On Balance Volume (OBV)': 'v0.1'
    }
}


def showLibraryInfo():
    '''
    Prints library information in the below format:
    <indicator type>
    - <indicator name>: <indicator version>
    
    Args:
        -

    Raises:
        -

    Returns:
        -
    '''
    
    print('\nTrading Technical Indicators Python Library: version', 
        tradingti.__version__)
    
    indicators_number = 0
    
    for type in _LIBRARY_INFO:
        print('\n', type, ' technical indicators:', sep = '')
        
        for indicator in _LIBRARY_INFO[type]:
            indicators_number += 1
            print('- ', indicator, ': ', _LIBRARY_INFO[type][indicator], 
                sep = '')

    print('\n', indicators_number, ' technical indicators included in version ',
        tradingti.__version__, ' of the library.\n', sep = '')