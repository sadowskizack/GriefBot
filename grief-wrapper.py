import subprocess
import threading
import time
from playsound import playsound

# commented out because it's annoying, as intended
#def DONO():
    #playsound("DONO-INTRO.mp3")

#x = threading.Thread(target=DONO, args=())

#x.start()
time.sleep(2)

subprocess.call(["python", "grief.py"])


