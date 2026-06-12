# 📘 Assignment: Python Data Visualization

## 🎯 Objective

Practice creating clear, informative static and interactive charts using `matplotlib` and `plotly`. Students will load a dataset, explore visualization types, and produce publication-ready figures.

## 📝 Tasks

### 🛠️ Data Loading & Preparation

#### Description
Load a CSV dataset, clean or transform fields as needed, and prepare data structures suitable for plotting (aggregations, groupings, date parsing).

#### Requirements
Completed work should:

- Load a CSV file (e.g., with `pandas.read_csv`) and show the first 5 rows
- Handle missing values (drop or impute) and parse dates where relevant
- Provide a short summary of the dataset (columns, dtypes, basic stats)

Example commands:

```
pip install pandas matplotlib plotly
python -c "import pandas as pd; print(pd.read_csv('data.csv').head())"
```


### 🛠️ Static Charts with Matplotlib

#### Description
Create common static visualizations using `matplotlib` (and optionally `seaborn`) for exploratory and presentation purposes.

#### Requirements
Completed work should:

- Produce at least three different chart types (e.g., line chart, histogram, bar chart, scatter plot)
- Include axis labels, titles, and legends where appropriate
- Save plots to image files (PNG or SVG) with a suitable resolution

Minimal `matplotlib` example:

```
import matplotlib.pyplot as plt
plt.plot([1,2,3], [4,5,6])
plt.title('Example')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('plot.png', dpi=150)
```


### 🛠️ Interactive Visualizations with Plotly

#### Description
Build at least one interactive plot using `plotly` that supports hovering, zooming, and exporting.

#### Requirements
Completed work should:

- Create an interactive chart (e.g., interactive scatter, line, or bar chart) using `plotly.express` or `plotly.graph_objects`
- Include informative hover text and axis labels
- Provide instructions for viewing the plot (e.g., run script to open in browser or save as HTML)

Minimal `plotly` example:

```
import plotly.express as px
fig = px.scatter(df, x='x', y='y', color='category', hover_data=['info'])
fig.write_html('interactive.html')
```


### 🛠️ Storytelling & Presentation

#### Description
Combine multiple visualizations and short captions to tell a clear data-driven story.

#### Requirements
Completed work should:

- Include at least two figures with short captions explaining the insight each figure shows
- Export a small report (Markdown, PDF, or HTML) that includes figures and interpretations


### 🛠️ Reproducibility & Examples

#### Description
Provide reproducible commands and at least one example output snippet or image.

#### Requirements
Completed work should:

- Include `requirements.txt` or a `pip` install command listing major dependencies
- Show sample commands to run the scripts and produce outputs

Example `requirements.txt` lines:

```
pandas
matplotlib
plotly
seaborn  # optional
```

---

Optional extensions (encouraged):

- Create interactive dashboards with `dash` or `streamlit`
- Add animations (matplotlib animation or Plotly frames)
- Implement advanced statistical visualizations (heatmaps, pairplots, violin plots)
