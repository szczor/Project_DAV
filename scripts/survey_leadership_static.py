import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../data/survey_leadership.csv')

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8,6))

sns.barplot(x="label", y="val", data=data, color=(128/255,170/255,255/255), ax=ax)
ax.set_title('How strong is your trust in the political leadership\nin terms of COVID-19 crisis?', fontsize=12)
ax.set_xlabel('')
ax.set_xticklabels([el for el in data['label']], size=10)
ax.set_ylabel('Share of respondents', fontsize=10)
ax.set_yticks(np.arange(0,55,10))
ax.set_yticklabels([str(el)+'%' for el in np.arange(0,55,10)], fontsize=10)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 1, str(int(height))+'%',
            ha="center", size=9)

plt.text(0.92, -0.12, 'Source: SRG SSR, Die Schweiz und die Corona-Krise',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)

plt.text(0.1, -0.12, 'Details: March 21-23, 2020; 30460 respondents; 15 years and older',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)


plt.savefig('survey_leadership.png', dpi=400)

