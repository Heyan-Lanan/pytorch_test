import time
from progressbar import *

progress = ProgressBar()
for i in progress(range(100)):
    # print("hi")
    time.sleep(0.1)
