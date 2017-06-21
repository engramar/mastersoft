my_file  = open('matching.log', 'r')
out_file = open('output.txt', 'w')

if my_file:
    current_line = my_file.readline()

for line in my_file:
	previous_line = current_line 
	current_line = line 
	
	if 'Vs.' in current_line:
		next_line = next(my_file)		
		out_file.write(previous_line.rstrip() + "|" + next_line)