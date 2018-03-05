#########################################################################################################
#   Program Name : ncoadriver.py                                                                        #
#   Program Description:                                                                                #
#   This program sends calls ncoa API                                                                   #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 05/03/2018            Engramar Bollas               #
#########################################################################################################

import httplib2 as http
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import sys

import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Create HTTPS connection
c = HTTPSConnection("0.0.0.0", context=context)

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
uri = 'https://ncoa-sb.doubleiqapps.com/NCOA'
target = urlparse(uri)
method = 'POST'
#body = '{"option":{"source":"AUPAF"},"payload":{"fullAddress":%s}}' % address
body = '{"collection_id": "1",\
"return_deceased_flag": True,\
"check_date_from": "",\
"input_set": [\
{"record_id": "999999XXXX1", "dpid": "99960062", "first_name": "MELVA", "last_name": "HUBNER", "title": "MRS"},\
{"record_id": "999999XXXX2", "dpid": "99982188", "first_name": "WILLIAM HAROLD", "last_name": "JESSOP", "title": "MR"}\
]}'

h = http.Http()		
response, content = h.request(
		target.geturl(),
		method,
		body,
		headers)

json_string = str(content, 'utf8')	
jdata = json.loads(json_string)
payld = jdata['payload']
'''
fname = input('Enter Input Dataset: ')
record = open(fname)

filename  = open("HRAMatcherOutput.txt",'w')
sys.stdout = filename

for line in record:
	field = line.split('|')
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
	score = fuzz.ratio(fieldstrip,candidateaddress)
	print (fieldstrip+"|"+candidateaddress+"|"+str(score))
'''
