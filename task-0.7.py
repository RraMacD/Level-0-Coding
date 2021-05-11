#Formula for degree celcius to fahrenheit celcius = (user_fahrenheit -32) * 5/9 
#Formula for fahrenheit to degree celcius fahrenheit = (user_celcius * 9/5) + 32 

def celcius_degree_and_fahrenheit(a,b): 
    celcius = (a -32) * 5/9
    fahrenheit = (b * 9/5) + 32
    return celcius , fahrenheit 
print("Your temperatures are: ",celcius_degree_and_fahrenheit (int(input()),int(input())))


