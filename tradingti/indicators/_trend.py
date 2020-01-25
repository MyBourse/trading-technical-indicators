'''
File name: _technical_indicator.py
    Trend type technical indicators implementation.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import pandas as pd
from ._technical_indicator import TI
from .._constants import *
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues


class SMA(TI):
    '''
    SMA Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains one column with the Adjusted
            Closed price of a given stock.
                
        sma_periods (object): The sma periods for which the rolling mean of the
            input data should be calculated. Is a list of integers, with one 
            (representing the long term SMA) or two (representing the short term
            and the long term SMA) members at most. Default values are [50, 200],
            50 for the short term and 200 for the long term.

    Attributes:
        _input_data (pandas dataframe): The input data to the Technical Indicator.
            
        _ti_data (pandas dataframe): The calculated values of the Technical
            indicator.
            
        _sma_periods (list of integers): The rolling mean windows.
                                
    Methods:
        _inputValidation(): Validates the input to the SMA Technical Indicator data.
    
        _calculateSMA(): Calculates the SMA for the given input data.
    
        getSignal(): Calculates and returns the signal of the technical indicator.
        
    Raises:
        TypeError()
        
    '''
    def __init__(self, df_data, sma_periods = [50, 200]):

        # Validate the input data, check tradingti.utils._data_validation module
        # for details
        data_validation = validateStockData(df_data)
        if data_validation is not None:
            raise(TypeError(data_validation))
            
        # Sort the input data and fill the missing values if any
        df_data = fillMissingValues(df_data)
        
        # Validate the SMA input (specific to the indicator)
        self._inputValidation(df_data, sma_periods)
        
        if len(sma_periods) == 1:
            colors_palette = ['red', 'black']
        else:
            colors_palette = ['red', 'blue', 'black']
            
        # If contains only one member, this is considered as long term SMA
        # If contains two members, then the larger value is considered as the long term SMA
        # and the shorter one is considered as the short term SMA
        self._sma_periods = sma_periods
        
        self._input_data = df_data
        self._ti_data = self._calculateSMA()
        
        # Parent class constructor (all job is done here, parent class provides the public
        # interface for accessing the data of the indicator)
        super().__init__(input_data = self._input_data, ti_data = self._ti_data, 
            indicator_name = 'SMA-' + str(sma_periods), 
            colors_palette = colors_palette)
        
    
    def _inputValidation(self, df_data, sma_periods):
        '''
        Validates the input to the SMA Technical Indicator data.
    
        Args:
            df_data (pandas dataframe): The input data to the Technical Indicator.
                Index is of type date. It contains one column with the Adjusted
                Closed price of a given stock.
                
            sma_periods (list of integers): The sma periods for which the rolling 
                mean of the input data should be calculated. Should be a list of 
                integers, with one or two members at most.

        Raises:
            TypeError()
            ValueError()

        Returns:
            -
        '''
        
        # Validate that the sma_periods is a list
        if not isinstance(sma_periods, list):
            message = 'sma_periods must be a list of one or two positive integers. '+\
                'sma_periods_type = ' + str(type(sma_periods)) + '.'          
            raise(TypeError(message))
        
        # Validate that the sma_periods is valid (not empty list of postive integers)
        if len(sma_periods) == 0 or len(sma_periods) > 2:
            message = 'sma_periods must contain one or two positive integers with values' +\
                'less than the number of the input data points. '+\
                'sma_periods = ' + str(sma_periods) + ' contains ' + str(len(sma_periods)) + '.'           
            raise(ValueError(message))
            
        for sma_period in sma_periods:
            if not isinstance(sma_period, int) or sma_period <= 0:
                message = 'sma_periods must contain only positive integers. '+\
                    'sma_periods = ' + str(sma_periods) + ', ' + str(sma_period) +\
                    ' is not a valid positive integer.' 
                raise ValueError(message)
        
        # Validate that sma_period is less than the number of the data points
        for sma_period in sma_periods:
            if len(df_data.index) < sma_period:
                message = 'sma_period should be less than the number of the data points.'+\
                    ' sma_period = ' + str(sma_period) + ' < ' + str(len(df_data.index)) + '.'
                raise(ValueError(message))
                
    
    def _calculateSMA(self):
        '''
        Calculates the SMA for the given input data.
    
        Args:
            -

        Raises:
            -

        Returns:
            pandas dataframe: The calculated values of the Technical
                indicator. Index is of type date. It contains one or two
                columns depending the requested sma periods.
        '''
    
        sma = pd.DataFrame(index = self._input_data.index)
        
        # Calculate SMA for each requested rolling window (concat results to a single dataframe)
        for sma_period in self._sma_periods:
            sma = pd.concat([sma, self._input_data.rolling(window = sma_period, min_periods = 1, center = False,
                win_type = None, on = None, axis = 0, closed = None).mean()], axis = 1)
        
        sma.columns = ['SMA-' + str(x) for x in self._sma_periods]
            
        return sma

    
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

        # Signal from long term SMA
        long_term_SMA = max(self._sma_periods)
        
        # Prices crosses the long term SMA
        if (self._input_data.iat[-2, 0] - self._ti_data.at[self._ti_data.index[-2], 'SMA-' + str(long_term_SMA)]) *\
           (self._input_data.iat[-1, 0] - self._ti_data.at[self._ti_data.index[-1], 'SMA-' + str(long_term_SMA)]) < 0:
            
            direction = self._input_data.iat[-1, 0] - self._ti_data.at[self._ti_data.index[-1], 'SMA-' + str(long_term_SMA)]
            if direction > 0:
                long_term_signal = TRADE_SIGNALS['Buy']
            elif direction < 0:
                long_term_signal = TRADE_SIGNALS['Sell']
        else:
            long_term_signal = TRADE_SIGNALS['Hold']
        
        # Signal from short term SMA
        if len(self._sma_periods) > 1:
            short_term_SMA = min(self._sma_periods)
            
            # SMAs crosses each other
            if (self._ti_data.at[self._ti_data.index[-2], 'SMA-' + str(short_term_SMA)] - \
                self._ti_data.at[self._ti_data.index[-2], 'SMA-' + str(long_term_SMA)]) * \
               (self._ti_data.at[self._ti_data.index[-1], 'SMA-' + str(short_term_SMA)] - \
                self._ti_data.at[self._ti_data.index[-1], 'SMA-' + str(long_term_SMA)]) < 0:
                
                direction = self._ti_data.at[self._ti_data.index[-1], 'SMA-' + str(short_term_SMA)] - \
                            self._ti_data.at[self._ti_data.index[-1], 'SMA-' + str(long_term_SMA)]
                            
                if direction > 0:
                    short_term_signal = TRADE_SIGNALS['Buy']
                elif direction < 0:
                    short_term_signal = TRADE_SIGNALS['Sell']
            else:
                short_term_signal = TRADE_SIGNALS['Hold']
                            
            # Merge signals.
            signal = long_term_signal + short_term_signal
            
            # Normalize signal if needed
            if abs(signal) == 2:
                signal = signal / 2
 
        return signal