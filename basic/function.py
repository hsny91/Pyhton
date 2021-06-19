#print()
#len() ==> uzunluk icin
#sorted(iterable, /, *, key=None, reverse=False) ==>
# max() ==> find max element inside list
#list


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

