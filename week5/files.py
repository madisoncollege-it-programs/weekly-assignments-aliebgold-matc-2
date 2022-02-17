#!/usr/bin/env python3

# To Do step 1

# opening /etc/passwd with read only access and saving file to "str" data type.
# using the len() function to specify size function counts
# print a statement to describe when you would use the read function over other read functions. 


hFile=open("/etc/passwd","r")
print('\n')
strfiletxt=hFile.read()
#print(strfiletxt)
print(f"The length of the file is {len(strfiletxt)} bytes long")
print(f"\nWhen using this read function it will tell you the number of\ncharacters that are in the file")
print("\n")
print(f"You would use this function to see  all of the contents of the file") 

# To Do Step (2)
# opening /etc/passwd with read access only and saving file to a "list" data type
# add a print statement to the script to indicate what length function counts 
# add a print statement to describe when you would use this read function over other read functions 


print("\n")
hFile=open("/etc/passwd","r")
listfiletxt=hFile.readlines()
#print(listfiletxt)
print("\n")
print(f"The length of the file is {len(listfiletxt)} bytes long")
print("\n")
print(f"You would use this read function to count how many lines are in the file. I assume it counts all of the new line characters in the file")
print("\n")
print(f"You would use the readline function when you want to know how many lines are in a paticular file. This function only counts how many lines not how many total characters.")

# open /etc/passwd file using read only access and save the contents one line at a time to a variable
# add code that will  calculate total length of the file
# add a print state ment to describe when you would use this technique 


print("\n")

hFile=open("/etc/passwd","r")

for line in hFile:
    print(line)

OneLine=hFile.read()
print(f"The length of this file is NOT {len(OneLine)} bytes long\nIt is 2744 bytes long\nYou can double check this by running the command 'sudo cat /etc/passwd | wc -c'")
print("\n")
print("You would use the read function when you want to be\nable to read the output carefully\nThis provides more white space to make it\neasier on the eyes\n")
