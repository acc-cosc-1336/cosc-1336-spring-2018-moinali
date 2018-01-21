#seconds since midnight to return hours, minutes, and seconds
#1 min = 60
#1 hour = 60 * 60 = 3600

def get_hours_since_midnight(seconds):
    return (seconds//3600)

def get_minutes(seconds):
    return (seconds - (get_hours_since_midnight(seconds)*3600))//60

def get_seconds(seconds):
    return seconds - ((get_hours_since_midnight(seconds)*3600) + (get_minutes(seconds)*60))

def time():
    seconds= int(input('enter amount of seconds: '))
    print('Total time eclipse since midnight in hh:mm:ss is ', get_hours_since_midnight(seconds), ':', get_minutes(seconds), ':',get_seconds(seconds) )
    
    
time()
