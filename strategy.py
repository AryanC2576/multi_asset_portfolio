def compute_volatility(returns, window=20):
    return returns.rolling(window=window).std()

def compute_inv_vol_weights(volatility, signals):
    inv_vol = 1 / volatility
    inv_vol = inv_vol * signals
    weights = inv_vol.div(inv_vol.sum(axis=1), axis=0).fillna(0)
    return weights

def compute_portfolio_returns(returns, weights):
    return (returns * weights.shift(1)).sum(axis=1)
