import time
from datetime import datetime, date
import requests
import json

#Get Api-Key from File 
def get_apik():
    key_file = open("weather_key.txt","r")
    key = key_file.read()
    return key

def get_date(args,offset = 0):
    d = datetime.strptime(args.date,"%Y")
    unixtime = str(time.mktime(d.timetuple()))
    unixtime = unixtime[:-2]
    return int(unixtime) + 7200 + (offset * 86400)

def get_request(info_list,key,args,offset):
    lat = info_list[1]
    lng = info_list[2]
   
    key = key[:-1] 
   
    if not args.date:
       response = requests.get("https://api.darksky.net/forecast/" + key + "/" + str(lat) + "," + str(lng))
    else:
       response = requests.get("https://api.darksky.net/forecast/" + key + "/" + str(lat) + "," + str(lng) + "," + str(get_date(args,offset)))

    return response

def get_jsond(response):
    json_data = json.loads(response.text)
    return json_data	

def get_weather(info_list,args,offset = 0):
    key = get_apik()
    response = get_request(info_list,key,args,offset)
    data = get_jsond(response)
    return data
