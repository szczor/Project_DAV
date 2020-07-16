import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('survey_fear.csv')[['label', 'val']]
df.columns = ['', 'Share of respondents']

fig = px.bar(df, x='', y='Share of respondents')

fig.update_layout(
    title = 'Does the coronavirus (COVID-19) scare you?',
    titlefont = dict(size=12),
    title_x=0.5,
    autosize = False,
    width=680,
    height=500,
    xaxis=dict(
               tickmode = 'array',
               tickvals = [x for x in range(6)],
               ticktext = ['1= no'] + [df[''][x] for x in range(1,5)] + ['6= yes, very'],
               tickfont = dict(size=10)),

    yaxis=dict(tickmode = 'array',
               tickvals = np.arange(0,35,10),
               ticktext = [str(i)+'%' for i in np.arange(0,35,10)],
               tickfont = dict(size=10),
               titlefont = dict(size=10))
)

fig.write_html('plotly_fear.html', include_plotlyjs='cdn')