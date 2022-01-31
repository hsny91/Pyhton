import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/hsekeroglu/Desktop/Huesniye/Pyhton/Pyhton/Visualization_Matplotlib/Scatter/iris.csv")

print(df.columns)

# Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species'],

print(df.Species.unique())
# ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

setosa = df[df.Species== "Iris-setosa"] # get the ones with type "Iris-setosa
versicolor= df[df.Species== "Iris-versicolor"] # get the ones with type Iris-versic
virginica= df[df.Species== "Iris-virginica"] # get the ones with type Iris-virginica

df1= df.drop(["Id"], axis=1)


plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color ="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color ="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color ="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()

