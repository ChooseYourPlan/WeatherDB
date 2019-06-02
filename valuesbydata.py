from datetime import datetime as dt, timedelta

def unixtimetotime(time):
    time = dt.utcfromtimestamp(time)
    time = time + timedelta(hours=0)
    return time.strftime('%Y-%m-%d %H:%M:%S') 

def fahrtocels(fahr):
    return (fahr - 32) / 1.8

def checkjsonkey(data,loc,key):
    if key in data[loc]:
        return data[loc][key]
    else:
        return 0
       
def get_values(data):
    latitude = data['latitude']
    longitude = data['longitude']
    timezone = data['timezone'] 

    #currently 
    currently_time = data['currently']['time']
    currently_time = unixtimetotime(currently_time)
    currently_summary = checkjsonkey(data,'currently','summary')
    currently_icon = checkjsonkey(data,'currently','icon')
    currently_preciptype = checkjsonkey(data,'currently','precipType')
    currently_temperature = fahrtocels(checkjsonkey(data,'currently','temperature'))
    currently_apparentTemperature = fahrtocels(checkjsonkey(data,'currently','apparentTemperature'))
    currently_humidity = checkjsonkey(data,'currently','humidity')
    currently_pressure = checkjsonkey(data,'currently','pressure')
    currently_windSpeed = checkjsonkey(data,'currently','windSpeed')
    currently_cloudCover = checkjsonkey(data,'currently','cloudCover',)
    currently_visibility = checkjsonkey(data,'currently','visibility')
    currently_ozone = checkjsonkey(data,'currently','ozone')


    #minutely_summary = checkjsonkey(data,'minutely','summary')
    #minutely_time = unixtimetotime(checkjsonkey(data,'minutely','time'))
    
    values = [latitude,longitude,timezone,
    currently_summary,currently_icon,currently_preciptype,currently_temperature,currently_time,
    currently_apparentTemperature,currently_humidity,currently_pressure,
    currently_windSpeed,currently_cloudCover,currently_visibility,
    currently_ozone]
    #minutely_summary,minutely_time]
         
    return values 
