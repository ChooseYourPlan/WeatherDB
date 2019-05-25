import requests
import json 
import argparse

#Get Api-Key from File
key_file = open("key.txt","r")
key = key_file.read()

#CLI-Arguments
parser = argparse.ArgumentParser(description='lat and lng getter')
parser.add_argument('-c','--city',type = str, help = 'City to Request')
parser.add_argument('-BW','--Baden-Wuerttemberg',type = str, help = 'Baden-Wuerttemberg')
parser.add_argument('-BY','--Bayern',type = str, help = 'Bayern')
parser.add_argument('-BE','--Berlin',type = str, help = 'Berlin')
parser.add_argument('-BB','--Brandenburg',type = str, help = 'Brandenburg')
parser.add_argument('-HV','--Bremen',type = str, help = 'Bremen')
parser.add_argument('-HH','--Hamburg',type = str, help = 'Hamburg')
parser.add_argument('-HE','--Hessen',type = str, help = 'Hessen')
parser.add_argument('-MV','--Mecklenburg-Vorpommern',type = str, help = 'Mecklenburg-Vorpommern')
parser.add_argument('-NI','--Niedersachsen',type = str, help = 'Niedersachsen')
parser.add_argument('-NW','--Nordrhein-Westfalen',dest = 'NR',action = 'store_true', help = 'Nordrhein-Westfalen')
parser.add_argument('-RP','--Rheinland-Pfalz',type = str, help = 'Rheinland-Pfalz')
parser.add_argument('-SL','--Saarland',type = str, help = 'Saarland')
parser.add_argument('-SN','--Sachsen',type = str, help = 'Sachsen')
parser.add_argument('-ST','--Sachsen-Anhalt',type = str, help = 'Sachsen-Anhalt')
parser.add_argument('-SH','--Schleswig-Holstein',type = str, help = 'Schleswig-Holstein')
parser.add_argument('-TH','--Thueringen',type = str, help = 'Thueringen')

args = parser.parse_args()

city = args.city

#Get-Request for lat and lng
response = requests.get("https://www.mapquestapi.com/geocoding/v1/address?key=" + str(key) + "&inFormat=kvp&outFormat=json&location=" + city + "%2CGermany&thumbMaps=false")

#Json evaluation
json_data = json.loads(response.text)

bundesland = json_data['results'][0]['locations'][0]['adminArea3']
lat  = json_data['results'][0]['locations'][0]['latLng']['lat']
lng  = json_data['results'][0]['locations'][0]['latLng']['lng']

#Print to console
print bundesland
print lat
print lng 
