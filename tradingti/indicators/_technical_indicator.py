'''
File name: _technical_indicator.py
    Parent class for all the technical indicators.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 08.02.2020

Python Version: 3.6
'''

from abc import ABC, abstractmethod
import pandas as pd
from ..utils import linesGraph
from ..utils._data_validation import validateDataFrame


class TI(ABC):
    '''
    Technical Indicators class implementation. Is used as a parent class for
    each implemented technical indicator. It implements the public API for
    accessing the calculated values of each technical indicator.

    Args:
        input_data (pandas dataframe): The input to the Technical Indicator.
            Index is of type date. It contains a variable number of columns of 
            stock related data such `High`, `Low`, `Volume`, `Close`, 
            `Adj Close`, depending the Technical Indicator.
            
        ti_data (pandas dataframe): The calculated values of the Technical
            indicator. Index is of type date. It contains a number of columns
            depending the Technical Indicator.
    
        indicator_name (string): The name of the Technical Indicator.
                
        plotted_input_columns (list of strings): The columns from the input data
            to be plotted (getTiPlot). The rest of the columns will be ignored.
            
        y_label (string): The label of the y-axis of the graph. Default value
            is `Price`.
        
        lines_color (list of matplotlib colors): The colors to be used
            when generating the plot for a Technical Indicator. Default value is
            None (matplotlib default colors will be used). In case where the 
            lines are more than the members of the list, then the list is 
            scanned again from the zero index.
            
        alpha_values (list of floats): Alpha value of each line, to be used in 
            the call of the matplotlib.pyplot.plot method. In case where the 
            lines are more than the members of the list, then the list is 
            scanned again from the zero index.
            
        areas (list of dictionaries): Includes the areas to be plotted by using
            the fill_between matplotlib method. Each member of the list should
            be a dictionary with the below keys:
            {'x':, 'y1':, 'y2':, 'color':}, see fill_between matplotlib method
            for more details.
            
        subplots (boolean): Indicates if the technical indicator graph should
            contain subplots.

    Attributes:
        _input_data (pandas dataframe): The input to the Technical Indicator.

        _ti_data (pandas dataframe): The calculated values of the Technical
            indicator.
    
        _indicator_name (string): The name of the Technical Indicator.
                
        _plotted_input_columns (list of strings): The columns from the input 
            data to be plotted (getTiPlot).
            
        _y_label (string): The label of the y-axis of the graph (getTiPlot).
        
        _lines_color (list of matplotlib colors): The colors to be used
            when generating the plot for a Technical Indicator.
            
        _alpha_values (list of floats): Alpha value of each line, to be used in 
            the call of the matplotlib.pyplot.plot method.
            
        _areas (list of dictionaries): Includes the areas to be plotted by using
            the fill_between matplotlib method.
        
        _subplots (boolean): Indicates if the technical indicator graph should
            contain subplots.
                                
    Methods:
        getTiPlot(): Generates a plot including the input data and the technical 
            indicator calculated values.
            
        getTiData(): Returns the Technical Indicator values for the whole 
            period.
  
        getSignal(): Abstract method for Technical Indicator signal calculation.

        getTiValue(): Returns the Technical Indicator value for a given date.
        
    Raises:
        TypeError (Exception raised from the validateDataFrame called method)
    
    '''
    def __init__(self, input_data, ti_data, indicator_name, 
        plotted_input_columns, y_label = None, lines_color = None, 
        alpha_values = [None], areas = None, subplots = False):

        # Validate the type of the input data and then store them
        validateDataFrame(input_data)
        self._input_data = input_data
        
        # Validate the type of the calculate indicator data and then store them
        validateDataFrame(ti_data)
        self._ti_data = ti_data
        
        self._indicator_name = indicator_name
        self._plotted_input_columns = plotted_input_columns
        self._y_label = y_label if y_label is not None else 'Price'
        self._lines_color = lines_color
        self._alpha_values = alpha_values
        self._areas = areas
        self._subplots = subplots
    
        
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
            
        if self._subplots:
            data = [self._input_data[self._plotted_input_columns], 
                self._ti_data]
        else:
            data = pd.concat([self._input_data[self._plotted_input_columns], 
                self._ti_data], axis = 1)
        
        return linesGraph(data = data, title = self._indicator_name, 
            y_label = self._y_label, lines_color = self._lines_color, 
            alpha_values = self._alpha_values, areas = self._areas)


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

        