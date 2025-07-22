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
