import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/hsekeroglu/Desktop/Huesniye/Pyhton/Pyhton/Data_Science_Python/automobileEDA.csv")
print(df.head())


####   LINEAR REGRESSION ##########
# y_head = b0 + b1X  ==> b0 = intercep   b1==> slope or coef

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
x = df[["highway-mpg"]]
y = df[["price"]]
lr.fit(x,y)

y_head = lr.predict(x)
print(y_head)
print(lr.predict(np.array(27).reshape(-1,1)))
# y_head = [[16236.50464347]]   y=13495.0


print("intercept: ", lr.intercept_)  # intercept:  [38423.30585816]
print("coef: ", lr.coef_) # coef:  [[-821.73337832]]

##MES(Mean Square Error)
# Residual = y-yhead  MSE = sum(residual^2) /n ==> our aim is min(Mse)
# Residual Visual
sns.residplot(df['highway-mpg'], df['price'])
plt.show()

#Visualization
sns.regplot(x = "highway-mpg", y = "price", data=df)
plt.ylim(0,)

#######   OR

plt.scatter(x,y ,color ="red")
plt.plot(x, y_head, color = "blue")
plt.xlabel("price")
plt.ylabel("highway-mpg")
plt.show()
