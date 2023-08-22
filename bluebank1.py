# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:16:22 2023

@author: gdorlah
"""

import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data/file
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data?file
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transforming data into Dataframe 
loandata = pd.DataFrame(data)

#Use unique function to show unique values in a specific column of a dataframe
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe data for specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using the ESP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#working with IF statements
a = 40
b = 500
if b > a:
    print('b is greater than a')
    
    
a = 40
b = 500
c = 1000
if b > a and b < c:
    print('b is greater than a but less than c')


#what if a  condition is not met

a = 40
b = 500
c = 20
if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('Condition not met')


a = 40
b = 500
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No condition met')


#using or
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a or less than c')
else:
    print('No condition met')


a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No condition met')


#working on fico score

#fico >= 300 and < 400: 'Very Poor'
#fico >= 400 and ficoscore < 600: 'Poor'
#fico >= 601 and ficoscore < 660: 'Fair'
#fico >= 660 and ficoscore < 780: 'Good'
#fico >=780: 'Excellent'

fico = 700
if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico <600:
    ficocat ='Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico <780:
    ficocat = 'Good'
elif fico >=780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)


# Applying if statements to every line in data frame using For loops

fruits = ['apple', 'pear', 'banana', 'cherry']
for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)


for x in range(0,4):
    y = fruits[x]+' for sale'
    print(y)


# applying for loops to loandata
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat


# Could do this instead of if statememts
# df.loc as conditional statement
# df.loc[df[columnname]] condition, newcolumname = 'value if condition is met'
# for interest rate, a new column is wanted. rate>0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'


#plotting in python with grouping

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'yellow', width = 0.5)
plt.show()

purplot = loandata.groupby(['purpose']).size()
purplot.plot.bar(color = 'orange')
plt.show()

#scatter plot need x and y values
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'maroon')
plt.show()



# Finally!!
#writing to csv
loandata.to_csv('loandata_cleaned1.csv', index = True)















