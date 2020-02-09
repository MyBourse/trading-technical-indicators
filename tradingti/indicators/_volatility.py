'''
File name: _technical_indicator.py
    Volatility technical indicators implementation.
    Implements the following technical indicators:
    - Bollinger Bands (BB class)
    - Standard Deviation (SD class)
           
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
            Index is of type date. The indicator requires the following stock
            data: 'Adj Close'
            
        term (string): The term type for which the indicator should be
            calculated. It takes one of the following values: 'short', 'medium',
            'long'. Default value is 'medium'.
            
            - Short term: 10 day moving average, bands at 1.5 standard 
                deviations. (1.5 times the standard dev. +/- the SMA)
            - Medium term: 20 day moving average, bands at 2 standard deviations
            - Long term: 50 day moving average, bands at 2.5 standard deviations
            
    Attributes:
        _term (string): The term type for which the indicator should be
            calculated.
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data, term = 'medium'):
        
        # Validate and tranform the input data, check tradingti.utils.
        # _data_validation module for more details
        input_data = validateStockData(data = df_data, required_columns = 
            ['Adj Close'], indicator_name = 'BB')

        # Validate that term has one of the allowed values
        if str(term) not in ['short', 'medium', 'long']:
            raise(ValueError('Not allowed value for the \'term\' argument.' +\
                'It should be one of the following: \'short\', \'medium\', '+\
                '\'long\'. Value given is \'' + str(term) + '\'.'))

        self._term = {'short': (10, 1.5), 'medium': (20, 2.), 
            'long': (50, 2.5)}[term]
            
        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)    
        super().__init__(input_data = input_data, 
            ti_data = self._calculateIndicator(input_data),
            indicator_name = 'BB (sma = ' + str(self._term[0]) + ', std = ' + \
            str(self._term[1]) + ')', plotted_input_columns = ['Adj Close'], 
            y_label = 'Price', lines_color = ['black', 'cornflowerblue', 
            'limegreen', 'tomato'], subplots = False)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the BB technical indicator for the given input data.

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
        sma = SMA(input_data, sma_periods = [self._term[0]]).getTiData()
        sma.columns = ['SMA']
        
        # Calculate Standard Deviation
        std = input_data.std(axis = 0).values[0]
        
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
            tuple (string, integer): The Trading signal. Possible values are 
            ('Hold', 0), ('Buy', -1), ('Sell', 1). See TRADE_SIGNALS package 
            constant.
        '''
        
        # Price goes above upper band
        if self._input_data.iat[-1, 0] > self._ti_data.iat[-1, 1]:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        # Price goes below lower band
        elif self._input_data.iat[-1, 0] < self._ti_data.iat[-1, 2]:
            return ('Buy', TRADE_SIGNALS['Buy'])
            
        else:
            return ('Hold', TRADE_SIGNALS['Hold'])


class SD(TI):
    '''
    Standard Deviation (SD) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. The indicator requires the following stock
            data: 'Adj Close'
            
        periods (int): The past periods on which standard deviation should be 
            calculated for each date.

    Attributes:
        _periods (int): The past periods on which standard deviation should be 
            calculated for each date.
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data, periods = 20):
        
        # Validate and tranform the input data, check tradingti.utils.
        # _data_validation module for more details
        input_data = validateStockData(data = df_data, required_columns = 
            ['Adj Close'], indicator_name = 'SD')

        # Validate that periods is positive integer less than the number of the
        # input periods found in the dataframe.
        if type(periods) != int or periods <= 0 or periods > len(df_data.index):
            raise(ValueError('Not allowed value for the \'periods\' argument.'+\
                ' It should be integer > 0 and < ' + str(len(df_data.index))  +\
                '. Value given is ' + str(periods) + '.'))

        self._periods = periods
        
        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)    
        super().__init__(input_data = input_data, 
            ti_data = self._calculateIndicator(input_data),
            indicator_name = 'SD-' +  str(periods), plotted_input_columns = 
            ['Adj Close'], y_label = 'SD | Price', lines_color = ['black', 
            'cornflowerblue'], subplots = True)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the SD technical indicator for the given input data.

        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one column, the
                'SD'.
        '''

        sd = input_data.rolling(self._periods).std()
        sd.columns = ['SD']

        return sd
        
        
    def getSignal(self):
        '''
        Calculates and returns the signal of the technical indicator.
    
        Args:
            -

        Raises:
            -

        Returns:
            tuple (string, integer): The Trading signal. Possible values are 
            ('Hold', 0), ('Buy', -1), ('Sell', 1). See TRADE_SIGNALS package 
            constant.
        '''
        
        sma = SMA(self._input_data, sma_periods = [self._periods])
        
        # Price above average and volatility is high
        if self._input_data.iat[-1,0] > sma.getTiValue(self._input_data.index[-1]) and \
            self._ti_data.iat[-1,0] > 3:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        # Price below average and volatility is high
        if self._input_data.iat[-1,0] < sma.getTiValue(self._input_data.index[-1]) and \
            self._ti_data.iat[-1,0] > 3:
            return ('Buy', TRADE_SIGNALS['Buy'])
        
        return ('Hold', TRADE_SIGNALS['Hold'])
