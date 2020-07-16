import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path
data_folder = Path("../data/")
plots_folder=Path('../static_plots/')
df = pd.read_csv(data_folder/'applemobilitytrends-2020-04-28.csv', sep=",", error_bad_lines=False, index_col=2)
#filter Switzerland
df=df[df['region']=='Switzerland']
df=df.drop(columns=['region','alternative_name','geo_type']).T
df=df.reset_index()
df=df.rename(columns={'index':'date'})
df=df.melt(id_vars=["date"], 
        var_name="transportation", 
        value_name="value")

fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(x='date',y='value',hue='transportation',data=df,palette=['red','purple','orange'])
ticktextx=['Jan 15 \n 2020',"Feb 1",'Feb 15','Mar 1','Mar 15','Apr 1','Apr 15','May 1']
tickvalsx=['2020-01-15',"2020-02-01","2020-02-15","2020-03-01","2020-03-15","2020-04-01","2020-04-15","2020-05-01"]
ticktexty=['-60%',"-20%",'+20%','+60%']
tickvalsy=[ 40,80,120,160]
plt.ylabel('')
plt.xlabel('')
plt.xticks(ticks=tickvalsx,labels=ticktextx,fontsize=10,rotation=0)
plt.yticks(ticks=tickvalsy,labels=ticktexty,fontsize=10)
plt.grid(axis='x')
plt.title('Switzerland mobility trends',loc='center',fontsize=12)
ax.set_xlim(-10,133)
ax.set_ylim(20,150)
coord=[100,73.68,38.42,58.86]
ax.text(110, coord[0], 'Baseline', color='dimgray', va='center', fontweight='bold',fontsize=11)
ax.text(110, coord[1], 'driving -26%', color='red', va='center',fontsize=11)
ax.text(110, coord[2], 'transit -62%', color='purple', va='center',fontsize=11)
ax.text(110, coord[3], 'walking -41%', color='orange', va='center',fontsize=11)
ax.get_legend().remove()

plt.plot([-10,100],[100,100],c='dimgray')
plt.annotate('Source: Apple mobility trends',xy=(0.97,0.03),
            xycoords='figure fraction', horizontalalignment='right',
            verticalalignment='top', fontsize=7, color='#555555')          
fig.savefig(plots_folder/'transportation.png',dpi=400)