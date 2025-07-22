import numpy as np

def sharpe_ratio(series, periods=365):
    return series.mean() / series.std() * np.sqrt(periods)

def max_drawdown(cumulative_returns):
    return (cumulative_returns / cumulative_returns.cummax() - 1).min()

def annualized_volatility(series, periods=365):
    return series.std() * np.sqrt(periods)
