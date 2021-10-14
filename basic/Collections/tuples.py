#TUPPLE IS IMMUTABLE
#WE CAN NOT CHANGE THEM

# Create your first tuple
myTuple = (1,2,3,4,5)
tuple1= ('disco',10, 1.2) 

print(type(myTuple)) #tuple

# Print the variable on each index
print(tuple1[0]) #disco
print(tuple1[1]) #10
print(tuple1[2]) #1.2

# Use negative index to get the value of the last element
print(tuple1[-1]) #1.2

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2) #('disco', 10, 1.2, 'hard rock', 10)

# Slice from index 0 to index 2
print(tuple2[0:3]) # ('disco', 10, 1.2)

# Slice from index 3 to index 4
print(tuple2[3:5]) # ('hard rock', 10)

# Get the length of tuple
print(len(tuple2)) # 5

#### SORTING #####

# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
print(RatingsSorted) # [0, 2, 5, 6, 6, 8, 9, 9, 10]

########NESTED TUPLE #####

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 2 of Tuple: ", NestedT[2]) ##Element 2 of Tuple:  ('pop', 'rock')
print("Element 2, 0 of Tuple: ",   NestedT[2][0]) ## ('Element 2, 0 of Tuple: ', 'pop')

# Print the first element in the second nested tuples
print(NestedT[2][1][0]) ## r
print(NestedT[4][1][0]) ## 1

######INDEX ######
genres_tuple=('pop',
 'rock',
 'soul',
 'hard rock',
 'soft rock',
 'R&B',
 'progressive rock',
 'disco')
X= genres_tuple.index("disco") #
print(X) ## 7