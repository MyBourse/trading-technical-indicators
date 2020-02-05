# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Support and Resistance Technical Indicators examples
The Support and Resistance Technical Indicators implemented are:
- Fibonacci Retracement (FR)

#### FR Technical Indicator example
```
$python indicators_fr.py
- Graph ../figures/indicators_fr_example.png saved.

FR data:
               RL0        RL1        RL2        RL3     RL4
Date
2012-01-03  151.0  144.27872  140.12064  133.39936  122.52
2012-01-04  151.0  144.27872  140.12064  133.39936  122.52
2012-01-05  151.0  144.27872  140.12064  133.39936  122.52
2012-01-06  151.0  144.27872  140.12064  133.39936  122.52
2012-01-09  151.0  144.27872  140.12064  133.39936  122.52
...           ...        ...        ...        ...     ...
2012-09-06  151.0  144.27872  140.12064  133.39936  122.52
2012-09-07  151.0  144.27872  140.12064  133.39936  122.52
2012-09-10  151.0  144.27872  140.12064  133.39936  122.52
2012-09-11  151.0  144.27872  140.12064  133.39936  122.52
2012-09-12  151.0  144.27872  140.12064  133.39936  122.52

[176 rows x 5 columns]

FR value at 2012-09-06: [151.0, 144.27872, 140.12064, 133.39936, 122.52]

FR value at 2012-09-12 00:00:00 : [151.0, 144.27872, 140.12064, 133.39936, 122.52]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### FR
![](../figures/indicators_fr_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `latest commit in master branch`
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

