from xml.dom import minidom

NAME=""
fhandoutput = open('ExtractedAddresses.txt', 'w')

ctr=0 
xmldoc = minidom.parse('CNARIndexCleansed.xml')
itemlist = xmldoc.getElementsByTagName('field')
for s in itemlist:
	if s.attributes['name'].value == 'complete_address': 
		ctr = ctr + 1
		try:
			NAME = s.getElementsByTagName("val")[0].childNodes[0].data
			fhandoutput.write (str(ctr)+"|"+NAME+"\n")
		except IndexError:
			fhandoutput.write (str(ctr)+"|"+"No childNodes for this element"+"\n")
	
	if s.attributes['name'].value == 'dpid':
		try:
			NAME = s.getElementsByTagName("val")[0].childNodes[0].data
			fhandoutput.write (str(ctr)+"|"+NAME+"\n")
		except IndexError:
			fhandoutput.write (str(ctr)+"|"+"No childNodes for this element"+"\n")

print("Processing completed")
fhandoutput.close()