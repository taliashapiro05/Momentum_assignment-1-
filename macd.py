def macd_signals(prices, short_window=12, long_window=26, signal_window=9):
    signals = []
    short_ema = prices.ewm(span=short_window, adjust=False).mean()
    long_ema = prices.ewm(span=long_window, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()

    for i in range(len(prices)):
        if macd_line[i] > signal_line[i]:
            signals.append(1)  # Buy signal
        else:
            signals.append(0)  # Sell signal

    return signals