import itertools

functionality = ["Address Validation using AUPAF",
	 	  		       "Address Validation using GNAF",
	 	  		       "Address Validation using NZPAF",
	   	  		     "Address Validation using NZAD",
	  	  		     "Address Validation using CNAR"]

testmachine = ["64-bit Windows Server 2016",
			         "64-bit Red Hat Enterprise Linux 7",
			         "64-bit macOS 10.12"]

cpu = ["4 Cores","8 Cores"]

ram = ["4GB","8GB"]

heap = ["1GB","2GB"]

threads = ["1","2","3","4"]

testdataquality = ["100% Clean",
			             "10% Unclean",
			             "20% Unclean",
			             "30% Unclean"]

garbagecollection = ["GC is on",
			         "GC is off"]

harmonylogging = ["Logging is on",
			      "Logging is off"]			         

p = itertools.product(functionality, 
					  testmachine, 
					  cpu,
					  ram,
					  heap,
					  threads,
					  testdataquality,
					  garbagecollection)

for rec in p:
	print (rec)	
