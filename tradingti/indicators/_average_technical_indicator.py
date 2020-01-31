'''
File name: _average_technical_indicator.py
    Parent class for all the technical indicators of average type
    (SMA, EMA).
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 27.01.2020

Python Version: 3.6
'''

from ._technical_indicator import TI
from .._constants import *
from ..utils._data_validation import validateStockData
from ..utils._data_preprocessing import fillMissingValues


class AverageTI(TI):
    '''
    Average Technical Indicator class implementation.

    Args:
        df_data (pandas dataframe): The input data to the Technical Indicator.
            Index is of type date. It contains one column with the Adjusted
            Closed price of a given stock.
            
        calculate_MA (object method): Reference to a method in child class, 
            which calculates the MA for the given input data.
        
        indicator_name (string): The name of the Technical Indicator.
        
        lines_color (list of matplotlib colors): The colors to be used
            when generating the plot for a Technical Indicator. Default value is
            None (default colors will be used).
                
        periods (object): The periods (rolling windows, span periods, etc.) for 
            which the technical indicator is calculated. Is a list of integers, 
            with one (representing the long term MA) or two (representing the short term
            and the long term MA) members at most.

    Attributes:
        _input_data (pandas dataframe): The input data to the Technical Indicator.
            
        _ti_data (pandas dataframe): The calculated values of the Technical
            indicator.
            
        _indicator_name (string): The name of the Technical Indicator.
            
        _periods (list of integers): The periods (rolling windows, span periods, etc.) 
            for which the technical indicator is calculated.
                                
    Methods:
        _inputValidation(): Validates the input to the SMA Technical Indicator data.
    
        getSignal(): Calculates and returns the signal of the technical indicator.
        
    Raises:
        TypeError()
        
    '''
    
    def __init__(self, df_data, calculate_MA, indicator_name, lines_color,
        periods):

        # Validate the input data, check tradingti.utils._data_validation module
        # for details
        data_validation = validateStockData(df_data)
        if data_validation is not None:
            raise(TypeError(data_validation))
        
        # Validate that all required input data are available
        if 'Adj Close' not in df_data.columns:
            raise(ValueError('Input \'Adj Close\' data are missing for MA indicator use. '+\
                'Mandatory input data are: \'Adj Close\'.'))
            
        # Sort the input data and fill the missing values if any
        df_data = fillMissingValues(df_data)
        
        # Validate the MA input (specific to the indicator)
        self._inputValidation(df_data, periods)
            
        # If contains only one member, this is considered as long term SMA
        # If contains two members, then the larger value is considered as the long term SMA
        # and the shorter one is considered as the short term SMA
        self._periods = periods
        
        self._indicator_name = indicator_name
        
        self._input_data = df_data
        self._ti_data = calculate_MA(self._input_data)
        
        # Parent class constructor (all job is done here, parent class provides the public
        # interface for accessing the data of the indicator)
        super().__init__(input_data = self._input_data, ti_data = self._ti_data, 
            indicator_name = indicator_name, lines_color = lines_color)
        
    
    def _inputValidation(self, df_data, periods):
        '''
        Validates the input to the MA Technical Indicator data.
    
        Args:
            df_data (pandas dataframe): The input data to the Technical Indicator.
                Index is of type date. It contains one column with the Adjusted
                Closed price of a given stock.
                
            periods (object): The periods (rolling windows, span periods, etc.) for 
            which the technical indicator is calculated.

        Raises:
            TypeError()
            ValueError()

        Returns:
            -
        '''
        
        # Validate that the periods is a list
        if not isinstance(periods, list):
            message = 'periods must be a list of one or two positive integers. '+\
                'periods_type = ' + str(type(periods)) + '.'          
            raise(TypeError(message))
        
        # Validate that the periods is valid (not empty list of postive integers)
        if len(periods) == 0 or len(periods) > 2:
            message = 'periods must contain one or two positive integers with values' +\
                'less than the number of the input data points. '+\
                'periods = ' + str(periods) + ' contains ' + str(len(periods)) + '.'           
            raise(ValueError(message))
            
        for period in periods:
            if not isinstance(period, int) or period <= 0:
                message = 'periods must contain only positive integers. '+\
                    'periods = ' + str(periods) + ', ' + str(period) +\
                    ' is not a valid positive integer.' 
                raise ValueError(message)
        
        # Validate that period is less than the number of the data points
        for period in periods:
            if len(df_data.index) < period:
                message = 'period should be less than the number of the data points.'+\
                    ' period = ' + str(period) + ' < ' + str(len(df_data.index)) + '.'
                raise(ValueError(message))

    
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

        # Signal from long term MA
        long_term_MA = max(self._periods)
        
        # Prices crosses the long term MA
        if (self._input_data.iat[-2, 0] - self._ti_data.at[self._ti_data.index[-2], 
            self._indicator_name.split('-')[0] + '-' + str(long_term_MA)]) *\
           (self._input_data.iat[-1, 0] - self._ti_data.at[self._ti_data.index[-1], 
            self._indicator_name.split('-')[0] + '-' + str(long_term_MA)]) < 0:
            
            direction = self._input_data.iat[-1, 0] - self._ti_data.at[self._ti_data.index[-1], 
                self._indicator_name.split('-')[0] + '-' + str(long_term_MA)]
           
            if direction > 0:
                long_term_signal = TRADE_SIGNALS['Buy']
            elif direction < 0:
                long_term_signal = TRADE_SIGNALS['Sell']
                
        else:
            long_term_signal = TRADE_SIGNALS['Hold']
        
        # Signal from short term MA
        if len(self._periods) > 1:
            short_term_MA = min(self._periods)
            
            # MAs crosses each other
            if (self._ti_data.at[self._ti_data.index[-2], 
                self._indicator_name.split('-')[0] + '-'  + str(short_term_MA)] - \
                self._ti_data.at[self._ti_data.index[-2], 
                self._indicator_name.split('-')[0] + '-'  + str(long_term_MA)]) * \
               (self._ti_data.at[self._ti_data.index[-1], 
                self._indicator_name.split('-')[0] + '-'  + str(short_term_MA)] - \
                self._ti_data.at[self._ti_data.index[-1], 
                self._indicator_name.split('-')[0] + '-'  + str(long_term_MA)]) < 0:
                
                direction = self._ti_data.at[self._ti_data.index[-1], 
                    self._indicator_name.split('-')[0] + '-'  + str(short_term_MA)] - \
                    self._ti_data.at[self._ti_data.index[-1],
                    self._indicator_name.split('-')[0] + '-'  + str(long_term_MA)]
                            
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