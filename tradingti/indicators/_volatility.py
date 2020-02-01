'''
File name: _technical_indicator.py
    Volatility technical indicators implementation.
    Implements the following technical indicators:
    - Bollinger Bands (BB class)
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import pandas as pd
from ._technical_indicator import TI
from ._trend import SMA
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues
from .._constants import *


class BB(TI):
    '''
    Bollinger Bands (BB) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains the below columns:
            'Adj Close'
            
        term (string): The term type for which the indicator should be
            calculated. It takes one of the following values: 'short', 'medium',
            'long'. Default value is 'medium'.
            
            - Short term: 10 day moving average, bands at 1.5 standard 
                deviations. (1.5 times the standard dev. +/- the SMA)
            - Medium term: 20 day moving average, bands at 2 standard deviations.
            - Long term: 50 day moving average, bands at 2.5 standard deviations.
            
    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        - TypeError
        - ValueError
        
    '''
    def __init__(self, df_data, term = 'medium'):
        
        # Validate the input data, check tradingti.utils._data_validation module
        # for details
        data_validation = validateStockData(df_data)
        if data_validation is not None:
            raise(TypeError(data_validation))
            
        # Validate that all required input data are available
        if 'Adj Close' not in df_data.columns:
            raise(ValueError('Input \'Adj Close\' data are missing for BB ' +\
                'indicator use. Mandatory input data are: \'Adj Close\'.'))
                
        # Validate that term has one of the allowed values
        if str(term) not in ['short', 'medium', 'long']:
            raise(ValueError('Not allowed value for the \'term\' argument.' +\
                'It should be one of the following: \'short\', \'medium\', '+\
                '\'long\'. Value given is \'' + str(term) + '\'.'))

        self._term = {'short': (10, 1.5), 'medium': (20, 2.), 
            'long': (50, 2.5)}[term]
            
        # Sort the input data and fill the missing values if any
        self._input_data = fillMissingValues(df_data)['Adj Close']

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)
        super().__init__(input_data = self._input_data, 
            ti_data = self._calculateIndicator(df_data['Adj Close']),
            indicator_name = 'BB (sma = ' + str(self._term[0]) + ', std = ' +\
            str(self._term[1]) + ')', lines_color = ['black', 'cornflowerblue', 
            'limegreen', 'tomato'], subplots = False)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the BB for the given input data.

        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains three columns, the
                'SMA', the 'Upper Band' and the 'Lower Band'.
        '''
        
        # Calculate Simple Moving Average
        sma = SMA(input_data.to_frame(), sma_periods = [self._term[0]]).getTiData()
        sma.columns = ['SMA']
        
        # Calculate Standard Deviation
        std = input_data.to_frame().std(axis = 0).values[0]
        
        upper_band = sma + self._term[1]*std
        upper_band.columns = ['Upper Band']
        
        lower_band = sma - self._term[1]*std
        lower_band.columns = ['Lower Band']
        
        # Indicator holds the MACD and the Signal Line data
        bb = pd.concat([sma, upper_band, lower_band], axis = 1)
        
        return bb  
        
        
    def getSignal(self):
        '''
        Calculates and returns the signal of the technical indicator.
    
        Args:
            -

        Raises:
            -

        Returns:
            integer: The Trading signal. Possible values are {'Hold': 0, 
                'Buy': -1, 'Sell': 1}. See TRADE_SIGNALS package constant.
        '''
        
        # Price goes above upper band
        if self._input_data.iat[-1, 0] > self._ti_data.iat[-1, 1]:
            return TRADE_SIGNALS['Sell']
            
        # Price goes below lower band
        elif self._input_data.iat[-1, 0] < self._ti_data.iat[-1, 2]:
            return TRADE_SIGNALS['Buy']
            
        else:
            return TRADE_SIGNALS['Hold']
