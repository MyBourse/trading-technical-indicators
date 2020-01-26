# Utils package usage examples (tradingti.utils)
## Description
The `tradingti.utils` package contains utilities methods. The input data used for the below examples can be found under the `data` directory.

### _plot module examples
The `_plot` module defined under the `tradingti.utils` package implements methods for plotting stock and technical indicators data. Below is an example of using the module's methods.
```
$python utils_plot.py
```

The script generates a plot of an input stock price data.
![](./figures/utils_plot_example.png?raw=true)


### _data_preprocessing module examples
The `_data_preprocessing` module defined under the `tradingti.utils` package implements methods for preprocessing the input stock data. Below is an example of using the module's methods.
```
$python utils_data_preprocessing.py
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
2. tradingti library: `commit c6cf9a2010ea01ecaf1056f8596d0093e965d639` or later
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

