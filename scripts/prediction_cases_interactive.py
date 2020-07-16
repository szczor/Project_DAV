from pmdarima import auto_arima
from datetime import datetime
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from pathlib import Path
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


data_folder = Path("../data/")

data = pd.read_csv(data_folder / 'che.csv')

dta = data[['new_cases', 'date']]
dta = dta['new_cases'].replace(to_replace=0, method='ffill')
dates = list(data['date'])

dta.index = [datetime.strptime(f"{date}{datetime.now().year}", "%d%b%Y") for date in dates]
result = seasonal_decompose(dta,
                            model='additive')

import warnings

warnings.filterwarnings("ignore")

# Fit auto_arima function to AirPassengers dataset
stepwise_fit = auto_arima(dta, start_p=1, start_q=1,
                          max_p=3, max_q=3, m=1,
                          start_P=0, seasonal=False,
                          d=None, D=None, trace=True,
                          error_action='ignore',  # we don't want to know if an order does not work
                          suppress_warnings=True,  # we don't want convergence warnings
                          stepwise=True)  # set to stepwise

# To print the summary
stepwise_fit.summary()
arma_mod11 = sm.tsa.ARMA(dta, (1, 1), freq='D').fit(disp=False)
pred = arma_mod11.predict(datetime(2020, 4, 30, 0, 0), datetime(2020, 5, 9, 0, 0))

x = np.asarray(data['new_cases'])

df = pd.read_csv('che.csv')[['date', 'new_cases']]
df.columns = ['Date', 'Number of new daily cases']

x = ['30Apr','01May','02May','03May','04May','05May','06May','07May','08May','09May']


fig = px.bar(df, x='Date', y='Number of new daily cases')
X = list(list(df['Date'])+x)
Y = list(list(df['Number of new daily cases'])+list(pred))

fig = go.Figure(data=[go.Bar(
    x= X,
    y=Y,
    marker_color=['rgba(82,95,216, 1)' for x in range(len(X)-len(pred))] +
                 ['rgba(242,63,63, 1)' for x in range(len(pred))]
)])

fig.update_layout(
    title='Predicted evolution of new daily COVID-19 cases\n'
             'in Switzerland using ARMA model',
    autosize=False,
    width=680,
    height=500,
    xaxis=dict(title='Date', tickangle=45, tickfont=dict(size=10), titlefont=dict(size=10)),
    yaxis=dict(title='New daily cases', tickfont=dict(size=10), titlefont=dict(size=10)),
    titlefont=dict(size=12),
    title_x=0.5
)

fig.write_html('plotly_prediction_cases.html', include_plotlyjs='cdn')