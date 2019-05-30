import time
from datetime import datetime, date
import requests
import json

#Get Api-Key from File 
def get_apik():
    key_file = open("weather_key.txt","r")
    key = key_file.read()
    return key

def get_date(args):
    d = datetime.strptime(args.date,"%d/%m/%y %H:%M")
    unixtime = str(time.mktime(d.timetuple()))
    unixtime = unixtime[:-2]
    print unixtime 
    return unixtime

def get_request(info_list,key,args):
    lat = info_list[1]
    lng = info_list[2]
   
    key = key[:-1] 
   
    if not args.date:
       response = requests.get("https://api.darksky.net/forecast/" + key + "/" + str(lat) + "," + str(lng))
    else:
       response = requests.get("https://api.darksky.net/forecast/" + key + "/" + str(lat) + "," + str(lng) + "," + get_date(args))

    return response

def get_jsond(response):
    json_data = json.loads(response.text)
   
    return json_data	

def get_weather(info_list,args):
    key = get_apik()
    response = get_request(info_list,key,args)
    data = get_jsond(response)
    return data
