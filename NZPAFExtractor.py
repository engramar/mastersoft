my_file  = open('HELLONZPAFExtract', 'r')
out_file = open('NZPAFExtract.txt', 'w')

ctr=0
saved_complete_address = ""
saved_dpid = ""

if my_file:
    current_line = my_file.readline()

for line in my_file:
	ctr = ctr + 1
	previous_line = current_line 
	current_line = line 
	
	if 'delivery_service_type' in current_line:
		next_line = next(my_file)		
		saved_complete_address = next_line

	if 'dpid' in current_line:
		next_line = next(my_file)		
		saved_dpid = next_line
		out_dpid = saved_dpid.replace("<val>","").replace("</val>","")
		out_complete_address = saved_complete_address.replace("<val>","").replace("</val>","")  
		out_file.write(out_dpid.rstrip()+"|"+out_complete_address.rstrip()+"\n")
		saved_complete_address = ""
		saved_dpid = ""