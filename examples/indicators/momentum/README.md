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
$python indicators_ic.py
- Graph ../figures/indicators_ic_example.png saved.

IC data:
             Tenkan Sen  Kijun Sen  Senkou A  Senkou B
Date
2012-01-03     131.465    131.465       NaN       NaN
2012-01-04     130.600    130.600       NaN       NaN
2012-01-05     130.350    130.350       NaN       NaN
2012-01-06     130.350    130.350       NaN       NaN
2012-01-09     130.330    130.330       NaN       NaN
...                ...        ...       ...       ...
2012-09-06     142.500    143.410  144.8525   142.865
2012-09-07     142.620    142.140  144.5050   142.865
2012-09-10     142.620    142.140  144.4175   142.865
2012-09-11     142.620    141.540  144.4175   142.865
2012-09-12     142.530    141.400  145.6525   142.865

[176 rows x 4 columns]

IC value at 2012-09-06: [142.5, 143.41, 144.85250000000002, 142.865]

IC value at 2012-09-12 00:00:00 : [142.52999999999997, 141.39999999999998, 145.65249999999997, 142.865]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### IC
![](../figures/indicators_ic_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `latest commit in master branch`
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

