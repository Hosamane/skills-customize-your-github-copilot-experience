from pathlib import Path
import pandas as pd
import plotly.express as px


ROOT = Path(__file__).parent
DATA_FILE = ROOT / "data.csv"
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"], infer_datetime_format=True)
    return df


def make_charts(df: pd.DataFrame):
    figs = {}
    # Time series line
    if "date" in df.columns and "value" in df.columns:
        figs["time_series"] = px.line(df.sort_values("date"), x="date", y="value", title="Value Over Time", hover_data=df.columns)

    # Scatter colored by category
    if "x" in df.columns and "y" in df.columns:
        color_col = "category" if "category" in df.columns else None
        figs["scatter"] = px.scatter(df, x="x", y="y", color=color_col, size="value" if "value" in df.columns else None, title="Scatter Plot", hover_data=df.columns)

    # Bar chart of category counts
    if "category" in df.columns:
        cat_counts = df["category"].value_counts().reset_index()
        cat_counts.columns = ["category", "count"]
        figs["category_bar"] = px.bar(cat_counts, x="category", y="count", title="Category Counts")

    return figs


def assemble_report(figs: dict, df: pd.DataFrame):
    parts = []
    parts.append("<html><head><meta charset='utf-8'><title>Interactive Data Story</title></head><body>")
    parts.append("<h1>Interactive Data Story</h1>")
    parts.append("<p>Dataset preview:</p>")
    parts.append(df.head().to_html(index=False))

    captions = {
        "time_series": "Time series shows trends and seasonal changes.",
        "scatter": "Scatter plot highlights relationships between x and y colored by category.",
        "category_bar": "Category counts show distribution across groups."
    }

    for key, fig in figs.items():
        html_fragment = fig.to_html(full_html=False, include_plotlyjs='cdn')
        parts.append(f"<h2>{fig.layout.title.text if fig.layout.title.text else key}</h2>")
        parts.append(f"<p>{captions.get(key, '')}</p>")
        parts.append(html_fragment)

    parts.append("</body></html>")
    report_path = OUT_DIR / "report.html"
    report_path.write_text("\n".join(parts), encoding="utf-8")
    return report_path


def main():
    df = load_data()
    figs = make_charts(df)
    report = assemble_report(figs, df)
    print("Report generated:", report)


if __name__ == "__main__":
    main()
