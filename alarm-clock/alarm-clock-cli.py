'''
Requirements:
vlc:            pip install vlc
mutagen:        pip install mutagen
python-crontab: pip install python-crontab
'''

import sys
import string
import vlc
import os
import getpass
from time import sleep
from mutagen.mp3 import MP3
from crontab import CronTab


if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("\nUsage: [ python ] alarm-clock-cli.py [option] h m")
    print("Example: [ python ] alarm-clock-cli.py 1 10 25")
    print("Example: [ python ] alarm-clock-cli.py 1 0 4")
    print("Example: [ python ] alarm-clock-cli.py 2")
    print("Use a value of 0 for testing the alarm immediately.")
    print("Example: [ python ] alarm-clock-cli.py 0")
    print("Plays mp3(only) file stored in cwd named as 'alarm.mp3'")
    print("Press Ctrl-C to terminate the alarm clock early.")
    sys.exit(1)

username = getpass.getuser()
script_path = os.path.abspath(sys.argv[0])

if int(sys.argv[1]) == 0:
    #print(os.path.dirname(script_path))
    alarm_file = vlc.MediaPlayer(os.path.join(os.path.dirname(script_path), "alarm.mp3"))
    alarm_file_length = MP3(os.path.join(os.path.dirname(script_path), "alarm.mp3")).info.length
    alarm_file.play()
    sleep(alarm_file_length)

elif int(sys.argv[1]) == 1:
    hours= int(sys.argv[2])
    minutes = int(sys.argv[3])
    
    print("Do yo want to schedule the alarm to ring daily/weekly? ('d' for daily, 'w' for weekly): ")
    schedule_period = input()
    
    if schedule_period == 'd':
        cron_task = CronTab(user=username)
        idno='0'
        job = cron_task.new(command='python ' + script_path + ' 0', comment='alarm-clock-' + idno)
        job.hour.on(hours)
        job.minute.on(minutes)
        job.day.every(1)
        #print(job.is_valid())
        cron_task.write()
        
    elif schedule_period == 'w':
        print("Which day of the week? (0-6): ")
        dow = int(input())
        cron_task = CronTab(user=username)
        job = my_cron.new(command="python '" + script_path + "' 0")
        job.hour.on(hours)
        job.minute.on(minutes)
        job.dow.on(dow)
        job.week.every(1)
        cron_task.write()
    else:
        hours= int(sys.argv[2])
        minutes = int(sys.argv[3])
        total_seconds= hours*60*60 + minutes*60
        alarm_file = vlc.MediaPlayer(os.path.join(os.path.dirname(script_path), "alarm.mp3"))
        alarm_file_length = MP3(os.path.join(os.path.dirname(script_path), "alarm.mp3")).info.length
        alarm_file.play()
        sleep(total_seconds)
        #print(os.path.dirname(script_path))
        sleep(alarm_file_length)

elif int(sys.argv[1]) == 2:
    cron_task = CronTab(user=username)
    for job in cron_task:
        if job.comment.startswith('alarm-clock-'):
            print (job)
    idno = input("Enter the id for the alarm to be deleted: ")
    for job in cron_task:
        if job.comment=='alarm-clock-'+idno:
            cron_task.remove(job)
            cron_task.write()