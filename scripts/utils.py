import pandas as pd

def drop_prepandemic_dates(data):
    prepandemic_dates = []
    for index, row in data.iterrows():
        if row['new_cases'] > 0:
            break
        prepandemic_dates.append((index))
    return data.drop(labels=prepandemic_dates)

def convert_dates(data):
    months = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
              '07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    for index, row in data.iterrows():
        data.at[index,'date'] = row['date'][-2:] + months[row['date'][5:7]]
    return data

def save_ch_neighbours(anim=False, filename='ourworldindatadeathetc.csv'):
    df = pd.read_csv(filename)
    che = df.loc[df['location'] == 'Switzerland']
    fra = df.loc[df['location'] == 'France']
    ita = df.loc[df['location'] == 'Italy']
    ger = df.loc[df['location'] == 'Germany']
    aut = df.loc[df['location'] == 'Austria']
    lie = df.loc[df['location'] == 'Liechtenstein']

    countries = [che, fra, ita, ger, aut, lie]
    codes = ['che', 'fra', 'ita', 'ger', 'aut', 'lie']

    for i in range(len(countries)):
        if anim:
            convert_dates(drop_prepandemic_dates(countries[i])).to_csv('%s_anim.csv' % (codes[i]))
        else:
            convert_dates(drop_prepandemic_dates(countries[i])).to_csv('%s.csv'%(codes[i]))

def load_ch_neighbours(anim=False):
    if anim:
        return [pd.read_csv('che_anim.csv'), pd.read_csv('fra_anim.csv'), \
               pd.read_csv('ita_anim.csv'), pd.read_csv('ger_anim.csv'), \
               pd.read_csv('aut_anim.csv'), pd.read_csv('lie_anim.csv')]
    else:
        return pd.read_csv('../data/che.csv'), pd.read_csv('fra.csv'), \
               pd.read_csv('ita.csv'), pd.read_csv('ger.csv'), \
               pd.read_csv('aut.csv'), pd.read_csv('lie.csv')

