# Indicators package usage examples (tradingti.indicators)
## Description
The `tradingti.indicators` package contains the implemented Trading Technical Indicators. The input data used for the below examples can be found under the `data` directory.

### Trend Technical Indicators examples
The Trend Technical Indicators implemented are:
- Average Directional Movement Index (ADX)
- Directional Movement Index (DMI)

#### ADX Technical Indicator example
```
$python indicators_adx.py
- Graph ../figures/indicators_adx_example.png saved.

ADX data:
                   ADX
Date
2012-01-03        NaN
2012-01-04        NaN
2012-01-05        NaN
2012-01-06        NaN
2012-01-09        NaN
...               ...
2012-09-06  30.114986
2012-09-07  32.938476
2012-09-10  29.913201
2012-09-11  27.627468
2012-09-12  32.771843

[176 rows x 1 columns]

ADX value at 2012-09-06: [30.1149862442006]

ADX value at 2012-09-12 00:00:00 : [32.771842584627706]

Signal: ('Sell', 1)
```

The script generates the below plots:

##### ADX
![](../figures/indicators_adx_example.png?raw=true)

#### DMI Technical Indicator example
```
$python indicators_dmi.py
- Graph ../figures/indicators_dmi_example.png saved.

DMI data:
                DMI+     DMI-       DX
Date
2012-01-03      NaN      NaN      NaN
2012-01-04      NaN      NaN      NaN
2012-01-05      NaN      NaN      NaN
2012-01-06      NaN      NaN      NaN
2012-01-09      NaN      NaN      NaN
...             ...      ...      ...
2012-09-06  20.0311  15.7958  11.8214
2012-09-07  29.1952  12.9465  38.5575
2012-09-10   19.572  35.8672   29.393
2012-09-11  15.4392  35.4357  39.3053
2012-09-12  13.4546  35.2782  44.7821

[176 rows x 3 columns]

DMI value at 2012-09-06: [20.03108164270775, 15.79584999923614, 11.821363006463192]

DMI value at 2012-09-12 00:00:00 : [13.454620921936474, 35.278207204881014, 44.78210504457693]

Signal: ('Hold', 0)
```

The script generates the below plots:

##### DMI
![](../figures/indicators_dmi_example.png?raw=true)

## Prerequisites
1. python: `version 3.6` or later
2. tradingti library: `version 0.1` or later
3. matplotlib: `version 3.1.2` or later
4. pandas: `version 0.25.3` or later

