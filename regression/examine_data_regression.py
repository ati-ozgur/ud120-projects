# examine_data_regression.py
import pandas as pd
df = pd.DataFrame.from_dict(dictionary,orient='index')
df[['bonus', 'salary']] = df[['bonus', 'salary']].astype(float)



df["salary"].sum()

df["bonus"].sum()

sum(target_train + target_test)

