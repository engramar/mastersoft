#########################################################################################################
#   Program Name : pythoncurl.py                                                                      #
#   Program Description:                                                                                #
#   This program generated legacy datasan token                                                         #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version Python v2                       14/10/2016            Engramar Bollas               #
#   Updated Version Python v3                       08/11/2016            Engramar Bollas               #
#########################################################################################################
import os
import json

print ("===============================================================================")
print ("                         DATASAN Token Generation")
print ("===============================================================================")
#Step 1 Generate Datasan Token
print (" ")
print ("===============================================================================")
print ("Starting Step 1 - Token generation.......")
print ("===============================================================================")
print (" ")
text = os.popen('curl -i -H "Accept: application/json" -X POST https://rapidmatch.datasan.com.au/token/jPhhb').read()
beg = text.find('{')
json_string = text[beg:len(text)]
obj = json.loads(json_string)
token = obj["token"]
print ("Token =====> "+str(token))
print (" ")

#Step 2 Activate Datasan Token in force.com 
print ("===============================================================================")
print ("Starting Step 2 - Activate token in force.com.......")
print ("===============================================================================")
print (" ")
step2 = "curl -i -H \"Accept: application/json\" -X POST https://rapidmatch.datasan.com.au/token/jPhhb/"+token+"/domain/force.com"
text = os.popen(step2).read()
print (text)
start = text.find('Status') + 8
end = start + 3
response_code = text[start:end]
if response_code == '200': 
    print (" ")
    print ("Response Code is 200 OK")
    print (" ")
else: 
    print ("Exception encountered")
    print (" ")
        
#Step 3 Activate Datasan Token in salesforce.com
print ("===============================================================================")
print ("Starting Step 3 - Activate token in salesforce.com.......")
print ("===============================================================================")
print (" ")
step3 = "curl -i -H \"Accept: application/json\" -X POST https://rapidmatch.datasan.com.au/token/jPhhb/"+token+"/domain/salesforce.com"
text = os.popen(step3).read()
print (text)
start = text.find('Status') + 8
end = start + 3
response_code = text[start:end]
if response_code == '200': 
    print (" ")
    print ("Response Code is 200 OK")
    print (" ")
else: 
    print ("Exception encountered")
    print (" ")

#Step 4 Activate Datasan Token in wildcard * 
print ("===============================================================================")
print ("Starting Step 4 - Activate token in wildcard * domains.......")
print ("===============================================================================")
print (" ")
step4 = "curl -i -H \"Accept: application/json\" -X POST https://rapidmatch.datasan.com.au/token/jPhhb/"+token+"/domain/*"
text = os.popen(step4).read()
print (text)
start = text.find('Status') + 8
end = start + 3
response_code = text[start:end]
if response_code == '200': 
    print (" ")
    print ("Response Code is 200 OK")
    print (" ")
else: 
    print ("Exception encountered")
    print (" ")
print ("===============================================================================")
print ("Generating Datasan Token completed")
print ("===============================================================================")
