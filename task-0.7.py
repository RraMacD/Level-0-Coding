#Formula for degree celcius to fahrenheit celcius = (user_fahrenheit -32) * 5/9 
#Formula for fahrenheit to degree celcius fahrenheit = (user_celcius * 9/5) + 32 

user_number = float(input('Enter a number in celcius degree: '))
celciusDegree_to_fahrenheit = (user_number - 32)* 5/9
print('Your temparature in Fahrenheit is: {0}' .format(celciusDegree_to_fahrenheit))

user_number2 = float(input('Enter a number in fahrenheit: '))
fahrenheit_to_celciusDegree = (user_number2 * 9/5) + 32
print('Your temparature in celcius degrees is: {0}' .format(fahrenheit_to_celciusDegree))



