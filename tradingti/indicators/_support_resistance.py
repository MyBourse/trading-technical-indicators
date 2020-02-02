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
            Index is of type date. It contains the below columns:
            'Adj Close'
            
    Attributes:
        -
                                
    Methods:
        -
        
    Raises:
        - TypeError
        - ValueError
        
    '''
    def __init__(self, df_data):
        
        # Validate the input data, check tradingti.utils._data_validation module
        # for details
        data_validation = validateStockData(df_data)
        if data_validation is not None:
            raise(TypeError(data_validation))
            
        # Validate that all required input data are available
        if 'Adj Close' not in df_data.columns:
            raise(ValueError('Input \'Adj Close\' data are missing for FR ' +\
                'indicator use. Mandatory input data are: \'Adj Close\'.'))
            
        # Sort the input data and fill the missing values if any
        self._input_data = fillMissingValues(df_data)['Adj Close']

        # Parent class constructor (all job is done here, parent class provides 
        # the public interface for accessing the data of the indicator)
        super().__init__(input_data = self._input_data, 
            ti_data = self._calculateIndicator(df_data['Adj Close']),
            indicator_name = 'FR', lines_color = ['black', 'cornflowerblue', 
            'limegreen', 'tomato', 'orange', 'purple'], subplots = False)
        
        
    def _calculateIndicator(self, input_data):
        '''
        Calculates the FR for the given input data.

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
        
        total_max = input_data.max()
        total_min = input_data.min()
        
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
            integer: The Trading signal. Possible values are {'Hold': 0, 
                'Buy': -1, 'Sell': 1}. See TRADE_SIGNALS package constant.
        '''
        
        pass
