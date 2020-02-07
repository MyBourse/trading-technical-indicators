# Utils package usage examples (tradingti.utils)
## Description
The `tradingti.utils` package contains utilities methods. The input data used for the below examples can be found under the `data` directory.

### _system_information and _library_information modules example
The `_system_information` and `_library_information` modules defined under the `tradingti.utils` package implement system and library information methods. Below is an example of using the modules' methods.
```
$python utils_info.py

System Information:
- python version: 3.7.6 | packaged by conda-forge | (default, Jan  7 2020, 21:48:41) [MSC v.1916 64 bit (AMD64)]
- python executable: C:\Users\vsaveris\Anaconda3\envs\trading-technical-indicators\python.exe
- platform: Windows-10-10.0.18362-SP0

Dependencies:
- pandas    : 0.25.3
- matplotlib: 3.1.2

Trading Technical Indicators Python Library: version 0.1.dev

momentum technical indicators:
- Fast Stochastic Oscillator (FSO): v0.1
- Slow Stochastic Oscillator (SSO): v0.1
- Relative Strength Index (RSI): v0.1
- Ichimoku Cloud (IC): v0.1

support and resistance technical indicators:
- Fibonacci Retracement (FR): v0.1

trend technical indicators:
- Simple Moving Average (SMA): v0.1
- Exponential Moving Average (EMA): v0.1
- Moving Average Convergence Divergence (MACD): v0.1
- Average Directional Movement Index (ADX): v0.1
- Directional Movement Index (DMI): v0.1

volatility technical indicators:
- Bollinger Bands (BB): v0.1
- Standard Deviation (SD): v0.1

volume technical indicators:
- On Balance Volume (OBV): v0.1

13 technical indicators included in version 0.1.dev of the library.
```

### _plot module examples
The `_plot` module defined under the `tradingti.utils` package implements methods for plotting stock and technical indicators data. Below is an example of using the module's methods.
```
$python utils_plot.py

- Graph ./figures/utils_plot_example.png saved.
```

The script generates a plot of an input stock price data.
![](./figures/utils_plot_example.png?raw=true)


### _data_preprocessing module examples
The `_data_preprocessing` module defined under the `tradingti.utils` package implements methods for preprocessing the input stock data. Below is an example of using the module's methods.
```
$python utils_data_preprocessing.py

- Graph ./figures/example_data_missing_1.png saved.
- Graph ./figures/example_data_missing_2.png saved.
- Graph ./figures/example_data_missing_3.png saved.
```

The script fills the missing values for three different input data:

#### Missing data at the begining of the period 
![](./figures/example_data_missing_1.png?raw=true)

#### Missing data at the end of the period 
![](./figures/example_data_missing_2.png?raw=true)

#### Missing data in multiple places in the period 
![](./figures/example_data_missing_3.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `latest commit in master branch`
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

