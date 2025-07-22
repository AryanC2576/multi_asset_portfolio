def generate_ma_signal(df, window=20):
    ma = df.rolling(window=window).mean()
    return (df > ma).astype(int)
