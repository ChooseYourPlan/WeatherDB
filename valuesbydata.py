from datetime import datetime

def unixtimetotime(time):
    ts = int(time)
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def get_values(data):
    latitude = data['latitude']
    longitude = data['longitude']
    
    #currently
    currently_time = data['currently']['time']
    currently_time = unixtimetotime(currently_time)
    summary = data['currently']['summary']
    preciptype = data['currently']['precipType']
    temperature = data['currently']['temperature']
    values = [latitude,longitude,summary,preciptype,temperature]
    return values 
