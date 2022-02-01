#!/usr/bin/env python3


varRed='Red'
varGreen='Green'
varBlue='Blue'
varName='Aaron'
varLoot='10.4516295'


print ('\nQuestion: Hello Aaron') 
print (f'Answer: Hello {varName}\n')

print ('Question: Red-blue-Green')
print(f'Answer: {varRed}-{varGreen}-{varBlue}\n')

print('Question: Is this Green or Blue')
print(f'Answer: Is this {varGreen} or {varBlue}\n')

print('Question: My name is Aaron')
print(f'Answer: My name is {varName.upper()}\n')

print('Question: ++Red++')
print(f'Answer: {varRed:+^7}\n')

print('Question: Green==')
print(f'Answer: {varGreen:=<7}\n')

print('Question: *****Blue')
print(f"Answer:{varBlue:*>9}\n")

print('Question: BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue')
print(f'Answer: {varBlue * 10}\n')

print(f'Question: {varLoot}') 
print(f'Answer: {varLoot}\n')

print('Question: 10.4')
print(f'Answer: {varLoot [0:4]}\n')

print('Question: I have $10.45')
print(f'Answer: I have ${varLoot [0:5]}\n')

print('Question: $$$Red$$$ - $$Green$$ - $$$Blue$$$')
print(f'Answer: {varRed:$^9} - {varGreen:$^9} - {varBlue:$^10}\n')

print(f'Question: deR\tGreen\teulB')
print(f'Answer:\t{varRed [::-1]}\t{varGreen}\t{varBlue [::-1]}\n')

print('Question: First Color Red    Second Color Green  Third color Blue') 
print(f'Answer: FirstColor {varRed}\tSecondColor{varGreen}\tThirdColor{varBlue}\n')
