# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Momentum Technical Indicators examples
The Momentum Technical Indicators implemented are:
- Relative Strength Index (RSI)
- Ichimoku Cloud (IC)

#### RSI Technical Indicator example
```
$python indicators_rsi.py

- Graph ../figures/indicators_rsi_example.png saved.

RSI data:
                 RSI
Date
2011-01-03      NaN
2011-01-04      NaN
2011-01-05      NaN
2011-01-06      NaN
2011-01-07      NaN
...             ...
2012-09-06  65.8824
2012-09-07  65.4762
2012-09-10  48.8021
2012-09-11  47.4003
2012-09-12  36.0116

[428 rows x 1 columns]

RSI value at 2012-09-06: [65.88235294117652]

RSI value at 2012-09-12 00:00:00 : [36.011616650532375]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### RSI
![](../figures/indicators_rsi_example.png?raw=true)

#### IC Technical Indicator example
```
$
```

The script generates the below plots:

##### IC
![](../figures/indicators_ic_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `latest commit in master branch`
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

