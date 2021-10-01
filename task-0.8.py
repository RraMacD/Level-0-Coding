num = int(input('Enter any number: ')) 
hour = round(num / 60) 
minute = num % 60
time1 = "hours"
time2 = "minutes in this number"
print ('There are: {0}'.format(hour) + " " + time1, '{0}'.format(minute) + " " + time2)
