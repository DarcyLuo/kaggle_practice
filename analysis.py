import pandas as pd
df=pd.read_csv("data/abcnews-date-text.csv")
print(df.head())

#exploratory analysis
#count headline length
df['headline_length']=df['headline_text'].str.len()
print(df.head())
print(df['headline_length'].info())
#take-away: no missing data

#count headline words
df['headline_word_count'] = df['headline_text'].str.split().str.len()
print(df.head())
print(df['headline_word_count'].info())

print(df['headline_word_count'].min())
print(df['headline_word_count'].max())

#how many headline word count is 1 and what are they?

