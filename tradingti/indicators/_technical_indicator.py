'''
File name: _technical_indicator.py
    Parent class for all the technical indicators.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

from abc import ABC, abstractmethod
import pandas as pd
from ..utils import linesGraph


class TI(ABC):
    '''
    Technical Indicators class implementation. Is used as a parent class for
    each implemented technical indicator. It implements the public API for
    accessing the calculated values of each technical indicator.

    Args:
        input_data (pandas dataframe): The input to the Technical Indicator.
            Index is of type date. It contains one column with the Adjusted
            Closed price of a given stock.
            
        ti_data (pandas dataframe): The calculated values of the Technical
            indicator. Index is of type date. It contains a number of columns
            depending the Technical Indicator.
                
        indicator_name (string): The name of the Technical Indicator.
                
        lines_color (list of matplotlib colors): The colors to be used
            when generating the plot for a Technical Indicator. Default value is
            None (default colors will be used).
            
        subplots (boolean): Indicates if the technical indicator graph should
            contain subplots.
            
        areas (list of dictionaries): Includes the areas to be plotted by using
            the fill_between matplotlib method. Each member of the list should
            be a dictionary with the below keys:
            {'x':, 'y1':, 'y2':, 'color':}, see fill_between matplotlib method
            for more details.

    Attributes:
        _input_data (pandas dataframe): The input to the Technical Indicator.
            
        _ti_data (pandas dataframe): The calculated values of the Technical
            indicator.
                
        _indicator_name (string): The name of the Technical Indicator.
                
        _lines_color (list of matplotlib colors): The colors to be used
            when generating the plot for a Technical Indicator.
            
        _subplots (boolean): Indicates if the technical indicator graph should
            contain subplots.
            
        _areas (list of dictionaries): Includes the areas to be plotted by using
            the fill_between matplotlib method. Each member of the list should
            be a dictionary with the below keys:
            {'x':, 'y1':, 'y2':, 'color':}, see fill_between matplotlib method
            for more details.
                                
    Methods:
        getTiPlot(): Generates a plot including the input data and the technical 
            indicator calculated values.
            
        getTiData(): Returns the Technical Indicator values for the whole period
  
        getSignal(): Abstract method for Technical Indicator signal calculation.

        getTiValue(): Returns the Technical Indicator value for a given date.
    
    '''
    def __init__(self, input_data, ti_data, indicator_name,
        lines_color = None, subplots = False, areas = None):

        self._input_data = input_data
        self._ti_data = ti_data
        self._indicator_name = indicator_name
        self._lines_color = lines_color
        self._subplots = subplots
        self._areas = areas
        
        
    def getTiPlot(self):
        '''
        Generates a plot including the input data and the technical indicator
        calculated values.
    
        Args:
            -

        Raises:
            -

        Returns:
            matplotlib object: The generated plot.
        '''
        
        # If data are Series, then convert them to DataFrame
        if isinstance(self._input_data, pd.core.series.Series):
            self._input_data = self._input_data.to_frame()
            
        if isinstance(self._ti_data, pd.core.series.Series):
            self._ti_data = self._ti_data.to_frame()
            
        if self._subplots:
            data = [self._input_data, self._ti_data]
        else:
            data = pd.concat([self._input_data, self._ti_data], axis = 1)
        
        return linesGraph(data = data, title = self._indicator_name, 
            lines_color = self._lines_color, areas = self._areas)


    def getTiData(self):
        '''
        Returns the Technical Indicator values for the whole period.
        
        Args:
            -

        Raises:
            -

        Returns:
            pandas dataframe object: The Technical Indicator values.
        '''
        
        return self._ti_data
        
    
    @abstractmethod    
    def getSignal(self):
        '''
        Abstract method for Technical Indicator signal calculation. The
        implemented method should return an integer representing the Trading 
        signal. Possible values are {'Hold': 0, 'Buy': -1, 'Sell': 1}
    
        Args:
            -

        Raises:
            -

        Returns:
            -
        '''
        
        pass
        
        
    def getTiValue(self, date = None):
        '''
        Returns the Technical Indicator value for a given date. If the date
        is None, it returns the most recent entry.
    
        Args:
            data (string, default is None): A date string. 

        Raises:
            -

        Returns:
            list of numbers: The value of the Technical Indicator for the given
                date.
        '''

        if date is None:
            return list(self._ti_data.iloc[-1, :])
        else:
            return list(self._ti_data.loc[pd.to_datetime(date), :])

        