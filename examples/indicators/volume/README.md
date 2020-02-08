# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Volume Technical Indicators examples
The Volume Technical Indicators implemented are:
- On Balance Volume (OBV)

#### OBV Technical Indicator example
```
$python indicators_obv.py
- Graph ../figures/indicators_obv_example.png saved.

OBV data:
                     OBV
Date
2012-01-03            0
2012-01-04      -683000
2012-01-05       -82300
2012-01-06      -804200
2012-01-09  -1.3816e+06
...                 ...
2012-09-06  1.44872e+07
2012-09-07  1.48273e+07
2012-09-10  1.38265e+07
2012-09-11   1.3383e+07
2012-09-12  1.28942e+07

[176 rows x 1 columns]

OBV value at 2012-09-06: [14487200.0]

OBV value at 2012-09-12 00:00:00 : [12894200.0]

Signal: ('Sell', 1)
```

The script generates the below plots:

##### OBV
![](../figures/indicators_obv_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `version 0.1` or later
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

