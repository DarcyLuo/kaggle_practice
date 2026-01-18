import pandas as pd
df=pd.read_csv("data/abcnews-date-text.csv")
print(df.head())

#exploratory analysis
#count headline length
df['headline_length']=df['headline_text'].str.len()
print(df.head())
print(df['headline_length'].info())