#print()
#len() ==> uzunluk icin

# max() ==> find max element inside list


####### STRING METHODS ############

# str.upper()=> it is used for capitalize all letters
# str.count('letter') => it is used to count the number of letter/letters inside str
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up=place.upper()

# Print out place and place_up
print(place_up)
print(place)

# Print out the number of o's in place
print(place.count('o'))

####### LIST METHODS ########

# list.index(listElement) ==> it is used to find the index of element
# list.count(listElement) ==> it is used to count the number of list element
# list.append(list elemnet) ==> add lement into the list
# list.reverse() ==> reverse list
# sorted(iterable, /, *, key=None, reverse=False) ==>

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

### SORT ########

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full=first+second

# Sort full in descending order: full_sorted
full_sorted=sorted(full) ### kucukten büyüge
full_sorted2=sorted(full , reverse=True) ##buyukten kuucuge

# Print out full_sorted
print(full_sorted)
print(full_sorted2)