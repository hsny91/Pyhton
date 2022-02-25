#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




data= pd.read_csv("/Users/hsekeroglu/Desktop/Huesniye/Pyhton/Pyhton/Data_Science_Python/data_cleaning/imports-85.data",header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

data.columns = headers
data.describe()

## Missing Data

# Convert "?" to NaN
data = data.replace('?', np.NaN)
print(data.head())

#calculate missing data
missing_data = data.isnull()
missing_data.head(5)

## calculate sum of the True and False (True =NAN)
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

print(data['price'].value_counts(dropna =False)) ##4 tane Nan var
print(data['normalized-losses'].value_counts(dropna =False)) # 41 Nan var
print(data['stroke'].value_counts(dropna =False)) # 4 Nan var
print(data['horsepower'].value_counts(dropna =False)) # 2 Nan var
print(data['peak-rpm'].value_counts(dropna =False)) # 2 Nan var
print(data['num-of-doors'].value_counts(dropna =False)) # 2 NaN



###DEAL WITH MISSING DATA

#How to deal with missing data?
# 1.Drop data
#   a. Drop the whole row
#   b. Drop the whole column
# 2.Replace data
#   a. Replace it by mean
#   b. Replace it by frequency
#   c. Replace it based on other functions

# 1.b Drop the whole row:
data = data.dropna(subset = ['price'], axis=0) ## NaN olanlari drop ettik
data.reset_index(drop=True, inplace=True)
    
# 2.a Replace by mean
    #normalized-losses": 41 missing data, replace them with mean
avg_norm_loss = data["normalized-losses"].astype("float").mean(axis=0) ##122
print("Average of normalized-losses:", avg_norm_loss)
# Replace "NaN" with mean value in "normalized-losses" column
data["normalized-losses"].replace(np.nan, avg_norm_loss, inplace = True)

#"stroke": 4 missing data, replace them with mean
avg_norm_strk = data["stroke"].astype("float").mean(axis=0)
print("Average of stroke:",avg_norm_strk)
data['stroke'].replace(np.nan,avg_norm_strk, inplace =True )


#"bore": 4 missing data, replace them with mean
avg_norm_bore = data["bore"].astype("float").mean(axis=0)
print("Average of bore:",avg_norm_bore)
data['bore'].replace(np.nan,avg_norm_bore, inplace =True )


#"horsepower": 2 missing data, replace them with mean
avg_horsepower = data['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)
data['horsepower'].replace(np.nan, avg_horsepower, inplace=True)


#"peak-rpm": 2 missing data, replace them with mean
avg_peakrpm=data['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
data['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)


#2.b Replace by frequency:
# num-of-doors": 2 missing data, replace them with "four"
data['num-of-doors'].value_counts() # four    114 two      89
data['num-of-doors'].value_counts().idxmax() # four
data['num-of-doors'].replace(np.nan, "four", inplace = True)



###### Data Formating
print(data.dtypes)

data[["bore", "stroke"]] = data[["bore", "stroke"]].astype("float")
data[["normalized-losses"]] = data[["normalized-losses"]].astype("int")
data[["price"]] = data[["price"]].astype("float")
data[["peak-rpm"]] = data[["peak-rpm"]].astype("float")

print(data.dtypes)


## Data Standardization
# We will need to apply data transformation to transform mpg into L/100km.
# L/100km = 235 / mpg
data['city-L/100km'] = 235/data["city-mpg"]


## NORMALIZATION
# replace (original value) by (original value)/(maximum value)
data['length'] = data['length']/data['length'].max()
data['width'] = data['width']/data['width'].max()

