from datetime import datetime, timedelta
import os
import time

while 1:
    print ('Run CR_Updater.py..')
    os.system('python jiradataingestion.py')

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)
