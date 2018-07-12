#########################################################################################################
#   Program Name : HRAPerformanceTester.py                                                              #
#   Program Description:                                                                                #
#   This program processes an address dataset against HRA and determines response time                  #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 12/07/2018            Engramar Bollas               #
#########################################################################################################
import httplib2 as http
import json
import sys
import time

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

infile  = open("HRAPeformanceInput.txt", 'r')
outfile = open("HRAPerformanceTesterOutput.txt",'w')

for address in infile:	
	body = '{"option": {"locale": "AU","baseSource": "GNAF"},"payload":{"fullAddress":%s}}' % address
	h = http.Http()		

	start_time = time.time()
	response, content = h.request(
			target.geturl(),
			method,
			body,
			headers)
	end_time = time.time()
	elapsed_time = end_time - start_time
	outfile.write(str(elapsed_time)+'\n')
	#elapsed_time_ms = int(round(elapsed_time * 1000)
