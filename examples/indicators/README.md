# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### _trend module examples
The `_trend` module defined under the `tradingti.indicators` package implements Technical Indicators of Trend type. Below are examples of using the implemented indicators.

#### SMA Technical Indicator example
```
$python indicators_sma.py

- Graph ./figures/indicators_sma_200_example.png saved.
- Graph ./figures/indicators_sma_50_200_example.png saved.

SMA data:
                 SMA-50     SMA-200
Date
2000-02-01   19.230000   19.230000
2000-02-02   19.230000   19.230000
2000-02-03   19.206667   19.206667
2000-02-04   19.220000   19.220000
2000-02-07   19.222000   19.222000
...                ...         ...
2012-09-06  143.657400  136.162450
2012-09-07  143.810200  136.293400
2012-09-10  143.875000  136.414700
2012-09-11  143.864400  136.546750
2012-09-12  143.805400  136.670500

[3169 rows x 2 columns]

SMA value at 2012-09-06: [143.65740000000034, 136.16245000000015]

SMA value at 2012-09-12 00:00:00 : [143.80540000000033, 136.67050000000015]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### SMA-200
![](./figures/indicators_sma_200_example.png?raw=true)

##### SMA-200 and SMA-50
![](./figures/indicators_sma_50_200_example.png?raw=true)


## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `commit 53c61ca41beb7a273462c7c518f9433846bbcd8d` or later
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

