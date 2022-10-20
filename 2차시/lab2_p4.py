#Explain the program
print('This program will convert degrees Celsius to degrees Fahrenheit')

#Get Celsius 
Celsius = float(input('Enter degrees Celsius: '))

#Calculate and output to first decimal place
print(Celsius,'degrees Celsius equals',format((Celsius*1.8)+32,'.1f'),'degrees Fahrenheit')
