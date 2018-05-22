import pandas as pd
import re

file = 'NZ_Small2.xlsx'
fileoutput = open('NZ_Small_Output2.txt', 'w')

xl = pd.ExcelFile(file)
#print(xl.sheet_names)
df = xl.parse('Sheet1')
#print(df.iloc[0][0])

fileoutput.write("UID"+"|"+ \
				 "Endpoint"+"|"+ \
   	             "Method"+"|"+ \
   	             "Combination"+"|"+ \
   	             #"InputAddress"+"|"+ \
   	             "AddressLine1"+"|"+ \
	             "AddressLine2"+"|"+ \
	             "AddressLine3"+"|"+ \
   	             "AddressLine4"+"|"+ \
	             "AddressLine5"+"|"+ \
	             "AddressLine6"+"|"+ \
   	             "AddressLine7"+"|"+ \
	             "Postcode"+"|"+ \
	             "Country"+'\n')

tempPostCode = ''

for index, row in df.iterrows():
    ID = row[31]
    #Endpoint = row[16]     
    Method = row[1]
    methodFields = Method.split('.')
    try:
	    if 'RightAddress' in methodFields[0]:
	    	Endpoint = 'http://win2016-srv-tst/'+methodFields[0].lower()+'.asmx'
	    	Method = methodFields[1]
	    else: 
	    	Endpoint = 'http://win2016-srv-tst/rightaddress.asmx'
	    	Method = methodFields[0]
    except IndexError:
    	print('No method')

    Combination = row[15].replace('|','-')     
    InputAddress = row[9].replace('postcode=','')    
    fields = InputAddress.split('|')

    try:
    	if (fields[0].isdigit()):
    		tempPostCode = fields[0]    		
    		fields[0] = ''
    	AddressLine1 = fields[0]
    except IndexError:
    	AddressLine1 = ''

    try:
    	if (fields[1].isdigit()):
    		tempPostCode = fields[1]
    		fields[1] = ''
    	AddressLine2 = fields[1]
    except IndexError:
    	AddressLine2 = ''

    try:
    	if (fields[2].isdigit()):
    		tempPostCode = fields[2]
    		fields[2] = ''
    	AddressLine3 = fields[2]
    except IndexError:
    	AddressLine3 = ''

    try:
    	if (fields[3].isdigit()):
    		tempPostCode = fields[3]
    		fields[3] = ''
    	AddressLine4 = fields[3]    	
    except IndexError:
    	AddressLine4 = ''

    try:
    	if (fields[4].isdigit()):
    		tempPostCode = fields[4]
    		fields[4] = ''
    	AddressLine5 = fields[4]
    except IndexError:
    	AddressLine5 = ''

    try:
    	if (fields[5].isdigit()):
    		tempPostCode = fields[5]
    		fields[5] = ''
    	AddressLine6 = fields[5]
    except IndexError:
    	AddressLine6 = ''

    try:
    	if (fields[6].isdigit()):
    		tempPostCode = fields[6]
    		fields[6] = ''
    	AddressLine7 = fields[6]
    except IndexError:
    	AddressLine7 = ''

    try:
    	if (fields[7].isdigit()):
    		Postcode = fields[7]
    	else:   		
    		Postcode = tempPostCode    	
    except IndexError:
    	Postcode = tempPostCode    	

    try:
    	Country = fields[8]
    except IndexError:
    	Country = ''

    fileoutput.write(str(ID)+"|"+ \
    				 str(Endpoint)+"|"+ \
    	             str(Method)+"|"+ \
    	             str(Combination)+"|"+ \
    	             #str(InputAddress)+"|"+ \
    	             str(AddressLine1)+"|"+ \
		             str(AddressLine2)+"|"+ \
		             str(AddressLine3)+"|"+ \
    	             str(AddressLine4)+"|"+ \
		             str(AddressLine5)+"|"+ \
		             str(AddressLine6)+"|"+ \
    	             str(AddressLine7)+"|"+ \
		             str(Postcode)+"|"+ \
		             str(Country)+'\n')

fileoutput.close()