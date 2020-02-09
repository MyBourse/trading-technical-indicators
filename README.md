# trading-technical-indicators
Trading Technical Indicators, Open Source Library, in Python.

The library calculates Trading Technical Indicators from input stock data. The data required for each technical indicator differ. For being able to use all the indicators included in the library, the following data are required: `High`, `Low`, `Close`, `Volume`, `Adj Close`.

The library exposes the below API:
- getTiPlot(): Returns a matplotlib.pyplot object for the calculated technical indicator.
- getTiData(): Returns a pandas DataFrame object with the calculated technical indicator.
- getTiValue(optional Date): Returns the value of the calculated technical indicator for a specific date.
- getSignal(): Returns the suggested trading action based on the calculated technical indicator.

An example is given below (For the `On Balance Volume (OBV)` technical indicator):

```
# Read data from csv file. Set the index to the correct column (dates column)
df = pd.read_csv('../data/sample_data.csv', parse_dates = True, index_col = 0)

# Calculate the OBV indicator
obv = OBV(df[df.index >= '2012-01-01'])

# Save the plot of the calculated Technical Indicator
obv.getTiPlot()

# Get OBV calculated data
obv.getTiData()

# Get OBV value for a specific date
obv.getTiValue('2012-09-06')

# Get the most recent OBV value
obv.getTiValue()

# Get signal from OBV
obv.getSignal()
```

The calculated data:

```
#### OBV Technical Indicator example
```               OBV
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

OBV value at 2012-09-06: [14487200.0]

OBV value at 2012-09-12 00:00:00 : [12894200.0]

Signal: ('Sell', 1)
```

The plot returned by the use of the getTiPlot() method is:
![](./examples/indicators/figures/indicators_obv_example.png?raw=true)

More examples can be found in the `examples` folder (see also Usage Examples section below).

The library is under development of the first release. The README file will be updated with the detailed information prior to the first release.

## Planned Releases
- version: `0.1`, planned release date: `2020-02-29`

### Release Notes (v 0.1)
In release 0.1 the below technical indicators will be included:
```
Trading Technical Indicators Python Library: version 0.1.dev

momentum technical indicators:
- Fast Stochastic Oscillator (FSO): v0.1
- Slow Stochastic Oscillator (SSO): v0.1
- Relative Strength Index (RSI): v0.1
- Ichimoku Cloud (IC): v0.1

support and resistance technical indicators:
- Fibonacci Retracement (FR): v0.1

trend technical indicators:
- Simple Moving Average (SMA): v0.1
- Exponential Moving Average (EMA): v0.1
- Moving Average Convergence Divergence (MACD): v0.1
- Average Directional Movement Index (ADX): v0.1
- Directional Movement Index (DMI): v0.1

volatility technical indicators:
- Bollinger Bands (BB): v0.1
- Standard Deviation (SD): v0.1

volume technical indicators:
- On Balance Volume (OBV): v0.1

13 technical indicators included in version 0.1.dev of the library.
```

### Status Overview
- Development of release v0.1: **Completed**
- First code review: **Completed**
- Test cases development: **In progress**
- Unit test execution: **Not started**
- Indicators signals evaluation: **Not started**
- Final code review: **Not started**
- Final test execution: **Not started**
- Finalize library's documentation: **Not started**
- Release of version 0.1 in PyPi: **Not started**


## Usage Examples
As the development progresses some usage examples are added to the repository:

- [Utils package usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/utils)
- [Moving Averages Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/moving_averages)
- [Stochastic Oscillators Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/stochastic_oscillators)
- [Volatility Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/volatility)
- [Momentum Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/momentum)
- [Support and Resistance Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/support_resistance)
- [Volume Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/volume)
- [Trend Indicators usage examples](https://github.com/vsaveris/trading-technical-indicators/tree/master/examples/indicators/trend)