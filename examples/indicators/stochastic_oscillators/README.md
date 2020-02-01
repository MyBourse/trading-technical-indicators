# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Stochastic Oscillators Technical Indicators examples
The Stochastic Oscillators Technical Indicators implemented are:
- Fast Stochastic Oscillator (FSO)
- Slow Stochastic Oscillator (SSO)

#### FSO Technical Indicator example
```
$python indicators_fso.py

- Graph ../figures/indicators_fso_example.png saved.

FSO data:
                %K     %D
Date
2012-01-03   0.00   0.00
2012-01-04   0.00   0.00
2012-01-05   0.00   0.00
2012-01-06   0.00   0.00
2012-01-09   0.00   0.00
...           ...    ...
2012-09-06  72.30  68.14
2012-09-07  87.83  75.01
2012-09-10  20.22  60.12
2012-09-11  13.70  40.58
2012-09-12   5.65  13.19

[176 rows x 2 columns]

FSO value at 2012-09-06: [72.3, 68.14]

FSO value at 2012-09-12 00:00:00 : [5.65, 13.19]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### FSO Graph
![](../figures/indicators_fso_example.png?raw=true)


### SSO Technical Indicator example
```
$python indicators_sso.py

- Graph ../figures/indicators_sso_example.png saved.

SSO data:
                %K     %D
Date
2012-01-03   0.00   0.00
2012-01-04   0.00   0.00
2012-01-05   0.00   0.00
2012-01-06   0.00   0.00
2012-01-09   0.00   0.00
...           ...    ...
2012-09-06  67.72  62.82
2012-09-07  74.06  67.80
2012-09-10  59.97  67.25
2012-09-11  40.58  58.20
2012-09-12  13.09  37.88

[176 rows x 2 columns]

SSO value at 2012-09-06: [67.72, 62.82]

SSO value at 2012-09-12 00:00:00 : [13.09, 37.88]

Signal: Hold [ 0 ]
```

The script generates the below plots:

##### SSO Graph
![](../figures/indicators_sso_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `latest commit in master branch`
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

