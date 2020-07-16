from urllib.request import urlopen
import json
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
data_folder = Path("../data/")
file_to_open=data_folder/'covid19_cases_switzerland_openzh.csv'
df = pd.read_csv(file_to_open, sep=",", error_bad_lines=False)

df=df.fillna(method='ffill')
df=df.fillna(0)

with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/switzerland.geojson') as response:
    cantons_map = json.load(response)
cantons = []
for x in range(len(cantons_map['features'])):
    cantons.append(cantons_map['features'][x]['properties']['name'])
cantons.sort()
data_slider = []
data_for_slider=list(df['Date'])
        
for date in df["Date"].unique():
    one_date = df[df["Date"] == date].drop(["Date", "CH"], axis = 1)
    one_date.columns=cantons
    one_date=one_date.T
    new_df = pd.DataFrame({"canton": one_date.index,
                           "cases": one_date.T.values.tolist()[0]})
    data_one_date = dict(
                        type='choropleth', 
                        geojson = cantons_map, 
                        colorscale = 'Reds', 
                        locations = new_df["canton"],
                        featureidkey = 'properties.name',
                        z=new_df["cases"],
                        locationmode='geojson-id',
                        zmin = 0,
                        zmax = 4760,
        
                        marker = dict(
                            # for the lines separating states
                            line = dict (color = 'black', width = 0.5) 
                        ),
                        colorbar = dict(title = "Number of cases") 
                        )
    data_slider.append(data_one_date)

steps = []

for i in range(len(data_slider)):
    step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label=data_for_slider[i])
    step['args'][1][i] = True
    steps.append(step)
sliders = [dict(active=0, steps=steps, ticklen = 20)]

layout = dict(
    width = 680,
    height = 500, 
    hovermode = "closest",
    geo=dict(scope='europe',
             showlakes = False, 
             lataxis = {"range": [46, 48]}, 
             lonaxis = {"range": [5.5, 10.5]}, 
             showland = False,
             countrycolor = 'white'
            ),
    sliders=sliders,
    margin=dict(l=20, r=0, t=0, b=100),

)
fig=go.Figure(data=data_slider,layout=layout)
fig.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactive_plots\\map_counties.html', include_plotlyjs='cdn')