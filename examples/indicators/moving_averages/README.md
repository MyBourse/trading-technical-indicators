# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Moving Averages Technical Indicators examples
The Moving Averages Technical Indicators implemented are:
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)

#### SMA Technical Indicator example
```
$python indicators_sma.py

- Graph ../figures/indicators_sma_200_example.png saved.
- Graph ../figures/indicators_sma_50_200_example.png saved.

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
![](../figures/indicators_sma_200_example.png?raw=true)

##### SMA-200 and SMA-50
![](../figures/indicators_sma_50_200_example.png?raw=true)

### EMA Technical Indicator example
```
$python indicators_ema.py

- Graph ../figures/indicators_ema_200_example.png saved.
- Graph ../figures/indicators_ema_50_200_example.png saved.

EMA data:
                 EMA-26     EMA-200
Date
2000-02-01   19.230000   19.230000
2000-02-02   19.230000   19.230000
2000-02-03   19.204850   19.206433
2000-02-04   19.220267   19.220026
2000-02-07   19.222524   19.222061
...                ...         ...
2012-09-06  142.691924  136.832406
2012-09-07  142.815485  136.907308
2012-09-10  142.699524  136.950519
2012-09-11  142.569929  136.990314
2012-09-12  142.409934  137.024341

[3169 rows x 2 columns]

EMA value at 2012-09-06: [142.6919242663251, 136.83240626411458]

EMA value at 2012-09-12 00:00:00 : [142.40993445468686, 137.02434112063497]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### EMA-200
![](../figures/indicators_ema_200_example.png?raw=true)

##### EMA-200 and EMA-50
![](../figures/indicators_ema_50_200_example.png?raw=true)


## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `latest commit in master branch`
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

