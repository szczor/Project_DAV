import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('../data/che.csv')
new_cases = data[['date','new_cases']]
new_deaths = data[['date','new_deaths']]
dates = data['date']

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(x='date', y='new_cases', data=new_cases, color=(128/255,170/255,255/255), ax=ax)
sns.barplot(x='date',y='new_deaths', data=new_deaths, color=(255/255,51/255,51/255), ax=ax)
ax.set_title('New daily COVID-19 cases and deaths in Switzerland', fontsize=12)
ax.set_xticks([4,35,65])
ax.set_xticklabels(['Feb 1', 'Mar 1', 'Apr 1'], fontsize=10)
ax.set_xlabel('', fontsize=0)
ax.set_ylabel('New confirmed cases/deaths', fontsize=10)

lgd = ax.legend(fontsize=10, frameon=False, loc=(0.75,0.83))

def add_patch(legend):
    from matplotlib.patches import Patch

    handles, labels = [], []
    handles.append(Patch(facecolor=(128/255,170/255,255/255), edgecolor=(128/255,170/255,255/255)))
    handles.append(Patch(facecolor=(255/255,51/255,51/255), edgecolor=(255/255,51/255,51/255)))
    labels.append('New cases')
    labels.append('New deaths')

    legend._legend_box = None
    legend._init_legend_box(handles, labels)
    legend._set_loc(legend._loc)
    legend.set_title(legend.get_title().get_text())

add_patch(lgd)

plt.text(1, -0.12, 'Source: ourworldindata.org',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)



plt.savefig('new_daily_cases_deaths.png', dpi=400)
