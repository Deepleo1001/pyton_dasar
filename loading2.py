import itertools
import threading
import time
import sys

done=False

def animeate ():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break 
        
        sys.stdout.write('\rloading' +c)
        sys.stdout.write('\rDone!')
t=threading.Thread(target=animeate)
t.start

time.sleep(10)
done=True