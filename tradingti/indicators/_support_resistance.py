'''
File name: _technical_indicator.py
    Support-Resistance technical indicators implementation.
    Implements the following technical indicators:
    - Fibonacci Retracement (FR class)
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 02.02.2020

Python Version: 3.6
'''

import pandas as pd
from ._technical_indicator import TI
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues
from .._constants import *


class FR(TI):
    '''
    Fibonacci Retracement (FR) Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. The indicator requires the following stock
            data: 'Adj Close'
            
    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        TypeError (Raised from validateStockData method)
        ValueError (Raised from validateStockData method)
        
    '''
    def __init__(self, df_data):
       
        # Validate and tranform the input data, check tradingti.utils.
        # _data_validation module for more details
        input_data = validateStockData(data = df_data, required_columns = 
            ['Adj Close'], indicator_name = 'FR')

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)    
        super().__init__(input_data = input_data, 
            ti_data = self._calculateIndicator(input_data),
            indicator_name = 'FR', plotted_input_columns = ['Adj Close'], 
            lines_color = ['black', 'limegreen', 'brown', 'peru', 
            'orange', 'red'], subplots = False)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the FR technical indicator for the given input data.

        Args:
            input_data (pandas dataframe): The input data to the Technical 
                Indicator.

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains five columns, the
                resistance levels 'RL0', 'RL1', 'RL2', 'RL3' and 'RL4'.
        '''

        total_max = input_data['Adj Close'].max()
        total_min = input_data['Adj Close'].min()

        max_min_difference = total_max - total_min
        
        retracement_levels = [total_max - c*max_min_difference for c in 
            [0.0, 0.236, 0.382, 0.618, 1.0]]
            
        fr = pd.DataFrame(index = input_data.index, 
            data = [[retracement_levels[i] for i in 
            range(len(retracement_levels))]]*len(input_data.index), 
            columns = ['RL' + str(i) for i in range(len(retracement_levels))])
        
        return fr
        
        
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
        
        # Moves from in RL to another in downward direction
        if self._input_data.iat[-2,0] > self._ti_data.iat[-2,3] and\
            self._input_data.iat[-1,0] < self._ti_data.iat[-1,3]:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        if self._input_data.iat[-2,0] > self._ti_data.iat[-2,2] and\
            self._input_data.iat[-1,0] < self._ti_data.iat[-1,2]:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        if self._input_data.iat[-2,0] > self._ti_data.iat[-2,1] and\
            self._input_data.iat[-1,0] < self._ti_data.iat[-1,1]:
            return ('Sell', TRADE_SIGNALS['Sell'])
            
        # Moves from in RL to another in the upward direction
        if self._input_data.iat[-2,0] < self._ti_data.iat[-2,3] and\
            self._input_data.iat[-1,0] > self._ti_data.iat[-1,3]:
            return ('Buy', TRADE_SIGNALS['Buy'])
            
        if self._input_data.iat[-2,0] < self._ti_data.iat[-2,2] and\
            self._input_data.iat[-1,0] > self._ti_data.iat[-1,2]:
            return ('Buy', TRADE_SIGNALS['Buy'])
            
        if self._input_data.iat[-2,0] < self._ti_data.iat[-2,1] and\
            self._input_data.iat[-1,0] > self._ti_data.iat[-1,1]:
            return ('Buy', TRADE_SIGNALS['Buy'])
            
        return ('Hold', TRADE_SIGNALS['Hold'])
