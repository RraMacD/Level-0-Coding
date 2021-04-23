user_celcius = int(input('Enter temperature you want to convert into fahrenheit: '))
user_fahrenheit = int(input('Enter temparature you want to convert into celcius: '))

fahrenheit = (user_celcius * 9/5) + 32 #Formula for degree celcius to fahrenheit
celcius = (user_fahrenheit -32) * 5/9 #Formula for fahrenheit to degree celcius

print("The converted celcius to fahrenheit is", fahrenheit)
print("The comverted fahrenheit to celcius is ", celcius)
