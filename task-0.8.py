def time_convert(a): 
    hour = a // 60
    minute = a % 60
    return hour, minute
print('Hour and minute of this number is: ',time_convert(int(input()))) 



