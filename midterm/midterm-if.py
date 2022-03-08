#!/usr/bin/env python3

print("\n")
print("Name:Aaron Liebgold")
print("\n")

hFile=open("Midterm-if.txt","r")
strFiletxt=hFile.read()
print(strFiletxt)

print("\n")
print(f"The length of the file is {len(strFiletxt)} bytes long")
print("\n")

#list of key words to find

counter = 0
with open ("Midterm-if.txt","r") as hFile:
    for line in hFile:
        if "gmeach18@ed.gov" in line:
            print(line)

        if "248.253.63.149" in line:
            print(line)
        if "whiteland" in line:
            print(line)
        if "80.222.19.190" in line:
            print(line)
        if "Kayley" in line:
            print(line)
        if "dcassyqw@microsoft.com" in line:
            print(line)
            print(f'{counter}) {line}')
        counter += 1
print('\n')
Total = "2425"
print(f'The total when adding lines together is: {Total}')
print('\n')
