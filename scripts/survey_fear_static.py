import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../data/survey_fear.csv')

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(8,6))
sns.barplot(x="label", y="val", data=data, color=(128/255,170/255,255/255), ax=ax)
ax.set_title('Does the coronavirus (COVID-19) scare you?', fontsize=12)
ax.set_xlabel('1-3 = no; 4-6 = yes', fontsize=10)
ax.set_xticklabels(['1= no, not at all',2 ,3, 4, 5, '6= yes, very'], fontsize=10)
ax.set_ylabel('Share of respondents', fontsize=10)
ax.set_yticks(np.arange(0,35,10))
ax.set_yticklabels([str(el)+'%' for el in np.arange(0,35,10)], fontsize=10)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 1, str(int(height))+'%',
            ha="center", size=9)

plt.text(1, -0.12, 'Source: dieMarktforscher.org',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)

plt.text(0.1, -0.12, 'Details: Switzerland; March 9-11; 18-69 years; 520 respondents',
         horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes, size=7)

plt.savefig('survey_fear.png', dpi=400)

