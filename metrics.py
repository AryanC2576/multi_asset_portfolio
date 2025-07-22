import numpy as np

def sharpe_ratio(series, periods=365):
    """Risk-adjusted return using standard deviation"""
    return series.mean() / series.std() * np.sqrt(periods)

def sortino_ratio(series, periods=365):
    """Risk-adjusted return using downside deviation"""
    downside = series[series < 0]
    downside_std = downside.std()
    if downside_std == 0:
        return np.nan
    return series.mean() / downside_std * np.sqrt(periods)

def max_drawdown(cumulative_returns):
    """Worst % drop from portfolio peak"""
    return (cumulative_returns / cumulative_returns.cummax() - 1).min()

def annualized_volatility(series, periods=365):
    """Total risk (volatility) annualized"""
    return series.std() * np.sqrt(periods)

def cagr(cumulative_returns, periods_per_year=365):
    """Compound Annual Growth Rate"""
    total_return = cumulative_returns.iloc[-1] / cumulative_returns.iloc[0]
    num_years = len(cumulative_returns) / periods_per_year
    return total_return**(1 / num_years) - 1

def calmar_ratio(cumulative_returns):
    """Return to drawdown ratio"""
    return cagr(cumulative_returns) / abs(max_drawdown(cumulative_returns))
