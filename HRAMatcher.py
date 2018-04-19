#########################################################################################################
#   Program Name : HRAMatcher.py                                                                        #
#   Program Description:                                                                                #
#   This program processes an address dataset against HRA, gets the first candidate and scores          #
#   the similarity.                                                                                     #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 01/02/2017            Engramar Bollas               #
#   Case Sensitivity                                19/04/2018            Engramar Bollas               #
#########################################################################################################

import httplib2 as http
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}
#########################################################################################################
#  Change this URL to either au or nz                                                                   #
#########################################################################################################
uri = 'http://localhost:8080/HRAWeb/hra/rest/au/address/similar-addresses'
target = urlparse(uri)
method = 'POST'

fname = input('Enter Input Dataset: ')
record = open(fname)

filename  = open("HRAMatcherOutput.txt",'w')
sys.stdout = filename

for line in record:
	field = line.split('|')
#########################################################################################################
#  Change the index depending on the position of the addresss in your input dataset                     #
#########################################################################################################
	fieldstrip = field[1].strip()
	address = ("\""+fieldstrip+"\"")
	body = '{"option":{"source":"AUPAF"},"payload":{"fullAddress":%s}}' % address
	h = http.Http()		
	response, content = h.request(
			target.geturl(),
			method,
			body,
			headers)
		
	json_string = str(content, 'utf8')	
	jdata = json.loads(json_string)
	payld = jdata['payload']	

	candidateaddress=''	
	for i in payld:
		candidateaddress=(i['fullAddress'])
		if candidateaddress=='': break 							
	score = fuzz.token_set_ratio(fieldstrip,candidateaddress)
	print (fieldstrip+"|"+candidateaddress+"|"+str(score))
