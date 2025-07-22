import matplotlib.pyplot as plt
import seaborn as sns

def plot_cumulative_returns(cumulative_assets, cumulative_portfolio,figname="cummulative_returns"):
    plt.figure(figsize=(12, 6))
    for coin in cumulative_assets.columns:
        plt.plot(cumulative_assets[coin], label=f"{coin} Buy & Hold")
    plt.plot(cumulative_portfolio, label="Vol-Adjusted Momentum Portfolio", linewidth=2.5, color='black')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{figname}.png")
    plt.show()

def plot_correlation_heatmap(returns,figname="correlation_heatmap"):
    plt.figure(figsize=(6, 4))
    sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Asset Return Correlation")
    plt.tight_layout()
    plt.savefig(f"{figname}.png")
    plt.show()

def plot_all_strategies(cum_momentum, cum_reversion, cum_blended,figname="strategy comparision"):
    plt.figure(figsize=(12, 6))
    plt.plot(cum_momentum, label="Momentum Only", linewidth=2)
    plt.plot(cum_reversion, label="Mean Reversion Only", linewidth=2)
    plt.plot(cum_blended, label="Blended Strategy", linewidth=3, color='black')
    plt.title("Cumulative Returns: Momentum vs Mean Reversion vs Blended")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Portfolio Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{figname}.png")
    plt.show()
