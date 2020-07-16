import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('survey_leadership.csv')[['label', 'val']]
df.columns = ['', 'Share of respondents']

fig = px.bar(df, x='', y='Share of respondents')

fig.update_layout(
    title = 'How strong is your trust in the political leadership\nin terms of COVID-19 crisis?',
    titlefont = dict(size=12),
    title_x=0.5,
    autosize = False,
    width = 680,
    height = 500,
    xaxis=dict(
               tickmode = 'array',
               tickvals = [x for x in range(6)],
               ticktext = [df[''][x] for x in range(0,len(df['']))],
               tickfont = dict(size=10)),

    yaxis=dict(tickmode = 'array',
               tickvals = np.arange(0,55,10),
               ticktext = [str(i)+'%' for i in np.arange(0,55,10)],
               tickfont = dict(size=10),
               titlefont = dict(size=10))
)

fig.write_html('plotly_leadership.html', include_plotlyjs='cdn')