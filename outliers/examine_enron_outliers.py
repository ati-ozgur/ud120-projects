import pandas as pd
df = pd.DataFrame.from_dict(data_dict,orient='index')
df[['bonus', 'salary']] = df[['bonus', 'salary']].astype(float)
