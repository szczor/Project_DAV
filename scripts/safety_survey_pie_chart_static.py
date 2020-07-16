import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
data_folder = Path("../data/")
plots_folder=Path('../static_plots/')

sns.set_style("whitegrid")
df = pd.DataFrame({'y': [0.03,0.15,0.22,0.6],
                },
                  index=['I do not know','More than once a day','Once a day','Never'])

color=sns.color_palette("Blues", n_colors=4)
title1='How often do you currently stay near other people outside your \n household  (closer than 2 meters and longer than 15 minutes)?'
plot = df.plot.pie(y='y', figsize=(8, 6), autopct='%1.0f%%', startangle=270, pctdistance=0.75,colors=color, textprops={'color':'white', 'weight':'bold', 'fontsize':12})
centre_circle = plt.Circle((0,0),0.50,fc='white')

plt.title(title1,fontsize=12,loc='center')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.legend(frameon=False,loc='upper center', bbox_to_anchor=(0.5, 0),
          fancybox=True, shadow=True, ncol=2,fontsize=11)
plt.ylabel('')
# Equal aspect ratio ensures that pie is drawn as a circle
plt.annotate('Source: Bundesamt für Gesundheit',xy=(0.98,0.03),
            xycoords='figure fraction', horizontalalignment='right',
            verticalalignment='top', fontsize=7, color='#555555')
plt.annotate('2097 respondents',xy=(0.2,0.03),
            xycoords='figure fraction', horizontalalignment='right',
            verticalalignment='top', fontsize=7, color='#555555')

plt.savefig(plots_folder/'safety_survey_pie_chart.png',dpi=400)
