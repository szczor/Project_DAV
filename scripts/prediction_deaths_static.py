from pmdarima import auto_arima
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from pathlib import Path
import numpy as np

data_folder = Path("../data/")

data = pd.read_csv(data_folder / 'che.csv')

dta = data[['new_deaths', 'date']]
dta = dta['new_deaths'].replace(to_replace=0, method='ffill')
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
arima_mod011 = sm.tsa.ARIMA(dta, (1, 0, 1), freq='D').fit(disp=False)
pred = arima_mod011.predict(datetime(2020, 4, 30, 0, 0), datetime(2020, 5, 9, 0, 0))

x = np.asarray(data['new_deaths'])

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(np.arange(0, len(x), 1), x, color=(128 / 255, 170 / 255, 255 / 255))
ax.bar(np.arange(len(x), len(x) + len(pred), 1), pred, color=(255 / 255, 51 / 255, 51 / 255))
ax.set_title('Predicted evolution of new daily COVID-19 deaths\n'
             'in Switzerland using ARMA model', fontsize=12)
ax.set_ylabel('New daily deaths', fontsize=10)
ax.set_yticks(np.arange(0, 85, 20))
ax.set_yticklabels([x for x in np.arange(0, 85, 20)], fontsize=10)
ax.set_xticks([4, 35, 65])
ax.set_xticklabels(['Mar 1', 'Apr 1', 'May 1'], fontsize=10)

lgd = ax.legend(fontsize=10, frameon=True, loc=(0.65, 0.83))


def add_patches(legend):
    from matplotlib.patches import Patch

    handles, labels = [], []
    handles.append(Patch(facecolor=(128 / 255, 170 / 255, 255 / 255), edgecolor=(128 / 255, 170 / 255, 255 / 255)))
    handles.append(Patch(facecolor=(255 / 255, 51 / 255, 51 / 255), edgecolor=(255 / 255, 51 / 255, 51 / 255)))
    labels.append('Confirmed deaths')
    labels.append('Prediction')

    legend._legend_box = None
    legend._init_legend_box(handles, labels)
    legend._set_loc(legend._loc)
    legend.set_title(legend.get_title().get_text())


add_patches(lgd)

plt.text(1, -0.12, 'Source: ourworldindata.org',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)
ax.grid(axis='x')

plt.savefig('prediction_deaths.png', dpi=400)
