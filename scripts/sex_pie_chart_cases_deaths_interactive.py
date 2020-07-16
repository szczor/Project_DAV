from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from pathlib import Path
data_folder = Path("../data/")
file_to_open=data_folder/'agegroups.xlsx'
xls = pd.ExcelFile(file_to_open)

df1 = pd.read_excel(xls, 'COVID19 Altersverteilung',header=6)
df2 = pd.read_excel(xls, 'COVID19 Altersverteilung TodF',header=6)
df1=df1[['Altersklasse','Männlich: Anzahl Fälle','Weiblich: Anzahl Fälle']]
df1=df1.rename(columns={'Altersklasse':'agegroup','Männlich: Anzahl Fälle':'male','Weiblich: Anzahl Fälle':'female'})
df1=df1[:9]
df2=df2[['Altersklasse','Männlich: Anzahl Todesfälle','Weiblich: Inzidenz Todesfälle']]
df2=df2.rename(columns={'Altersklasse':'agegroup','Männlich: Anzahl Todesfälle':'dmale','Weiblich: Inzidenz Todesfälle':'dfemale'})
df2=df2[:9]
newdf=pd.DataFrame({'male': [df1['male'].sum()],'female': [df1['female'].sum()]}).T.reset_index().rename(columns={'index':'sex',0:'cases'})
newdf2=pd.DataFrame({'male': [df2['dmale'].sum()],'female': [df2['dfemale'].sum()]}).T.reset_index().rename(columns={'index':'sex',0:'cases'})


fig = px.pie(newdf, values='cases', names='sex', title='Cases of COVID-19 by sex', color_discrete_sequence=['cornflowerblue','tomato'])
fig.update_layout(legend=dict(x=0.365, y=-0.1),legend_orientation="h",title=dict(x=0.5),    width=680,
    height=500)
fig.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactive_plots\\sex_pie_chart_1.html', include_plotlyjs='cdn')

fig2=px.pie(newdf2, values='cases', names='sex', title='Deaths from COVID-19 by sex', color_discrete_sequence=['tomato','cornflowerblue'])
fig2.update_layout(legend=dict(x=0.365, y=-0.1),legend_orientation="h",title=dict(x=0.5),    width=680,
    height=500)
fig2.write_html('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\interactive_plots\\sex_pie_chart_2.html', include_plotlyjs='cdn')