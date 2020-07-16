import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches
from pathlib import Path
data_folder = Path("../data/")
plots_folder=Path('../static_plots/')
xls = pd.ExcelFile(data_folder/'agegroups.xlsx')

df1 = pd.read_excel(xls, 'COVID19 Altersverteilung Hospit',header=6)

df1=df1[['Altersklasse','Total hospitalisiert: Anzahl']]
df1=df1.rename(columns={'Altersklasse':'agegroup','Total hospitalisiert: Anzahl':'hospitalized'})
df1=df1[:9]

df2=pd.read_excel(xls, 'COVID19 Altersverteilung TodF',header=6)
df2=df2[['Altersklasse','Total Todesfälle: Anzahl']]
df2=df2.rename(columns={'Altersklasse':'agegroup','Total Todesfälle: Anzahl':'deaths'})
df2=df2[:9]
df1['deaths']=df2['deaths'] 


fig, ax = plt.subplots(figsize=(8, 6))
sns.set_style("whitegrid")
sns.barplot(x='agegroup',y='hospitalized',data=df1,color="#80aaff")
sns.barplot(x='agegroup',y='deaths',data=df1,color='#ff3333')
sns.set_style("whitegrid")

for index, row in df1.iterrows():
    ax.text(index,row.hospitalized+20, round(row.hospitalized), color='black', ha="center",fontsize=9)

labels=[]
for i in df1['agegroup']:
    labels.append(i)
ax.set_xticklabels(labels ,rotation=0,fontsize=10)
plt.xlabel('age groups',fontsize=10)
plt.ylabel('')
plt.yticks(ticks=[0,250,500,750,1000],labels=['0','250','500','750','1000'])
ax.set_ylim([0,1250])
plt.title('Hospitalizations due to the COVID-19 in Switzerland by age group',loc='center',fontsize=12)
red_patch = mpatches.Patch(color='#ff3333', label='deaths')
blue_patch = mpatches.Patch(color="#80aaff", label='hospitalizations')
plt.legend(handles=[blue_patch,red_patch],frameon=False,loc='upper center', bbox_to_anchor=(0.5, 0.95),
          fancybox=True, shadow=True, ncol=2,fontsize=11)
plt.annotate('Source: Bundesamt für Gesundheit',xy=(0.98,0.03),
            xycoords='figure fraction', horizontalalignment='right',
            verticalalignment='top', fontsize=7, color='#555555')
plt.savefig(plots_folder/'Hospitalizations_due_to_the_COVID-19_in_Switzerland_by_age_group.png',dpi=400)
