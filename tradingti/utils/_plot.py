'''
File name: _plot.py
    Plotting methods defined under the tradingti.utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import matplotlib.pyplot as plt
from ._data_validation import validateDataframe

'''
Constants
'''
C_DEFAULT_COLORS_PALETTE = ['rosybrown', 'firebrick', 'olivedrab']


def lineGraph(data, title = 'Untitled Graph', x_label = 'Date', y_label = 'Price', 
    colors_palette = C_DEFAULT_COLORS_PALETTE, linewidth = None * data.shape[1], linestyle = None * data.shape[1], 
    alpha = None * data.shape[1]):
    '''
    Returns a lines graph of type matplotlib.pyplot.
    
    Args:
        data (pandas.core.frame.DataFrame): The data to include in the graph. 
            The index of the dataframe represents the data on the x-axis and 
            it should be of type pandas.core.indexes.datetimes.DatetimeIndex.
            Each column of the dataframe represents a line in the graph.
            
        title (string): The title on the top of the graph. Default value is 
            `Untitled Graph`.
            
        x_label (string): The label of the x-axis of the graph. Default value
            is `Date`.
            
        y_label (string): The label of the y-axis of the graph. Default value
            is `Price`.
            
        colors_palette (list of matplotlib.colors): The colors to be used for
            each line of the graph, in the defined order. In case where the lines 
            are more than the colors, then the list is scanned again from the zero
            index.
        
        linewidth (list of data.shape[1] members):
        
        linestyle (list of data.shape[1] members):
        
        alpha (list of data.shape[1] members):
        
    Raises:
        TypeError()

    Returns:
        matplotlib.pyplot: The prepared graph object.
    '''
    
    plt.clf()
    
    # Validate that the data argumnet is a pandas dataframe object and that the
    # index is a date type.
    validation_result = validateDataframe(data)
    if validation_result is not None:
        raise(TypeError(validation_result))
    
    # Set graph attributes
    plt.title(title, fontsize = 11, fontweight = 'bold')
    plt.xlabel(x_label, fontsize = 11, fontweight = 'bold') 
    plt.ylabel(y_label, fontsize = 11, fontweight = 'bold')
    plt.grid(which = 'major', axis = 'y', alpha = 0.5)
    
    # Add the lines
    i = 0 # Used for colors use in rotation
    for line_name in data.columns.values:
        plt.plot(data.index.values, data[line_name], label = line_name, 
            color = colors_palette[i % len(colors_palette)])
        i += 1
    
    plt.legend()
    
    return plt
