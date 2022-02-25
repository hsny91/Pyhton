# single column = series
# NaN = not a number
# dataframe.values = numpy

import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("/Users/hsekeroglu/Desktop/Huesniye/Pyhton/Pyhton/Data_Science_Python/basic/pokemon.csv")

# data frames from dictionary
country = ["Spain","France"] ##list
population = ["11","12"] ##list
list_label = ["country","population"] 
list_col = [country,population]
zipped = list(zip(list_label,list_col))  # 
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
#print(df)

#   country population
# 0   Spain         11
# 1  France         12

df["capital"] = ["madrid","paris"]
#print(df)

#  country population capital
# 0   Spain         11  madrid
# 1  France         12   paris

# Plotting all data 
data1 = data.loc[:,["Attack","Defense","Speed"]]
#data1.plot()

data1.plot(subplots = True)
#plt.show()

# scatter plot  
data1.plot(kind = "scatter",x="Attack",y = "Defense")
#plt.show()


# hist plot  
#data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)

#INDEXING PANDAS TIME SERIES

time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object)) # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>


data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object

data2= data2.set_index("date")
print(data2)