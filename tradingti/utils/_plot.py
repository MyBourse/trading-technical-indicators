'''
File name: _plot.py
    Plotting methods defined under the utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import matplotlib.pyplot as plt
import pandas.core as pc

'''
Constants
'''
C_DEFAULT_COLORS_PALETTE = ['rosybrown', 'firebrick', 'olivedrab', 'seagreen', 'royalblue',
    'mediumpurple', 'darkorange']


def lineGraph(data, title = '', x_label = '', y_label = '', colors_palette = C_DEFAULT_COLORS_PALETTE):
    '''
    Returns a lines graph of type matplotlib.pyplot.
    
    Args:
        data (pandas.core.frame.DataFrame): The data to include in the graph. 
            The index of the dataframe represents the data on the x-axis and 
            it should be of type pandas.core.indexes.datetimes.DatetimeIndex.
            Each column of the dataframe represents a line in the graph.
            
        title (string): The title on the top of the graph. Default value is 
            an empty string.
            
        x_label (string): The label of the x-axis of the graph. Default value
            is an empty string.
            
        y_label (string): The label of the y-axis of the graph. Default value
            is an empty string.
            
        colors_palette (list of matplotlib.colors): The colors to be used for
            each line of the graph, in the defined order. In case where the lines 
            are more than the colors, then the list is scanned again from the zero
            index.

    Raises:
        TypeError()

    Returns:
        matplotlib.pyplot: The prepared graph object.
    '''

    # Validate that the data argumnet is a pandas dataframe object
    if not isinstance(data, pc.frame.DataFrame):
        message = 'The \'data\' argument of the \'lineGraph\' method should ' +\
            'be of type pandas.core.frame.DataFrame but it is of type '       +\
            str(type(data)) + '.'
        raise(TypeError(message))
    
    # Validate that the index of the pandas dataframe is a date
    if not isinstance(data.index, pc.indexes.datetimes.DatetimeIndex):
        message = 'The index of the \'data\' dataframe argument of the '     +\
            '\'lineGraph\' method should be of type '                        +\
            'pandas.core.indexes.datetimes.DatetimeIndex but it is of type ' +\
            str(type(data.index)) + '.'
        raise(TypeError(message))
    
    # Set graph attributes
    plt.title(title, fontsize = 11, fontweight = 'bold')
    plt.xlabel(x_label, fontsize = 11, fontweight = 'bold') 
    plt.ylabel(y_label, fontsize = 11, fontweight = 'bold')
    
    # Add the lines
    i = 0 # Used for colors use in rotation
    for line_name in data.columns.values:
        plt.plot(data.index.values, data[line_name], label = line_name, 
            color = colors_palette[i % len(colors_palette)])
        i += 1
    
    plt.legend()
    
    return plt
