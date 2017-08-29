import csv

with open('Sample_input_file.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    for line in reader:
    	outputRec=line[2]+"|"+line[3]+"|"+line[6]+"|"+line[7]
    	print(outputRec)

''' LEGEND
1=natural_key
2=family_names
3=first_name
4=middle_names
5=gender
6=date_of_birth
7=contact_email_address
8=alternate_email_address
9=contact_mobile_number
10=alternate_mobile_number
11=contact_landline_number
12=alternate_landline_number
13=contact_address_line_1
14=alternate_address_line_1
15=contact_suburb_name
16=alternate_suburb_name
17=contact_state
18=alternate_state
19=contact_postcode
20=alternate_postcode
21=contact_aus_dpid
22=alternate_aus_dpid
23=contact_country_code
24=alternate_country_code
'''
