from utils import load_ch_neighbours
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = load_ch_neighbours(anim=True)
dates = data[1]['date']

for i in range(len(data)):
    data[i] = np.asarray(data[i]['total_cases'])
    data[i] = np.pad(data[i], (96-len(data[i]), 0), 'constant', constant_values=(0, 0))
x = np.arange(0,len(dates),1)
y = data

def plot(x, y, index, colors):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('Total confirmed cases of COVID-19 in Switzerland and its neighbours')
    ax.set_xlim(0,len(x)+5)
    ax.set_xticks([4, 35, 65, 96])
    ax.set_xticklabels(['Feb 1', 'Mar 1', 'Apr 1', 'May 1'], fontsize=10)
    if index < 29:
        ax.set_ylim(0,85)
        ax.set_yticks(np.arange(0,90,10))
        ax.set_yticklabels([x for x in np.arange(0,90,10)], fontsize=10)
    else:
        ax.set_ylim(0,int(1.1*np.max([y[j][index] for j in range(len(y))])))
    lgd = ax.legend(loc='upper left')

    def add_patches(legend, colors):
        from matplotlib.patches import Patch
        handles, labels = [], []
        for col in colors:
            handles.append(Patch(facecolor=col, edgecolor=col))
        labels = ['Switzerland','France','Italy','Germany','Austria','Liechtenstein']

        legend._legend_box = None
        legend._init_legend_box(handles, labels)
        legend._set_loc(legend._loc)
        legend.set_title(legend.get_title().get_text())

    add_patches(lgd, colors)

    plt.text(1, -0.12, 'Source: ourworldindata.org',
             horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes, size=7)

    plt.text(-0.12, 0.5, 'Total confirmed cases',
             horizontalalignment='center',
             verticalalignment='center', transform=ax.transAxes, size=10, rotation=90)

    for i in range(len(y)):
        ax.plot(x[0:index+1],y[i][0:index+1], color=colors[i])

    if index < 10:
        plt.savefig('animation/anim0%d.png' % (index), dpi=150)
    else:
        plt.savefig('animation/anim%d.png' % (index), dpi=150)
    plt.clf()

colors = [(102/255, 140/255, 255/255),(255/255, 128/255, 255/255),
          (255/255, 51/255, 51/255),(255/255, 214/255, 51/255),
          (102/255, 153/255, 0/255),(198/255, 140/255, 83/255)]
for i in range(len(x)):
    plot(x,y,i, colors)




