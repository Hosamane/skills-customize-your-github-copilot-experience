import os
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


DATA_FILE = Path(__file__).parent / "data.csv"
OUT_DIR = Path(__file__).parent / "outputs"


def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    if path.exists():
        df = pd.read_csv(path, parse_dates=["date"], dayfirst=True, infer_datetime_format=True)
    else:
        # generate sample data
        rng = pd.date_range("2021-01-01", periods=30, freq="D")
        df = pd.DataFrame({
            "date": rng,
            "category": ["A", "B", "C"] * 10,
            "value": (pd.np.random.rand(len(rng)) * 100).round(2),
            "x": pd.np.random.randn(len(rng)),
            "y": pd.np.random.randn(len(rng)) * 2 + 1,
        })
    return df


def ensure_out_dir():
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def create_matplotlib_plots(df: pd.DataFrame):
    sns.set(style="whitegrid")
    # Line plot (time series)
    plt.figure(figsize=(8, 4))
    df_sorted = df.sort_values("date")
    plt.plot(df_sorted["date"], df_sorted["value"], marker="o")
    plt.title("Value over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "line_plot.png", dpi=150)
    plt.close()

    # Histogram
    plt.figure(figsize=(6, 4))
    plt.hist(df["value"].dropna(), bins=15, color="#4c72b0")
    plt.title("Value Distribution")
    plt.xlabel("Value")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "histogram.png", dpi=150)
    plt.close()

    # Scatter (x vs y) colored by category
    plt.figure(figsize=(6, 5))
    sns.scatterplot(data=df, x="x", y="y", hue="category", palette="deep")
    plt.title("Scatter: x vs y")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "scatter.png", dpi=150)
    plt.close()


def create_plotly_plot(df: pd.DataFrame):
    fig = px.scatter(df, x="x", y="y", color="category", size="value", hover_data=["date", "value"])
    fig.update_layout(title="Interactive Scatter (Plotly)")
    fig.write_html(OUT_DIR / "interactive_scatter.html")


def main():
    ensure_out_dir()
    df = load_data()
    print("Data preview:\n", df.head())
    create_matplotlib_plots(df)
    create_plotly_plot(df)
    print(f"Plots written to: {OUT_DIR}")


if __name__ == "__main__":
    main()
