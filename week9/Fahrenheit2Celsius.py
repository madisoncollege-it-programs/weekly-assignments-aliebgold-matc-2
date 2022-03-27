#!/usr/bin/env python3

# This function will  convert Fahrenheit to Celsius

def fahrenheit():
    inputCelsius = input("Please Enter a Tempeture you would like to Convert to Celsius:")
    inputCelsiusInteger =int(inputCelsius)
    fahrenheit = (inputCelsiusInteger - 32) * 5/9
    print("the tempeture in Celsius is")
    return(fahrenheit)

def main():
    print(fahrenheit())


if __name__ == "__main__":
    main()
