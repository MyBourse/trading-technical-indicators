# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Moving Averages Technical Indicators examples
The Moving Averages Technical Indicators implemented are:
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Moving Average Convergence Divergence (MACD)

#### SMA Technical Indicator example
```
$python indicators_sma.py
- Graph ../figures/indicators_sma_200_example.png saved.
- Graph ../figures/indicators_sma_50_200_example.png saved.

SMA data:
               SMA-50    SMA-200
Date
2011-01-03  109.0300  109.03000
2011-01-04  108.0100  108.01000
2011-01-05  107.7700  107.77000
2011-01-06  107.3425  107.34250
2011-01-07  106.8560  106.85600
...              ...        ...
2012-09-06  143.6574  136.16245
2012-09-07  143.8102  136.29340
2012-09-10  143.8750  136.41470
2012-09-11  143.8644  136.54675
2012-09-12  143.8054  136.67050

[428 rows x 2 columns]

SMA value at 2012-09-06: [143.65739999999997, 136.1624499999999]

SMA value at 2012-09-12 00:00:00 : [143.80539999999996, 136.6704999999999]

Signal: ('Hold', 0)
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
2011-01-03  109.030000  109.030000
2011-01-04  107.970769  108.004900
2011-01-05  107.726175  107.764213
2011-01-06  107.260386  107.331748
2011-01-07  106.715321  106.837663
...                ...         ...
2012-09-06  142.691924  137.428880
2012-09-07  142.815485  137.498844
2012-09-10  142.699524  137.536704
2012-09-11  142.569929  137.571149
2012-09-12  142.409934  137.599792

[428 rows x 2 columns]

EMA value at 2012-09-06: [142.69192426632534, 137.42888002081443]

EMA value at 2012-09-12 00:00:00 : [142.40993445468706, 137.5997924138932]

Signal: ('Hold', 0)
```

The script generates the below plots:

##### EMA-200
![](../figures/indicators_ema_200_example.png?raw=true)

##### EMA-200 and EMA-50
![](../figures/indicators_ema_50_200_example.png?raw=true)

### MACD Technical Indicator example
```
$python indicators_macd.py
- Graph ../figures/indicators_macd_example.png saved.

MACD data:
                 MACD  Signal Line
Date
2012-01-03  0.000000     0.000000
2012-01-04 -0.056538    -0.031410
2012-01-05 -0.000098    -0.018577
2012-01-06 -0.032554    -0.023312
2012-01-09 -0.098449    -0.045664
...              ...          ...
2012-09-06 -0.063506    -0.214686
2012-09-07  0.079327    -0.155884
2012-09-10 -0.057761    -0.136259
2012-09-11 -0.188440    -0.146695
2012-09-12 -0.331753    -0.183707

[176 rows x 2 columns]

MACD value at 2012-09-06: [-0.06350599349639197, -0.21468627319003128]

MACD value at 2012-09-12 00:00:00 : [-0.33175294306838055, -0.1837067687406364]

Signal: ('Hold', 0)
```

The script generates the below plots:

##### MACD
![](../figures/indicators_macd_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `version 0.1` or later
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

