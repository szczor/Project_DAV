import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
data_folder = Path("../data/")
plots_folder=Path('../static_plots/')

sns.set(style="whitegrid")
data=[['Scenario 1',14.8,29.5,49.2],['Scenario 2',17.7,35.4,59.0]]

df=pd.DataFrame(data,columns=['Scenario', '1 week','1 month' ,'2 months'])

df=pd.melt(df, id_vars=['Scenario'] , value_vars=['1 week','1 month' ,'2 months'])

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x="variable", y="value", hue='Scenario',data=df,palette='Blues')


for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 1,
            height,
            ha="center",fontsize=9) 
plt.xlabel('Shutdown duration',fontsize=10)
plt.ylabel('Added value loss in billion euros',fontsize=10)
plt.setp(ax.get_xticklabels(), fontsize=10)

plt.annotate('Source: ifo Institut',xy=(0.97,0.03),
            xycoords='figure fraction', horizontalalignment='right',
            verticalalignment='top', fontsize=7, color='#555555')
ax.set_ylim([0,75])
plt.legend(frameon=False,loc='upper center', bbox_to_anchor=(0.5, 0.95),
          fancybox=True, shadow=True, ncol=2,fontsize=11)
plt.yticks(ticks=[0,20,40,60],labels=['0','20','40','60'])
plt.title('Forecast for loss in added value due to the COVID-19 in \n Switzerland by duration of shutdowns',loc='center',fontsize=12)
fig.set_size_inches(8, 6)           
fig.savefig(plots_folder/'lossaddedvalue.png',dpi=400)