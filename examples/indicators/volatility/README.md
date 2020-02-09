# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Volatility Technical Indicators examples
The Volatility Technical Indicators implemented are:
- Bollinger Bands (BB)
- Standard Deviation (SD)

#### BB Technical Indicator example
```
$python indicators_bb.py
- Graph ../figures/indicators_bb_long_example.png saved.
- Graph ../figures/indicators_bb_short_example.png saved.
- Graph ../figures/indicators_bb_medium_example.png saved.

BB data:
                    SMA  Upper Band  Lower Band
Date
2012-01-03  128.220000  140.456350  115.983650
2012-01-04  126.960000  139.196350  114.723650
2012-01-05  127.313333  139.549683  115.076984
2012-01-06  127.087500  139.323850  114.851150
2012-01-09  126.706000  138.942350  114.469650
...                ...         ...         ...
2012-09-06  141.814500  154.050850  129.578150
2012-09-07  142.063000  154.299350  129.826650
2012-09-10  142.108500  154.344850  129.872150
2012-09-11  142.197000  154.433350  129.960650
2012-09-12  142.289500  154.525850  130.053150

[176 rows x 3 columns]

BB value at 2012-09-06: [141.81449999999995, 154.0508497570404, 129.5781502429595]

BB value at 2012-09-12 00:00:00 : [142.28949999999995, 154.5258497570404, 130.0531502429595]

Signal: ('Hold', 0)
```

The script generates the below plots:

##### BB Long Term
![](../figures/indicators_bb_long_example.png?raw=true)

##### BB Short Term
![](../figures/indicators_bb_short_example.png?raw=true)

##### BB Medium Term
![](../figures/indicators_bb_medium_example.png?raw=true)

#### SD Technical Indicator example
```
$python indicators_sd.py
- Graph ../figures/indicators_sd_20_example.png saved.

SD data:
              SD
Date
2012-01-03  NaN
2012-01-04  NaN
2012-01-05  NaN
2012-01-06  NaN
2012-01-09  NaN
...         ...
2012-09-06  NaN
2012-09-07  NaN
2012-09-10  NaN
2012-09-11  NaN
2012-09-12  NaN

[176 rows x 1 columns]

SD value at 2012-09-06: [nan]

SD value at 2012-09-12 00:00:00 : [nan]

Signal: ('Hold', 0)
```

The script generates the below plot:

##### SD
![](../figures/indicators_sd_20_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `version 0.1` or later
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

