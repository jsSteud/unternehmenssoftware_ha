import pandas as pd

df = pd.read_csv('../csv/november.csv', index_col=[0])
df = df.drop(df[df['Tweet'].str.contains("RT @")].index, inplace=False)

df.to_csv('../csv/november_ohneRetweets.csv', sep='\t', encoding='utf-8')