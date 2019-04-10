#########################################################################################################
#   Program Name : AddressProfiler.py                                                                   #
#   Program Description:                                                                                #
#   This program basically does profiling of profilinginput from PreAddressProfiler.py                  #
#                                                                                                       #
#   Tag Legend                                                                                          #
#       X - Alphanumeric word                                                                           #
#       A - Alphabetic word                                                                             #
#       9 - Numeric word                                                                                #
#       $ - Word with special character/s                                                               #
#       POBox - Postal Type                                                                             #
#       Unit - Subdwelling Type                                                                         #
#       Level - Floor/Level Type                                                                        # 
#       Block - Block Type                                                                              #
#       Rural - Rural Delivery Type                                                                     #
#       Street - Street Type                                                                            #
#       State - Au State Name                                                                           #
#       TownCity - NZ Town/City                                                                         #
#                                                                                                       #
#   PreRequisite:                                                                                       #
#   PreAddressProfiler.py must be triggered first.                                                      #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 04/07/2016            Engramar Bollas               #
#########################################################################################################
import sys
import re

print ('Running AddressProfiler...')

record = open('profilerinput')

filename  = open("AddressProfilerOutput.txt",'w')
sys.stdout = filename

filename2 = open("AddressProfilerOutputWithAddresses.txt",'w')

lexicals = {
	 'B' : 'Level' ,
	 'BASEMENT' : 'Level' ,
	 'WEST AUST' : 'State' ,
	 'WESTERN AUST' : 'State' ,
	 'WESTERN AUSTRALIA' : 'State'
}
	
patternlist = []
for line in record:
    try:
        pattern = re.compile(r'\b(' + '|'.join(lexicals.keys()) + r')\b')
        newrecord = pattern.sub(lambda x: lexicals[x.group()], line)
    except KeyError:
        newrecord = line
    newrecord = newrecord.rstrip()
    
    outaddressfields = []
    columnlist = newrecord.split('|')		
    
    fieldlist = columnlist[3].split();
	   
    for field in fieldlist:			
        outfield = "X"			

        if field == ('POBox'):
            outaddressfields.append(field)
            continue  		
		
        if field == ('Unit'):
            outaddressfields.append(field)
            continue  		

        if field == ('Level'):
            outaddressfields.append(field)
            continue  		

        if field == ('Block'):
            outaddressfields.append(field)
            continue  					

        if field == ('Rural'):
            outaddressfields.append(field)
            continue  					
			
        if field == ('Street'):
            outaddressfields.append(field)
            continue  		

        if field == ('State'):
            outaddressfields.append(field)
            continue  		

        if field.isdigit() == True:		
            outfield = '9'
		
        if field.isalpha() == True:		
            outfield = 'A'

        if field.find('/')!=-1:	
            outfield = 'UnitAndStNum'
			
        if field == ',':		
            outfield = ','
			
        special = ['~','`','!','@','#','$','%','^','&','*','(',')','_','+','=','{','}','[',']',':','>',';','<','?','*','+']
        if any(ext in field for ext in special):
            outfield = '$'

        outaddressfields.append(outfield)
        
    pattern = ""
    for item in outaddressfields:
        pattern += item+" "		
    patternlist.append(pattern)

    filename2.write(pattern+"|"+newrecord+'\n')	


counts = dict() 
for i in patternlist:
    counts[i] = counts.get(i, 0) + 1

for keys,values in counts.items():
    print(keys+"|"+str(values))	