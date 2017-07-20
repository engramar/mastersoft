#########################################################################################################
#   Program Name : addressgeocoder.py                                                                   #
#   Program Description:                                                                                #
#   This program geocodes an address using Harmony Suite                                                #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 20/07/2017            Engramar Bollas               #
#########################################################################################################

import httplib2 as http
import json
import sys
import pprint

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}

uri = 'http://localhost:8080/HarmonyWS/rest/parseCustomerData'
target = urlparse(uri)
method = 'POST'

address = ("\""+"Suite 202 Level 2 220 George St, Sydney NSW 2190"+"\"")
body = '{"harmonyServiceConfig":{"role":"DEMO","includeChanges":false,"failOnError": false,"offset":""},"parserInput":{"rawDataInput":{"address":{"value":%s}}}}' % address

h = http.Http()		
response, content = h.request(
target.geturl(),
method,
body,
headers)
		
json_string = str(content, 'utf8')	
jdata = json.loads(json_string)
payld = jdata['ciqPartyDocument']	

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(payld)
