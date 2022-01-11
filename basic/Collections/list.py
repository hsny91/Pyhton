#List is mutable
a = "is"
b = "nice"
my_list = ["my", "list", a, b]

#Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. 
#The same indexing conventions apply for nesting:
# Sample List

["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas=[hall,kit,liv,bed,bath]

# Print areas
print(areas)

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom", bath]
         ]

# Print out house

print(house)
# Print out the type of house
print(type(house))



###### LIST ELEMENT #####
#my_list[begin:end]



# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1]) #11.25

# Print out last element from areas
print(areas[-1]) #9.50

# Print out the area of the living room
print(areas[4])


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs(bastan itibaren)
downstairs=areas[:6]
# Use slicing to create upstairs(sondan itibaren)
upstairs=areas[6:]

# Print out downstairs and upstairs
print(downstairs) #['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
print(upstairs) #['bedroom', 10.75, 'bathroom', 9.5]

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]

print(x[2][0])  #i expect g
print(x[2][:2])  # I expect ['g','h']

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area

areas[-1]=10.50
# Change "living room" to "chill zone"
areas[4]="chill zone"

print(areas)
####### ADD ELEMENT AND CONCAT ######
# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1=areas+["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2=areas_1+["garage",15.45]

####### EXTEND ELEMENT  ######
# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 2])
print(L) ##['Michael Jackson', 10.2, 'pop', 2]

L.append(['pop', 10])
print(L)  ## ['Michael Jackson', 10.2, 'pop', 2, ['pop', 10]]
 
#####DELETE ELEMENT ##########
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
         
del(areas[0])   #delete hallway
print(areas)

####Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas. After your edit, changes made to areas_copy shouldn't affect areas. Submit the answer to check this.####
# Create list areas


areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas) ##[11.25, 18.0, 20.0, 10.75, 9.50]

#######SPLIT #######
B = 'hard rock'.split()
print(B) ## ['hard', 'rock']

# Split the string by comma

C= 'A,B,C,D'.split(',')
print(C)  ## ['A', 'B', 'C', 'D']

###### COPY AND CLONE LIST #####
A = ["hard rock", 10, 1.2]
B = A
print('A:', A) #('A:', ['hard rock', 10, 1.2])
print('B:', B) #('B:', ['hard rock', 10, 1.2])


## If we change the first element in A to "banana", we get an unexpected side effect.
print('B[0]:', B[0]) ## B[0]: hard rock
A[0] = "banana"
print('B[0]:', B[0]) ## B[0]: banana

## CLONE
# Clone (clone by value) the list A
item_List = ["hard rock", 10, 1.2]
clone_list = item_List[:]
print('clone_list[0]:', clone_list[0]) ## ('clone_list[0]:', 'hard rock')
item_List[0] = "hard rock"
print('clone_list [0]:', clone_list [0]) ## ('clone_list[0]:', 'hard rock')


###LIST METHOD #######
##appende(lement) append object to end
##remove(element) elemeni siler
##reverse(): ters ceviri
##sort(): siralar
##count(element): return numbrt of occurences of value