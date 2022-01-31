import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/hsekeroglu/Desktop/Huesniye/Pyhton/Pyhton/Visualization_Matplotlib/Subplot/iris.csv")

print(df.columns)

# Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species'],

print(df.Species.unique())
# ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

setosa = df[df.Species== "Iris-setosa"] # get the ones with type "Iris-setosa
versicolor= df[df.Species== "Iris-versicolor"] # get the ones with type Iris-versic
virginica= df[df.Species== "Iris-virginica"] # get the ones with type Iris-virginica

df1= df.drop(["Id"], axis=1)

# her feature göre line cizim yapar.
df1.plot(grid="true",alpha=0.9,subplots="True")  # alpa=0.1 opacity
plt.show()
