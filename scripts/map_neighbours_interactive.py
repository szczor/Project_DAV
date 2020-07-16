import geojson
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go

data_folder = Path("../data/")

path_to_file=data_folder/'countries.geojson'

countries=['France','Italy','Switzerland','Austria','Germany','Liechtenstein']
newgj=[]
with open(path_to_file) as f:
    gj = geojson.load(f)
for feature in gj['features']:
    if (feature['properties']['ADMIN']) in countries:
        newgj.append(feature)

gj['features']=newgj



file_to_open=data_folder/'ourworldindatadeathetc.csv'
df = pd.read_csv(file_to_open, sep=",", error_bad_lines=False)
df=df[['location','total_cases','date']]
df = df.loc[df['location'].isin(countries)]
df=pd.pivot_table(df,values=['total_cases'],index='date',columns='location').reset_index()
df.set_axis(['date','Austria','France','Germany','Italy','Liechtenstein','Switzerland'],axis=1,inplace=True)
df=df[(df['date'] > '2020-02-25')]
data_slider = []
data_for_slider=list(df['date'])

        
for date in df["date"].unique():
    one_date = df[df["date"] == date].drop(["date"], axis = 1)
    one_date=one_date.T
    new_df = pd.DataFrame({"country": one_date.index,
                           "cases": one_date.T.values.tolist()[0]})
    data_one_date = dict(
                        type='choropleth', 
                        geojson = gj, 
                        colorscale = 'Reds', 
                        locations = new_df["country"],
                        featureidkey = 'properties.ADMIN',
                        z=new_df["cases"],
                        locationmode='geojson-id',
                        text = new_df["country"],
                        zmin = 0,
                        zmax = 201000,
        
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
             showlakes = True, 
             lakecolor = 'blue',
             lataxis = {"range": [37, 55]}, 
             lonaxis = {"range": [-7, 18]}, 
             showland = False,
             countrycolor = 'white'
            ),
    sliders=sliders,
    margin=dict(l=20, r=0, t=0, b=100),

)
fig=go.Figure(data=data_slider,layout=layout)
fig.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactive_plots\\map_neighbours.html', include_plotlyjs='cdn')