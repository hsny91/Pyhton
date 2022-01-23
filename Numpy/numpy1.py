import numpy as np

array= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*15 matris olusturduk
print(array) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(array.shape) # (15,)
a=array.reshape(3,5)
print(a) 
###[[ 1  2  3  4  5]
#[ 6  7  8  9 10]
#[11 12 13 14 15]]

print(a.shape) # (3,5)

print("dimension: " , a.ndim) #dimension:2
print("data type: ", a.dtype.name) # data type:  int64
print("size: ", a.size) #size:  15

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,13]])
print(array1) #shape(3,4)
##[[ 1  2  3  4]
##[ 5  6  7  8]
## [ 9 10 11 13]]
zeros=np.zeros((3,4))
print( zeros)# allocation
#[[0. 0. 0. 0.]
#0. 0. 0. 0.]
#[0. 0. 0. 0.]]
zeros[0,0]=5
print(zeros)
#[[5. 0. 0. 0.]
#[0. 0. 0. 0.]
#[0. 0. 0. 0.]]

np.ones((3,4)) # 1 lerden olusan matris
np.empty((2,3)) # bosluklarsan olusur

newArray= np.arange(10,50,5) # 10 ile 50 arasi 5 ler 5 er artan dizi 
print(newArray) # [10 15 20 25 30 35 40 45]

array2=np.linspace(10,50,20) # 10 ile 50 arasinda 20 tane sayi
print(array2)   # [10.  12.10526316 14.21052632 16.31578947 18.42105263 20.52631579
                #22.63157895 24.73684211 26.84210526 28.94736842 31.05263158 33.15789474
                #35.26315789 37.36842105 39.47368421 41.57894737 43.68421053 45.78947368
                #47.89473684 50. ]

#BASIC OPERATION
firstArray = np.array([1,2,3])
secondArray = np.array([4,5,6])
print(firstArray+secondArray) # [5 7 9]
print(firstArray-secondArray) # [-3 -3 -3]
print(firstArray**2) # [1 4 9]
print(np.sin(firstArray)) # sinus [0.84147098 0.90929743 0.14112001]
print(firstArray>2) # [False False  True]
newArray = np.array([[1,2,3],[4,5,6]])
newArray2 = np.array([[1,2,3],[4,5,6]])
print(newArray*newArray2) #[[ 1  4  9][16 25 36]]

#matris carpimi
print(newArray.dot(newArray2.T)) # [[14 32][32 77]]
randomArray = np.random.random((5,5))
print(randomArray)   #[[0.75947921 0.5529714  0.8483896  0.67493675 0.58607664]
                    #[0.58022546 0.6452559  0.64366787 0.86925379 0.79480236]
                    #[0.1320662  0.61099114 0.29713948 0.11146005 0.21793815]
                    #[0.79126145 0.28453887 0.18648395 0.03383147 0.84490282]
                    #[0.09606489 0.20861273 0.1323174  0.16048047 0.84820322]]

print(randomArray.sum()) # 15.441782913907897
print(randomArray.max()) #0.9852612031571697
print(randomArray.min()) #0.03342914573554878
print(randomArray.sum(axis=0))# columnlari topla [2.15717908 3.6973428  2.06991963 3.49705409 1.93710996]
print(randomArray.sum(axis=1)) # rowlari topla [3.10531554 3.01488642 3.16117818 2.93265648 2.62180621]
print(np.square(randomArray)) #randomArray**2


#INDEXING SLICING
my_array = np.array([1,2,3,4,5,6,7])
print(my_array[3]) # 4
print(my_array[0:4]) # 1,2,3,4
reverse_array= my_array[::-1]
print(reverse_array) #  [7 6 5 4 3 2 1]
my_array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(my_array1[1,1]) # 7
print(my_array1[1,1:4]) # [7 8 9]
print(my_array1[:,-1]) # [ 5 10] son sutun

##SHAPE MANUPULATION
shape_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(shape_array)
#[[1 2 3]
#[4 5 6]
#[7 8 9]]
shape_array1 = shape_array.ravel()
print(shape_array1) # [1 2 3 4 5 6 7 8 9]

shape_array2= shape_array1.reshape(3,3) # eski haline geri dondu
arrayT= shape_array2.T
print(arrayT)
#[[1 4 7]
# [2 5 8]
# [3 6 9]]