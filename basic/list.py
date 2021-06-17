a = "is"
b = "nice"
my_list = ["my", "list", a, b]

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