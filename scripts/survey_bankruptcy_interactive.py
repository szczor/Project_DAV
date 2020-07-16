import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('survey_bankruptcy.csv')[['label', 'val']]
df.columns = ['', 'Likelihood of bankruptcy']

fig = px.bar(df, x='', y='Likelihood of bankruptcy')

fig.update_layout(
    title = 'In your opinion, how high is the likelihood of bankruptcy?',
    titlefont = dict(size=12),
    title_x=0.5,
    autosize = False,
    width=680,
    height=500,
    xaxis=dict(tickangle=45,
               tickmode = 'array',
               tickvals = [x for x in range(6)],
               ticktext = ['Holiday homes, apartments']+[df[''][x] for x in range(1,6)],
               tickfont = dict(size=10)),

    yaxis=dict(tickmode = 'array',
               tickvals = np.arange(0,45,10),
               ticktext = [str(i)+'%' for i in np.arange(0,45,10)],
               tickfont = dict(size=10),
               titlefont = dict(size=10))
)

fig.write_html('plotly_bankruptcy.html', include_plotlyjs='cdn')