import plotly.express as px
import pandas as pd

df = pd.read_csv('che.csv')[['date', 'new_cases']]
df.columns = ['Date', 'new_cases']
growth = [0]
for i in range (1,len(df['new_cases'])):
    if df['new_cases'][i-1] == 0:
        growth.append(df['new_cases'][i] / df['new_cases'][i-2])
    else:
        growth.append(df['new_cases'][i]/df['new_cases'][i-1])

df['Growth factor'] = growth

fig = px.bar(df, x='Date', y='Growth factor')

fig.update_layout(
    title='Growth factor of epidemic in Switzeralnd (new cases/new cases on the previous day)',
    autosize=False,
    width=680,
    height=500,
    xaxis=dict(tickangle=45, tickfont=dict(size=10), titlefont=dict(size=10)),
    yaxis=dict(tickfont=dict(size=10), titlefont=dict(size=10)),
    titlefont=dict(size=12),
    title_x=0.5
)

fig.write_html('plotly_growth.html', include_plotlyjs='cdn')