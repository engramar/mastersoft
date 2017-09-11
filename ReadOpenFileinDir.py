import os
import glob

os.chdir('F:\python\license')
files = glob.glob('*')

for fle in files:
      f = open(fle,'r')      
      text = f.read()
      print(text)
