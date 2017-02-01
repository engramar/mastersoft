#########################################################################################################
#   Program Name : GoogleMatcher.py                                                                     #
#   Program Description:                                                                                #
#   This program processes an address dataset against Google Maps gets the first candidate and scores   #
#   the similarity.                                                                                     #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 01/02/2017            Engramar Bollas               #
#########################################################################################################
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys
import requests

url = 'http://maps.googleapis.com/maps/api/geocode/json?'

fname = input('Enter Input Dataset: ')
record = open(fname)

outfile = open("GoogleMatcherOutput.txt",'w')

for line in record:
    field = line.split('|')
#########################################################################################################
#  Change the index depending on the position of the addresss in your input dataset                     #
#########################################################################################################
    address1 = field[1].strip()
    params = dict(
        address=address1,
        sensor='false'
    )    
    data = requests.get(url=url, params=params)
    binary = data.content
    
    try: js = json.loads(binary.decode("utf-8"))
    except: js = None

    if 'status' not in js or js['status'] != 'OK':
        location = ""
    else:    
        location = js['results'][0]['formatted_address']
    
    location1 = (location.encode('cp1252', errors='replace').decode('cp1252'))
    score = fuzz.ratio(address1,location1)
    outfile.write (address1+"|"+location1+"|"+str(score)+'\n')

print ('Run completed')