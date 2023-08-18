# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:05:39 2023

@author: gdorlah
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <------- format of read csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv' , sep=';')

data = data.dropna(how='any')


# get summary of data
data.info()

# playing around with variables
var = ('apple', 'pear', 'banana')


#Working with calculations
#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = ProfitPerItem * NumberofItemsPurchased
CostPerTransaction = CostPerItem * NumberofItemsPurchased
SalesPerTransaction = SellingPricePerItem * NumberofItemsPurchased

#applying calc to an entire column of data
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new columnto dataframe
data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = SalesPerTransaction
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/cost
data['MarkUp'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']


#formating and using functions
roundmarkup = round(data['MarkUp'], 2)
data['MarkUp'] = roundmarkup

#Changing datatype

data['Day'] = data['Day'].astype(int)
data['Year'] = data['Year'].astype(int)


#combining date fields or columns
my_date = 'Month'+'-'+'Day'+'-'+'Year'

#changing column data type
day = data['Day'].astype(str)
print(day.dtype)

month = data['Month'].astype(str)
print(month.dtype)

year = data['Year']. astype(str)
print(month.dtype)

my_date = month+'-'+day+'-'+year

data['Date'] = my_date


#using iloc to view specific columns or rows
data.iloc[0] #view row with index 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows
data.iloc[:,2]

#using split function 
#new_var = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#Creating new columns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')


#using the lower function 
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing new data file
new_data = pd.read_csv('Value_inc_seasons.csv' , sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on ='key')

data = pd.merge(data, new_data, on = 'Month')

#droping some columns
#df = df.drop('column', axis = 1)
data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Year' , 'Month'] , axis = 1)


#exporting data into csv
data.to_csv('Value_inc_Cleaned_New.csv' , index = False)





















