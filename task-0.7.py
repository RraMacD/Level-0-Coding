#Formula for degree celcius to fahrenheit celcius = (user_fahrenheit -32) * 5/9 
#Formula for fahrenheit to degree celcius fahrenheit = (user_celcius * 9/5) + 32 

def celcius_degree(a):
    celcius = (a -32) * 5/9
    return celcius 
print("Your temperature in celcius degree is: ",celcius_degree(int(input())))

def fahrenheit_temp(b):
    fahrenheit = (b * 9/5) + 32
    return fahrenheit 
print("Your temparature in fahrenheit is: ",fahrenheit_temp(int(input())))


