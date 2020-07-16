import plotly.express as px
import pandas as pd

df = pd.read_csv('che.csv')[['date', 'total_deaths']]
df.columns = ['Date', 'Total number of deaths']

fig = px.line(df, x='Date', y='Total number of deaths')

fig.update_layout(
    title='Total number of COVID-19 deaths in Switzerland',
    autosize=False,
    width=680,
    height=500,
    xaxis=dict(tickangle=45, tickfont=dict(size=10), titlefont=dict(size=10)),
    yaxis=dict(tickfont=dict(size=10), titlefont=dict(size=10)),
    titlefont=dict(size=12),
    title_x=0.5
)

fig.write_html('plotly_deaths.html', include_plotlyjs='cdn')