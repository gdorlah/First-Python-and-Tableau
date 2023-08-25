# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:56:30 2023

@author: gdorlah
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reading excel or xlsx file
data = pd.read_excel('articles.xlsx')

#summary of data
data.describe()

#counting the # of articles per source
#using group by: df.groupby(['column to group'])['column to count'].count()
data.groupby(['source_id'])['article_id'].count()

data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping column from dataframe
data = data.drop('engagement_comment_plugin_count' , axis=1)


# Functions in python
def thisFunction(): 
    print('This is my first Function')
thisFunction()

# this is a function with variables
def aboutMe(name, surname, location):
    print('This is '+name+' my surname is '+surname+ ' I am from '+location)
    return name, surname, location
a = aboutMe('Godsway', 'Dorlah', 'Arizona')

# using forloops in function 
def favfood(food):
    for x in food:
        print('top food is '+x)

fastfood = ['akple', 'banku', 'waakye', 'jollof']
favfood(fastfood)

# we can use function 'def' to identify key wrods in article tittle and create a seperate column for those key words: using for loop as well

# creating a key word flag
# keyword = 'crash'
# length = len(data)
# keyword_flag = []
# for x in range(0, 10):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)

# creating the fuction 
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
keywordflag = keywordflag('murder')

#creating a new column
data['keyword_flag'] = pd.Series(keywordflag)


#Sentiment analysis in python: this could be applied to news articles: the aime is to gage the artitude of the speaker
# We use VADER as it has already been trained on social media post
sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# we have to use for loop to loop through every title to select neg, pos and neu 
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)


data['neg_sentiment'] = title_neg_sentiment
data['pos_sentiment'] = title_pos_sentiment
data['neu_sentiment'] = title_neu_sentiment



# data to xlsx file
data.to_excel('blogme1_cleaned.xlsx', sheet_name='blogmedata', index = False)
   



    










