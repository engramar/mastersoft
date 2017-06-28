import os

fileinput = open('drives.txt')
detailedoutput = open('detailedoutput.txt', 'w')
summaryoutput = open('summaryoutput.txt', 'w')

total = 0
grandtotal = 0

def printcount(drive,drivename):
	global total, grandtotal, fileoutput

	for root, dirs, files in os.walk(drive):
		total += len(files)	
		grandtotal += len(files)	
		print(drivename+root+"|"+str(total))
		detailedoutput.write(drivename+root+"|"+str(total))
		total = 0		
	summaryoutput.write(drivename+"|"+str(grandtotal)+"\n")	
	return				

for line in fileinput:
    fields = line.split('|')
    drive = fields[0].strip()
    drivename = fields[1].strip()
    printcount(drive,drivename)	
    
detailedoutput.close()
summaryoutput.close()