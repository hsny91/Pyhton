import pandas as pd
import numpy as np

data= pd.read_csv("pokemon.csv")
data.head()
data.tail()
print(data.columns)
print(data.shape) # (800,12)
print(data.info())

###  EXPLORATORY DATA ANALYSIS  #####

# 1. value_counts(): Frequency counts

print(data['Type 1'].value_counts(dropna =False))  ## 112 tane su pokemonu var gibi

# 2. Outlier: the value that is considerably higher or lower from rest of the data
# Outlier are smaller than Q1 - 1.5(Q3-Q1) and bigger than Q3 + 1.5(Q3-Q1). (Q3-Q1) = IQR

# 1,4,5,6,8,9,11,12,13,14,15,16,17
# The median is the number that is in middle of the sequence. In this case it would be 11.
# The lower quartile is the median in between the smallest number and the median i.e. in between 1 and 11, which is 6
# The upper quartile, you find the median between the median and the largest number i.e. between 11 and 17, which will be 14 according to the question above.
# Q1=lower quartile Q3=upper quartile Q2= quantiler

print(data.describe())

######### VISUAL EXPLORATORY DATA ANALYSIS  ##########

# Box plots: visualize basic statistics like outliers, min/max or quantiles

data.boxplot(column='Attack',by = 'Legendary')


####    TIDY DATA AND PIVOTING DATA   #######

# We tidy data with melt()
data_new = data.head() 
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
print(melted)

#Reverse of melting.

melted.pivot(index = 'Name', columns = 'variable',values='value')
print(melted)

######## CONCATENATING DATA AND DATA TYPES ###########

##vertical concat
data1 = data.head()
data2= data.tail()
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True)

print(conc_data_row)

#horizantal concat
data3 = data['Attack'].head()
data4 = data['Defense'].head()
conc_data_col = pd.concat([data3,data4],axis =1) # axis = 1 : adds dataframes in column
print(conc_data_col)

#  There are 5 basic data types: object(string),boolean, integer, float and categorical.There are 5 basic data types: object(string),boolean, integer, float and categorical.

# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')