import re

original_string = open('CNARIndex.xml').read()
new_string = re.sub(r'^  <term.*\n?', '', original_string, flags=re.MULTILINE)
open('CleansedCNARindex100.xml', 'w').write(new_string)