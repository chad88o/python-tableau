# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:39:52 2024

@author: chaz-
"""

import pandas as pd

# file name = pd.read_csv('file.csv')<... format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

#working with caluclations

#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau 

ProfitPerItem = 21.11- 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem 
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calucation

#CostPerTransaction = CosetPerItem = NumberofItemsPurchases
# variable = dataframe{'column_name'}

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data ['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding a new colum to dataframe

data ['CostPerTransaction'] = CostPerTransaction

data ['CostPerTransaction'] = data ['CostPerItem'] * data ['NumberOfItemsPurchased']



#Sales per Transaction

data ['SalesPerTransaction'] = data['SellingPricePerItem'] * data ['NumberOfItemsPurchased']

#Profit Caluculation = Sales = Cost

data ['ProfitPerTransaction'] = data ['SalesPerTransaction'] - data ['CostPerTransaction']

#Markup = Sales - Cost/Cost

data ['Markup'] =  data ['SalesPerTransaction'] - data ['CostPerTransaction'] /data ['CostPerTransaction']

data ['Markup'] =  data ['ProfitPerTransaction'] /data ['CostPerTransaction']

#Rounding marking

roundmarkup = round (data ['Markup'] , 2)

data ['Markup'] = round (data ['Markup'] , 2)

#combining data fields

my_name ='Charles' + 'Steven'
my_date ='Day' + '-' +'Month'+'-'+'Year'

my_date = data ['Day'] +'-'

#checking columns data type
print(data ['Day']. dtype)

#change columns type

day = data ['Day']. astype(str)
year = data ['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-' +data ['Month'] + '-' +year

data ['data'] = my_date

#using iloc tp view specfifc columns/rows

data.iloc [0] #views the row with index -= 0
data.iloc [0:3]
data.iloc [-5:] #last 5 rows

data.head [5] #brings in first 5 rows

data.iloc [:,2]

#using split to split the client keywords field
#new_var = columb.str.split ('sep' , expand = True)

split_col = data ['ClientKeywords'].str.split(',', expand = True)


#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' ,'')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')


#using the lower function to chnge item to lowercase

data['ItemDescription'] = data ['ItemDescription'] .str.lower()

#how to merge files

#bringing in a new dataset

seasons = pd.read_csv ('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')


#dropping columns

# df = df.drop ('columnname' , axis = 1)

data = data.drop ('ClientKeywords', axis = 1)

data = data.drop ('Day' , axis = 1)

data = data.drop (['Year', 'Month'], axis = 1)


#Export into CSV

data.to_csv('ValueInc_Cleaned.csv' , index = False)



















