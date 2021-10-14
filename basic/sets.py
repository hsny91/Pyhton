# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1) # {'R&B', 'disco', 'hard rock', 'pop', 'rock', 'soul'}

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)

#####ADD ELEMENT TO SET #######
# If we add the same element twice, nothing will happen as there can be no duplicates in a set:

set1.add("NSYNC")
print(set1)

# Remove the element from set
set1.remove("NSYNC")
print(set1)

# Verify if the element is in the set
print("AC/DC" in set1)

###### Sets Logic Operations ######
# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Find the intersections
intersection = album_set1 & album_set2
print(intersection) # {'AC/DC', 'Back in Black'}

# Find the difference in set1 but not set2
print(album_set1.difference(album_set2)) # {'Thriller'}
print(album_set2.difference(album_set1)) # {'The Dark Side of the Moon'}