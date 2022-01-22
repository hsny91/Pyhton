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