'''
Requirements:
vlc:        pip install vlc
mutagen:    pip install mutagen
'''

import sys
import string
import vlc
from time import sleep
from mutagen.mp3 import MP3

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Usage: [ python ] alarm-clock-cli.py h m s")
    print("Example: [ python ] alarm-clock-cli.py 10 25 56")
    print("Example: [ python ] alarm-clock-cli.py 0 4 20")
    print("Use a value of 0 for testing the alarm immediately.")
    print("Plays mp3(only) file stored in cwd named as 'alarm.mp3'")
    print("Press Ctrl-C to terminate the alarm clock early.")
    sys.exit(1)

total_seconds = 0

if sys.argv[1] == 0 and len(sys.argv) == 2:
    total_seconds = 0
elif len(sys.argv)==4:
    hours = int(sys.argv[1])
    minutes = int(sys.argv[2])
    seconds = int(sys.argv[3])
    total_seconds = hours*60*60 + minutes*60 + seconds
elif len(sys.argv)==3:
    hours = int(sys.argv[1])
    minutes = int(sys.argv[2])
    total_seconds = hours*60*60 + minutes*60
else:
    hours = int(sys.argv[1])
    total_seconds = hours*60*60

print("Sleeping for %d seconds" % total_seconds)
alarm_file = vlc.MediaPlayer("alarm.mp3")
alarm_file_length = MP3("alarm.mp3").info.length
sleep(total_seconds)
alarm_file.play()
#print(audio.info.length)
sleep(alarm_file_length)
