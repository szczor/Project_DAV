import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from pathlib import Path
data_folder = Path("../data/")
plots_folder=Path('../static_plots/')
switzerland_folder=Path('../data/swisscanton/')


fp=switzerland_folder/'ch-cantons.shp'
map_df = gpd.read_file(fp)
map_df.plot()
map_df['Canton']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
xls = pd.ExcelFile(data_folder/'agegroups.xlsx')

df = pd.read_excel(xls, 'COVID19 Kantone',header=6)
df=df[['Kanton','Inzidenz/100 000']].rename(columns={'Kanton':'Canton','Inzidenz/100 000':'cases'})

merged = map_df.set_index('Canton').join(df.set_index('Canton'))

variable = 'cases'
vmin, vmax = 92.7, 1031.1

fig, ax = plt.subplots(figsize=(8,6))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='white', legend=True, cax=cax)
ax.axis('off')
ax.set_title('Cases per 100 thousand inhabitants by cantons', fontdict={'fontsize': '12', 'fontweight' : '3'})
ax.annotate('Source: Bundesamt für Gesundheit ',xy=(0.66, .18),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=7, color='#555555')
fig.set_size_inches(8, 6)
fig.savefig(plots_folder/'cases_per_100k_by_cantons.png', dpi=400)