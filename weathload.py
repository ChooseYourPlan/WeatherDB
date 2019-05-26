import requests
import json

#Get Api-Key from File
def get_apik():
    key_file = open("weather_key.txt","r")
    key = key_file.read()
    return key

def get_request(info_list,key):
    lat = info_list[1]
    lng = info_list[2]
   
    key = key[:-1] 
    response = "https://api.darksky.net/forecast/" + key + "/" + str(lat) + "," + str(lng)
   # print resp
    response = requests.get("https://api.darksky.net/forecast/" + key + "/" + str(lat) +  "," + str(lng)) 
   
    return response

def get_jsond(response):
    json_data = json.loads(response.text)
   
    return json_data	

def get_weather(info_list):
    key = get_apik()
    response = get_request(info_list,key)
    data = get_jsond(response)
    return data



