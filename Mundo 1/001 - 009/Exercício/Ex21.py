import  vlc

import time



p = vlc.MediaPlayer(‘testaudio.mp3’)

p.play()

print("The audio will finish playing in 4 seconds")

time.sleep(4)

p.stop()