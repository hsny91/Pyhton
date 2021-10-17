import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

# Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, "r")

# Print the path of file
print(file1.name) # 'Example1.txt'

# Print the mode of file, either 'r' or 'w'
print(file1.mode) # 'r'

# Read the file
FileContent = file1.read()
print(FileContent) # 'This is line 1 \nThis is line 2\nThis is line 3'

# Print the file with '\n' as a new line
print(FileContent) # This is line 1 This is line 2 This is line 3

# Type of file content
type(FileContent) # str

# Close file after finish
file1.close()

### Using the with statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object.

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
print(file1.closed) # True

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4)) # This

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline()) # first line: This is line 1 

# Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Iteration 0 :  This is line 1 

#Iteration 1 :  This is line 2

# Iteration 2 :  This is line 3

# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
FileasList[0] # 'This is line 1 \n'

# Print the third line
FileasList[2] # 'This is line 3'