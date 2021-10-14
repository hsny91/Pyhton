#### FOR AND WHILE LOOPS #####

# Range is helpful to think of the range object as an ordered list.
print(range(3)) # [0, 1, 2]

### FOR lOOP #######

# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i]) # 1982 1980 1973 

for i in range(8):
    print(i) # 0 1 2 3 4 5 6 7  

# In Python we can directly access the elements in the list as follows:
for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)  # 0 red 1 yellow 2 green 3 purple 4 blue

### WHILE lOOP #######

# The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.