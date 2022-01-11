#### FOR AND WHILE LOOPS #####

# Range is helpful to think of the range object as an ordered list.
print(range(3)) # [0, 1, 2]

### FOR lOOP #######

# For loop example
dates = [1982,1980,1973]
N = len(dates)
print(sum(dates)) ## 5935

for i in range(N):
    print(dates[i]) # 1982 1980 1973 

for i in range(8):
    print(i) # 0 1 2 3 4 5 6 7  
for i in range(1,11):
        print(i) # 1 2 3 4 5 6 7 9 10 

# In Python we can directly access the elements in the list as follows:
for year in dates:
    print(year)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)  # 0 red 1 yellow 2 green 3 purple 4 blue

for each in "ankara ist".split():
    print(each) # ankara ist

### WHILE lOOP #######

# The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.

# While Loop Example

dates = [1982, 1980, 1973, 2000]
i = 0
while(dates[i]!=1973):
    print(dates[i])
    i = i+1


### EXAMPLE ######
# find min
liste=[11,2,7,3,4,5,6,4,23,67]
min_number=liste[0]
for number in liste:
    if(number<min_number):
        min_number=number
print(min_number)
    