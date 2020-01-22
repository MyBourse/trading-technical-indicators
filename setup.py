import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'trading-technical-indicators',
    version = '1.0',
    author= 'Vasileios Saveris',
    author_email = 'vsaveris@gmail.com',
    description = 'Trading Technical Indicators, Open Source Library, in Python',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/vsaveris/trading-technical-indicators',
    packages = setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.6',
)