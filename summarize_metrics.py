def summarize_metrics(name, returns, cumulative):
    return {
        "Strategy": name,
        "Sharpe": sharpe_ratio(returns),
        "Sortino": sortino_ratio(returns),
        "CAGR": cagr(cumulative),
        "Calmar": calmar_ratio(cumulative),
        "Max DD": max_drawdown(cumulative),
        "Volatility": annualized_volatility(returns)
    }

summary_df = pd.DataFrame([
    summarize_metrics("Momentum", returns_momentum, cum_momentum),
    summarize_metrics("Mean Reversion", returns_reversion, cum_reversion),
    summarize_metrics("Blended", returns_blended, cum_blended)
])

print("\n📊 Strategy Comparison Summary:")
print(summary_df.set_index("Strategy").round(4))
