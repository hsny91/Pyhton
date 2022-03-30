#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:32:16 2022

@author: hsekeroglu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("pokemon.csv")
data = data.set_index("#")

data["HP"][1] ## 45
data.HP[1]  ## 45
data.loc[1,["HP"]]  #  45
data[["HP", "Attack"]]


##Slicing

data.loc[1:10,"HP":"Defense"] # 10 and "Defense" are inclusive
data.loc[1:10,-1,"HP":"Defense"] # 10 and "Defense" are inclusive reverse 10 dan 1 e

data.loc[1:10,"Speed":]  # From something to end


## FILTERING DATA FRAMES

boolean = data.HP >200  ## RETURN TRUE OR FALSE
data[boolean]

first_filter = data.HP > 150 
second_filter = data.Speed > 35
data[first_filter & second_filter]
data.HP[data.Speed <15]

#Transforming Data

def div(n):
    return n/2
data.HP.apply(div)

data.HP.apply(lambda n : n/2)

# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()

###INDEX OBJECTS AND LABELED DATA

print(data.index.name) #  #
data.index.name = "index_name"
data.head()


data3 = data.copy()
data3.index = range(100,900,1)
data3.head()


# HIERARCHICAL INDEXING

data1 = data.set_index(["Type 1", "Type 2"])
data1.head(100)


# PIVOTING DATA FRAMES(RESHAPE)

dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df.pivot(index="treatment", columns = "gender", values = "response")


df1 = df.set_index(["treatment","gender"])
df1


# level determines indexes
df1.unstack(level=0)
df1.unstack(level=1)

# change inner and outer level index position
df2 = df1.swaplevel(0,1)
df2


#### MELTING DATA FRAMES


# df.pivot(index="treatment",columns = "gender",values="response")
pd.melt(df,id_vars="treatment",value_vars=["age","response"])


## CATEGORICALS AND GROUPBY
df.groupby("treatment").mean()


df.groupby("treatment")[["age", "response"]].min()
