import pandas as pd
import json
df = pd.read_csv('../data/twitter_raw.csv', on_bad_lines='skip')

df = df.dropna()
df.rename(columns = {df.keys()[0]:'author_id', df.keys()[1]:'cleaned_text', df.keys()[2]:'sentiment',
                    df.keys()[3]:'gcc', df.keys()[4]:'state', df.keys()[6]:'left', df.keys()[7]:'bottom',
                    df.keys()[8]:'right',df.keys()[9]:'top'}, inplace = True)
# bbox = left,bottom,right,top = min Longitude, min Latitude, max Longitude, max Latitude
df = df.drop([df.keys()[5],df.keys()[10], df.keys()[11]], axis=1)

df['cleaned_text'] = df['cleaned_text'].str.lower()
df['gcc'] = df['gcc'].str.lower()
df['gcc'] = df['gcc'].str[29:]
#df['state'] = df['state'][1:-2].str.lower()
df['left'] = df['left'].str[10:]
df['top'] = df['top'].str.extract(r'([-]?\d+\.\d+)')

to_num_cols = ['left', 'right', 'top']
df[to_num_cols] = df[to_num_cols].astype(float)

city_dict = {}
with open('../data/sal.json', 'r', encoding='utf-8') as sal_file:
    sal_data = json.load(sal_file)
    for location in sal_data.keys():
        #if sal_data.get(location).get('gcc')[1] != 'r'and sal_data.get(location).get('gcc')[1] != 'R': 
        city_dict[location] = sal_data.get(location).get('gcc')
#save city_dict str into DataFrame
df_sal = pd.DataFrame({'gcc': city_dict.keys(), 
                       'Greater Capital City': city_dict.values()})
# 'state, australia' cases are not recorded in sal.json
df_sal_add = pd.DataFrame({'gcc': ['new south wales','victoria',  'queensland', 'south australia', 
                                         'western australia', 'tasmania', 'northern territory', 
                                         'australia capital territory', 'other territories'],
                           'Greater Capital City': ['1gsyd', '2gmel','3gbri','4gade', '5gper','6ghob','7gdar', 
                                                    '8acte','9oter']})
frames = [df_sal, df_sal_add]
df_sal = pd.concat(frames)
df = pd.merge(df, df_sal, on='gcc')
df['Greater Capital City'].value_counts()
df.to_csv('../data/twitter_clean.csv')