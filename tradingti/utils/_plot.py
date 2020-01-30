'''
File name: _plot.py
    Plotting methods defined under the tradingti.utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 29.01.2020

Python Version: 3.6
'''

import matplotlib.pyplot as plt
from ._data_validation import validateDataframe


def lineGraph(data, title = 'Untitled Graph', x_label = 'Date', y_label = 'Price', 
    lines_color = [None], lines_width = [None], lines_style = [None],
    alpha_values = [None]):
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
            
        lines_color (list of matplotlib.colors): The colors to be used for
            each line of the graph, in the defined order. In case where the lines 
            are more than the colors, then the list is scanned again from the zero
            index.
        
        lines_width (list of floats): Width of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned again 
            from the zero index.
        
        lines_style (list of strings): Style of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned again 
            from the zero index. See: 
            https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html 
            for possible values.
        
        alpha_values (list of floats): Alpha value of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned again 
            from the zero index.
        
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
        raise(TypeError('Validation of the \'data\' argument of the '+\
                '\'lineGraph\' method failed. ' + validation_result))
    
    # Set graph attributes
    plt.title(title, fontsize = 11, fontweight = 'bold')
    plt.xlabel(x_label, fontsize = 11, fontweight = 'bold') 
    plt.ylabel(y_label, fontsize = 11, fontweight = 'bold')
    plt.grid(which = 'major', axis = 'y', alpha = 0.5)

    # To avoid overlapping in x-axis
    plt.gcf().autofmt_xdate()
    
    # Add the lines
    i = 0 # Used for plot attributes use in rotation
    for line_name in data.columns.values:
        plt.plot(data.index.values, data[line_name], label = line_name, 
            color = lines_color[i % len(lines_color)], linewidth = lines_width[i % len(lines_width)], 
            linestyle = lines_style[i % len(lines_style)], alpha = alpha_values[i % len(alpha_values)])
            
        i += 1
    
    plt.legend()
    
    return plt

    
def verticalLineSubplots(data_list, title = 'Untitled Graph', x_label = 'Date', y_label = 'Price', 
    lines_color = [None], lines_width = [None], lines_style = [None],
    alpha_values = [None]):
    '''
    Returns a lines graph of type matplotlib.pyplot.
    
    Args:
        data_list (list of pandas.core.frame.DataFrame objects): The data to
            include in the graph. Each dataframe in the list is used for a 
            separate subplot. The index of the dataframe represents the 
            data on the x-axis and it should be of type pandas.core.indexes.
            datetimes.DatetimeIndex. Each column of the dataframe represents
            a line in the graph.
            
        title (string): The title on the top of the graph. Default value is 
            `Untitled Graph`.
            
        x_label (string): The label of the x-axis of the graph. Default value
            is `Date`.
            
        y_label (string): The label of the y-axis of the graph. Default value
            is `Price`.
            
        lines_color (list of matplotlib.colors): The colors to be used for
            each line of the graph, in the defined order. In case where the lines 
            are more than the colors, then the list is scanned again from the zero
            index.
        
        lines_width (list of floats): Width of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned again 
            from the zero index.
        
        lines_style (list of strings): Style of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned again 
            from the zero index. See: 
            https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html 
            for possible values.
        
        alpha_values (list of floats): Alpha value of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned again 
            from the zero index.
        
    Raises:
        TypeError()

    Returns:
        matplotlib.pyplot: The prepared graph object.
    '''

    plt.clf()
    
    # Validate that the data_list argumnet is a list of pandas dataframe objects and that the
    # index is a date type.
    if type(data_list) != list:
        message = 'The \'data_list\' argument of the \'verticalLineSubplots\' method should '+\
            'be a list (of pandas.core.frame.DataFrame objects), but it is of type '    +\
            str(type(data_list)) + '.'
        raise(TypeError(message))
    
    for df in data_list:
        validation_result = validateDataframe(df)
        if validation_result is not None:
            raise(TypeError('Contents validation of the \'data_list\' argument of the '+\
                '\'verticalLineSubplots\' method failed. ' + validation_result))

    plt.figure(figsize = (7, 5))
    
    # Add the subplots
    j = 0 # Used for plot attributes use in rotation
    
    for i in range(len(data_list)):
        plt.subplot(len(data_list), 1, i+1)
        
        for line_name in data_list[i].columns.values:
            plt.plot(data_list[i].index, data_list[i][line_name], label = line_name,
                color = lines_color[j % len(lines_color)], linewidth = lines_width[j % len(lines_width)], 
                linestyle = lines_style[j % len(lines_style)], alpha = alpha_values[j % len(alpha_values)])
            j += 1
            
        plt.legend(loc = 0)
        plt.grid(which = 'major', axis = 'y', alpha = 0.5)

        # Set attributes for each subplot depending its position      
        if i == 0:
            plt.title(title, fontsize = 11, fontweight = 'bold')
            plt.gca().axes.get_xaxis().set_visible(False)
        elif i == len(data_list)-1 :
            pass
        else:
            plt.gca().axes.get_xaxis().set_visible(False)
    
    # Last subplot x-axis
    plt.xlabel(x_label, fontsize = 11, fontweight = 'bold')
    plt.gcf().autofmt_xdate()    
    
    # Common y-axis label
    plt.gcf().text(0.04, 0.5, y_label, fontsize = 11, fontweight = 'bold', va = 'center', rotation = 'vertical')         
    
    return plt
