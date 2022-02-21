#https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("/Users/hsekeroglu/Desktop/Huesniye/Pyhton/Data_Science_Python/pokemon.csv")
print(df.corr())

# corelation map
#correlation map
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

print(df.columns)

# Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
#    'Sp. Def', 'Speed', 'Generation', 'Legendary'],
#    dtype='object')


# MATHPLOTLIB
## LINE PLOT
df.Speed.plot(kind="line",color="g",label="Speeed",linewidth=1,alpha=0.5, grid="True",linestyle=":")
df.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = "True",linestyle = '-.')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend(loc='upper right')     # legend = puts label into plot
plt.title("Line Plot")
plt.show()

##SCATTER PLOT
df.plot(kind="scatter", x= "Attack", y="Defense", alpha=0.5,color="red")
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack- Defence Scatter Plot")
plt.show()

##HISTOGRAM
df.Speed.plot(kind="hist", bins=50, figsize=(15,15))
plt.show()

#DICTIONARY

dictionary = {'spain' : 'madrid','usa' : 'vegas'}
print(dictionary.keys()) # dict_keys(['spain', 'usa'])
print(dictionary.values()) # dict_values(['madrid', 'vegas'])

dictionary['spain'] = "barcelona"    # update existing entry
print(dictionary)
dictionary['france'] = "paris"       # Add new entry
print(dictionary)
del dictionary['spain']              # remove entry with key 'spain'
print(dictionary)                       # {'usa': 'vegas', 'france': 'paris'}
print('france' in dictionary)        # check include or not True
dictionary.clear()                   # remove all entries in dict
print(dictionary)

#del dictionary         # delete entire dictionary     
print(dictionary)       # it gives error because dictionary is deleted


#PANDAS

series = df['Defense']        # data['Defense'] = series
print(type(series))
print(series)
data_frame = df[['Defense']]  # data[['Defense']] = data frame
print(type(data_frame))

# Comparison operator
print(3 > 2)
print(3!=2)
# Boolean operators
print(True and False)
print(True or False)

x = df['Defense']>200     # There are only 3 pokemons who have higher defense value than 200
print(x) # it writes true and false
print(df[x])


df[np.logical_and(df['Defense']>200, df['Attack']>100 )]
# df[(df['Defense']>200) & (df['Attack']>100)]

#LOOP DATA STRUCTURE
# 
i=0
while i !=5:
    print(i)
    i+=1

# 0,1,2,3,4

# Stay in loop if condition( i is not equal 5) is true
lis = [1,2,3,4,5]
for i in lis:
    print('i is: ',i)
print('')

# Enumerate index and value of list
# index : value = 0:1, 1:2, 2:3, 3:4, 4:5
for index, value in enumerate(lis):
    print(index," : ",value)
print('')  

# For dictionaries
# We can use for loop to achive key and value of dictionary. We learnt key and value at dictionary part.
dictionary = {'spain':'madrid','france':'paris'}
for key,value in dictionary.items():
    print(key," : ",value)
print('')
#spain  :  madrid
#france  :  paris

# For pandas we can achieve index and value
for index,value in df[['Attack']][0:1].iterrows():
    print(index," : ",value)

    
# 0  :  Attack    49
# Name: 0, dtype: int64


