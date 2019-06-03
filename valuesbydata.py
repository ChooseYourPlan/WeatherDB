from datetime import datetime as dt, timedelta

def unixtimetotime(time):
    time = dt.utcfromtimestamp(time)
    time = time + timedelta(hours=0)
    return time.strftime('%Y-%m-%d %H:%M:%S') 

def fahrtocels(fahr):
    return (fahr - 32) / 1.8

def checkjsonkey(data,loc,key,i = 0):
    if key in data[loc]:
        return data[loc][key]
    elif i and key in data[loc]['data'][i]:
        return data[loc]['data'][i][key]
    else:
        return 0

def get_values(data,i = 0):
    latitude = data['latitude']
    longitude = data['longitude']
    timezone = data['timezone'] 
    
    if i:
        loc = 'hourly'
    else:
        loc = 'currently'
    
    time = checkjsonkey(data,loc,'time',i)
    time = unixtimetotime(time)
    summary = checkjsonkey(data,loc,'summary',i)
    icon = checkjsonkey(data,loc,'icon',i)
    preciptype = checkjsonkey(data,loc,'precipType',i)
    temperature = fahrtocels(checkjsonkey(data,loc,'temperature',i))
    apparentTemperature = fahrtocels(checkjsonkey(data,loc,'apparentTemperature',i))
    humidity = checkjsonkey(data,loc,'humidity',i)
    dewPoint = checkjsonkey(data,loc,'dewPoint',i)
    windSpeed = checkjsonkey(data,loc,'windSpeed',i)
    cloudCover = checkjsonkey(data,loc,'cloudCover',i)
    visibility = checkjsonkey(data,loc,'visibility',i)
    uvIndex = checkjsonkey(data,loc,'uvIndex',i)
    
    values = [latitude,longitude,timezone,summary,icon,preciptype,temperature,time,
    apparentTemperature,humidity,dewPoint,windSpeed,cloudCover,visibility,uvIndex]
         
    return values 
