#Formula for degree celcius to fahrenheit celcius = (user_fahrenheit -32) * 5/9 
#Formula for fahrenheit to degree celcius fahrenheit = (user_celcius * 9/5) + 32 

def celciusDegree(x):
  celciusDegree_to_fahrenheit = (x - 32)* 5/9
  print('Your temparature in Fahrenheit is:',celciusDegree_to_fahrenheit)

celciusDegree(37)

def  fahrenheit(x): 
  fahrenheit_to_celciusDegree  =  (x  *  9/5)  +  32 
  print('Your temparature  in  Calcius Degree  is:',fahrenheit_to_celciusDegree) 

fahrenheit(17)
