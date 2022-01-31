# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:12:16 2018

@author: user
"""

# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarına acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir sekilde kaydedbilir.
# 3) pandas bizim isimizi kolaylastiriyor for missing data
# 4) reshape yapip datayi daha etkili bir sekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde cok yardimci
# 7) ayrica herseyden onemlisi hiz pandas hiz acisindan optimize edilmis hizli bir kutuphane

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 

dataFrame1 = pd.DataFrame(dictionary)


head = dataFrame1.head() # first 5
tail = dataFrame1.tail() # last 5
print(head,tail)

# %%
# pandas basic method

print(dataFrame1.columns) # ['NAME', 'AGE', 'MAAS']

print(dataFrame1.info()) # <class 'pandas.core.frame.DataFrame'> RangeIndex: 6 entries, 0 to 5 Data columns (total 3 columns):

print(dataFrame1.dtypes) # NAME    object AGE      int64 MAAS     int64

print(dataFrame1.describe())  # numeric feature = columns (age,maas)

# %% indexing and slicing


print(dataFrame1["AGE"]) # 0  15;    1 16;   2 17;   3 33;   4 45;   5 66 (index-value)
print(dataFrame1.AGE) # same with above

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6] # add new feature, new column

print(dataFrame1.loc[:, "AGE"])  # tumsatirlar age sutunu same with 1 and 2

print(dataFrame1.loc[:3, "AGE"]) # 0-3 row, 3 inklusive, 

print(dataFrame1.loc[:3, "AGE":"NAME"]) # 0-3 row age and until name ink.name

print(dataFrame1.loc[:3, ["AGE","NAME"]]) # 0-3 row age and name 

print(dataFrame1.loc[::-1,:]) # reverse 
#     NAME  AGE  MAAS  yeni feature
# 5  evren   66   220            -6
# 4   ayse   45   110            -5
# 3  hilal   33   350            -4
# 2  kenan   17   240            -3
# 1   veli   16   150            -2
# 0    ali   15   100            -1

print(dataFrame1.loc[:,:"NAME"]) # row until name,  name ink.

print(dataFrame1.loc[:,"NAME"]) # 

print(dataFrame1.iloc[:,2]) # all row 2. colunm(name), . ink. name , same as below

# %% filtering

filtre1 = dataFrame1.MAAS > 200   
print( filtre1) 
# 0    False
# 1    False
# 2     True
# 3     True
# 4    False
# 5     True

filtrelenmis_data = dataFrame1[filtre1]
print(filtrelenmis_data) 
#     NAME  AGE  MAAS  yeni_feature
# 2  kenan   17   240            -3
# 3  hilal   33   350            -4
# 5  evren   66   220            -6
filtre2 = dataFrame1.AGE <20
print(filtre2)
# 0     True
# 1     True
# 2     True
# 3    False
# 4    False
# 5    False

print(dataFrame1[filtre1 & filtre2])    
# NAME  AGE  MAAS  yeni_feature
# 2  kenan   17   240            -3

print(dataFrame1[dataFrame1.AGE > 60])
#     NAME  AGE  MAAS  yeni_feature
# 5  evren   66   220            -6

# %% list comprehension
import numpy as np

ortalama_maas = dataFrame1.MAAS.mean()

# ortalama_maas_np = np.mean(dataFrame1.MAAS)


dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.MAAS]

#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("dusuk")
#    else:
#        print("yukse")
        

dataFrame1.columns


dataFrame1.columns = [ each.lower() for each in dataFrame1.columns] 

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]

# %% drop and concatenating

dataFrame1.drop(["yeni_feature"],axis=1,inplace = True)

# dataFrame1 = dataFrame1.drop(["yeni_feature"],axis=1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# vertical
data_concat = pd.concat([data1,data2],axis=0)


# horizontal

maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)


# %% transforming data

dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.age]

# apply()

def multiply(age):
    return age*2
    
dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)




















