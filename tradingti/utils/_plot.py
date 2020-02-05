'''
File name: _plot.py
    Plotting methods defined under the tradingti.utils package.
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 01.02.2020

Python Version: 3.6
'''

import matplotlib.pyplot as plt
from ._data_validation import validateDataframe


def linesGraph(data, title = 'Untitled Graph', x_label = 'Date', 
    y_label = 'Price', lines_color = [None], lines_width = [None], 
    lines_style = [None], alpha_values = [None], areas = None): 
    '''
    Returns a lines graph of type matplotlib.pyplot. The graph can be either
    a figure with a single plot, or a figure containing two vertical subplots.
    
    Args:
        data (pandas.core.frame.DataFrame or a list of maximum two pandas.core.
            frame.DataFrame objects): The data to include in the graph. If data
            is a single dataframe or a list of one dataframe, then a single plot 
            is prepared. If data is a list of two dataframes, then a plot with
            two subplots vertically stacked is prepared. Each dataframe in the 
            list is used for a separate subplot. In all other cases a TypeError
            exception is raised.  
            The index of the dataframe represents the data on the x-axis and it 
            should be of type pandas.core.indexes.datetimes.DatetimeIndex. Each 
            column of the dataframe represents a line in the graph.
            
        title (string): The title on the top of the graph. Default value is 
            `Untitled Graph`.
            
        x_label (string): The label of the x-axis of the graph. Default value
            is `Date`.
            
        y_label (string): The label of the y-axis of the graph. Default value
            is `Price`.
            
        lines_color (list of matplotlib.colors): The colors to be used for
            each line of the graph, in the defined order. In case where the 
            lines are more than the colors, then the list is scanned again from 
            the zero index.
        
        lines_width (list of floats): Width of each line, to be used in the call
            of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned 
            again from the zero index.
        
        lines_style (list of strings): Style of each line, to be used in the 
            call of the matplotlib.pyplot.plot method. In case where the lines 
            are more than the members of the list, then the list is scanned 
            again from the zero index. See: 
            http://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html 
            for possible values.
        
        alpha_values (list of floats): Alpha value of each line, to be used in 
            the call of the matplotlib.pyplot.plot method. In case where the 
            lines are more than the members of the list, then the list is 
            scanned again from the zero index.
            
        areas (list of dictionaries): Includes the areas to be plotted by using
            the fill_between matplotlib method. Each member of the list should
            be a dictionary with the below keys:
            {'x':, 'y1':, 'y2':, 'color':}, see fill_between matplotlib method
            for more details.
        
    Raises:
        TypeError()

    Returns:
        matplotlib.pyplot: The prepared graph object.
    '''

    #plt.clf()

    # For handling a list input always
    if type(data) != list:
        data = [data]
    
    # Validate that the list contains at most two members
    if len(data) > 2:
        raise(TypeError('Validation of the \'data\' argument of the '      +\
            '\'linesGraph\' method failed. It should be a list of maximum '+\
            'two members, but it contains ' + str(len(data)) + ' members.'))
    
    # Validate that each member of the `data` list is a dataframe and that its
    # index is of date type.
    for df in data:
        validation_result = validateDataframe(df)
        if validation_result is not None:
            raise(TypeError('Validation of the \'data\' argument of the '+\
                '\'linesGraph\' method failed. ' + validation_result))

    plt.figure(figsize = (7, 5))
    
    # Add the subplots
    j = 0 # Used for plot attributes use in rotation
    
    for i in range(len(data)):
        plt.subplot(len(data), 1, i+1)
        
        for line_name in data[i].columns.values:
            plt.plot(data[i].index, data[i][line_name], label = line_name, 
                color = lines_color[j % len(lines_color)], 
                linewidth = lines_width[j % len(lines_width)], 
                linestyle = lines_style[j % len(lines_style)], 
                alpha = alpha_values[j % len(alpha_values)])
            
            j += 1
            
        plt.legend(loc = 0)
        plt.grid(which = 'major', axis = 'y', alpha = 0.5)

        # Set attributes for each subplot depending its position      
        if i == 0:
            plt.title(title, fontsize = 11, fontweight = 'bold')
            if len(data) > 1:
                plt.gca().axes.get_xaxis().set_visible(False)
    
    # Last subplot x-axis
    plt.xlabel(x_label, fontsize = 11, fontweight = 'bold')
    plt.gcf().autofmt_xdate()    
    
    # Common y-axis label
    plt.gcf().text(0.04, 0.5, y_label, fontsize = 11, fontweight = 'bold', 
        va = 'center', rotation = 'vertical')         
    
    # Plot areas
    if areas is not None:
        for a in areas:
            plt.gca().fill_between(x = a['x'], y1 = a['y1'], y2 = a['y2'], 
                color = a['color'])

    return plt
