fileinput = open('Suncorp_1M_Output_1035.txt','r')
fileoutput = open('Suncorp_1M_Output_1035_Reordered.txt', 'w')

ctr = 1
header_rec = fileinput.readline()
fileoutput.write(header_rec)

for line in fileinput:
	fields = line.split('|')
	fields[0] = str(ctr)	
	myString = "|".join(fields)
	fileoutput.write(myString)
	ctr = ctr + 1
	print(ctr)

fileinput.close()
fileoutput.close()
