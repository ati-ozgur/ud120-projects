import pandas as pd
df = pd.DataFrame.from_dict(data_dict,orient='index')
df[['bonus', 'salary']] = df[['bonus', 'salary']].astype(float)

df.sort(columns="salary",ascending=False).head()["salary"]
df.sort(columns="bonus",ascending=False).head()["bonus"]
