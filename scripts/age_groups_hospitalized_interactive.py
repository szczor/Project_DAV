import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
data_folder = Path("../data/")
interactive_plots=Path('../interactive_plots/')
file_to_open=data_folder/'agegroups.xlsx'
xls = pd.ExcelFile(file_to_open)

df1 = pd.read_excel(xls, 'COVID19 Altersverteilung Hospit',header=6)

df1=df1[['Altersklasse','Total hospitalisiert: Anzahl']]
df1=df1.rename(columns={'Altersklasse':'agegroup','Total hospitalisiert: Anzahl':'hospitalized'})
df1=df1[:9]

df2=pd.read_excel(xls, 'COVID19 Altersverteilung TodF',header=6)
df2=df2[['Altersklasse','Total Todesfälle: Anzahl']]
df2=df2.rename(columns={'Altersklasse':'agegroup','Total Todesfälle: Anzahl':'deaths'})
df2=df2[:9]
df1['deaths']=df2['deaths'] 

fig = go.Figure(data=[
    go.Bar(name='Hospitalized', x=df1['agegroup'], y=df1['hospitalized']),
    go.Bar(name='Deaths', x=df1['agegroup'], y=df1['deaths'])
])
fig.update_layout(
    barmode='overlay',
    xaxis_title="Age groups",
    yaxis_title="",
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='black',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='black',
        )
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        showline=True,
        showticklabels=True
    ),
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    plot_bgcolor='white',
    title={
        'text': "Total deaths and hospitalizations in Switzerland by age groups",
        'y':0.85,
        'x':0.53,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
        size=16)
        },
    width=680,
    height=500,
    autosize=True,
    template='plotly_white',
    showlegend=True,
    legend=dict(x=0.3,y=0.95),
    legend_orientation="h"
    )
fig.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactive_plots\\age_group_hospitalized.html', include_plotlyjs='cdn')