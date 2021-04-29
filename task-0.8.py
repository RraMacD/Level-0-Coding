def time_convert(a):
    hour = a // 60
    return hour 
print('Hour is: ',time_convert(int(input())))

def time_convert_minute(b):
    minute = b % 60
    return minute
print('Minute is: ',time_convert(int(input())))
