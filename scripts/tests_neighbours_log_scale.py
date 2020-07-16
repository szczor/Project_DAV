import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

data_folder = Path("../data/")
file_to_open=data_folder/'ourworldindatatests.csv'
df = pd.read_csv('C:/Users/rysza/Desktop/python data analysis/Project/data/ourworldindatatests.csv', sep=",", error_bad_lines=False, index_col=2)
#filter switz and neeighbours

countries=['Switzerland']
df['Entity']=df['Entity'].str.split(' ').str[0]
df=df.loc[df['Entity'].isin(countries)]
df=df[['Entity','Cumulative total','Date']]

fig = go.Figure()
colors=['blue','green','red','yellow','black','cyan']

for name in countries:

    fig.add_trace(go.Scatter(
        x=df.loc[df['Entity'] == name]['Date'],
        y=df.loc[df['Entity'] == name]['Cumulative total'],
        mode='lines',
        name=name

)
)
fig.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactiveplots\\tests_neighbours.html')
fig_json_1 = fig.to_html(full_html=False)