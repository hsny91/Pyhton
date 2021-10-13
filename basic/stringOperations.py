name = 'Husniye Sekeroglu'
print(name[0]) # 'H'
print(name[-1]) # 'u'
print(name[0:4]) # 'Husn'
print(name[::2]) # 'HsieSkrgu Get every second element.
print(name[:2]) # Hu
print(name[0:7:2]) # Hsie Get every second element in the range from index 0 to index 7

print(len(name)) #17

# Print the string for 3 times

print(3 * "Michael Jackson")

##concated '+'
name = name + "is the best"
print(name)
print("she\n is the best")  ##new line
print("she\t is the best")  ##tab


### Methods #####

## upper()
A= "hello guys"
B = A.upper()
print(B)

## replace()
C = A.replace('hello','hi')
print(C)

## find('xxx') first index number
D = A.find('guys')
print(D)  ## 6 