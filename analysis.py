import pandas as pd
import matplotlib.pyplot as plt

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
one_word_headlines = df.loc[df['headline_word_count'] == 1, 'headline_text']
print(one_word_headlines)

one_word_count = (df['headline_word_count'] == 1).sum()
one_word_count
#1248 of the headlines contains just one word

print(one_word_headlines.value_counts())
#through value counts function, we can see many headline texts are repetitive.
one_word_counts = one_word_headlines.value_counts().reset_index()
one_word_counts.columns = ['headline_text', 'count']
one_word_counts.to_excel('one_word_headlines.xlsx', index=False)
#for one-word headlines, they contain very few information for judgement. Many of them might
#just stand for one section, so we will pay less attention to these headlines;
# After checking the excel file of the one-word headlines, we see that most of the one-word
# headlines are for the general sections. For accuracy, we can ignore this part at some cases.

two_word_headlines = df.loc[df['headline_word_count'] == 2, 'headline_text']
print(two_word_headlines)

two_word_count = (df['headline_word_count'] == 1).sum()
two_word_count

#There are 21166 headlines containing 2 words.
#Make a plot to display the distribution of length of headlines

print(df.head())

plt.figure()
plt.hist(df["headline_length"], bins=50)
plt.xlabel("Headline Length (characters)")
plt.ylabel("Frequency")
plt.title("Distribution of Headline Lengths")
plt.show()

#Observing the graph, we the length of the headlines reaches its highest number between 40-50, and the number
#suddenly drops after 50. 

#lets plot with headline_wordcount








