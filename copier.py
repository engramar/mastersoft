fileinput = open('CNAR_Extract_with_Alt_Roadnames.TXT','r')
fileoutput = open('CNARFloors.txt', 'w')

total = 0

for line in fileinput:
    fields = line.split('|')
    floor = fields[15].strip()
    if floor != '':
    	print(line)	
    	fileoutput.write(line)
    	total = total + 1

fileinput.close()
fileoutput.close()