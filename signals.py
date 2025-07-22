
def generate_ma_signal(df, window=20):
    ma = df.rolling(window=window).mean()
    return (df > ma).astype(int)

def compute_zscore(series, window=20):
    mean = series.rolling(window=window).mean()
    std = series.rolling(window=window).std()
    return (series - mean) / std

def generate_mean_reversion_signal(prices, window=20, threshold=1):
    zscores = compute_zscore(prices, window)
    return ((zscores < -threshold) | (zscores > threshold)).astype(int)

def blend_signals(momentum_signal, reversion_signal, alpha=0.5):
    return alpha * momentum_signal + (1 - alpha) * reversion_signal

