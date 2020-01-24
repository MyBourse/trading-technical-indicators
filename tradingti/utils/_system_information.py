'''
File name: _system_information.py
    Prints system information. Adapted from `sklearn.utils._show_versions`
           
Author: Vasileios Saveris
enail: vsaveris@gmail.com

License: MIT

Date last modified: 22.01.2020

Python Version: 3.6
'''

import platform
import sys
import importlib


def showVersions():
    '''
    Prints system information.
    
    Args:
        -

    Raises:
        -

    Returns:
        -
    '''
    
    # Print System Information
    print('\nSystem Information:')
    print('-    python version:', sys.version),
    print('- python executable:', sys.executable),
    print('-          platform:', platform.platform())
    
    # Print Package Dependencies
    dependenciess = ['pandas', 'matplotlib']
    print('\nDependencies:')
    
    for d in dependenciess:

        try:
            if d in sys.modules:
                module = sys.modules[d]
            else:
                module = importlib.import_module(d)
            version = module.__version__
        except ImportError:
            version = 'Not installed'
            
        print('- {:10}: {}'.format(d, version))

