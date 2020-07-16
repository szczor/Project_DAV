import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
data_folder = Path("../data/")
file_to_open=data_folder/'agegroups.xlsx'
xls = pd.ExcelFile(file_to_open)

df1 = pd.read_excel(xls, 'COVID19 Altersverteilung',header=6)

df1=df1[['Altersklasse','Männlich: Anzahl Fälle','Weiblich: Anzahl Fälle']]
df1=df1.rename(columns={'Altersklasse':'agegroup','Männlich: Anzahl Fälle':'male','Weiblich: Anzahl Fälle':'female'})
df1=df1[:9]


fig = go.Figure(data=[
    go.Bar(name='female', x=df1['agegroup'], y=df1['female']),
    go.Bar(name='male', x=df1['agegroup'], y=df1['male'])
])
fig.update_layout(
    barmode='group',
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
        'text': "Total cases in Switzerland by sex",
        'y':0.85,
        'x':0.55,
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
    legend=dict(x=0.85,y=0.95)
    )
fig.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactive_plots\\sex_age_group.html', include_plotlyjs='cdn')