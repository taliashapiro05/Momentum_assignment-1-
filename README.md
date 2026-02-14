# Momentum_assignment-1-
# Momentum trading Assignment 

# Project Overview 
 the following project implements and backtests three momentum based trading strategies, Rate of Change (ROC), Moving Average Crossover (MAC), and Moving Average Convergence Divergence (MACD) on historical stock price data. The goal is to evaluate their performance in terms of total return and analyse how recent price data can indicate future price changes. As such this exploits the tendency for assets with recent positive performance to continue outperforming, and vice versa.

# Strategies Implemented
 **Rate of Change (ROC)**
- Measures percentage price change over a fixed lookback period (default: 10 days)
- Simple and reactive to recent price movements
- Trading rule: Buy when price has risen more than threshold (default: 3%) over lookback window

 **Moving Average (MA) Crossover**
- Compares fast-term (default: 20-day) and slow-term (default: 50-day) simple moving averages
- Smoother signals with less noise than ROC
- Trading rule: Buy when fast MA crosses above slow MA

 **MACD (Moving Average Convergence Divergence)**
- Compares exponential moving averages (12-day, 26-day) and signal line (9-day)
- Balances responsiveness with trend confirmation
- Trading rule: Buy when MACD line crosses above signal line

# Composite momentum score:*
- Weighted combination of standardized sub-scores from all three indicators
- Unified comparison and performance analysis
- Chosen weightings place higher weight on ROC

# How to Run
Libraries: pandas, numpy, matplotlib, yfinance
Execution: Run script or notebook top to bottom
Key Parameters:
  - Ticker: stock symbol
  - start_date / end_date: period in YYYY-MM-DD format
  - ROC: roc_n (lookback), roc_threshold (buy threshold)
  - MA: fast_n, slow_n
  - MACD: short_window, long_window, signal_window

# Backtesting Framework 
- Assumptions: execute the trade at the next day close, no transaction costs, long positions only

# Key Functions 
- get_price_data(): Downloads and cleans historical price data
- ROC_strategy(): Generates Rate of Change signals and positions
- signal_ma_crossover(): Generates moving average crossover signals
- macd_signals(): Generates MACD trading signals
- backtest_signal_only(): Backtests any signal-based strategy, calculates equity curve and trades
- composite_momentum_strategy(): Combines ROC, MA, and MACD into a weighted momentum score for trading signals

# Future Improvements
- Include transaction costs and slippage
- Add opportunity for short selling and multi-share strategies
- Compare against a benchmark (e.g., S&P 500)