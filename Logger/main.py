import sys
import re
import json
from os import path, makedirs
from datetime import datetime

timestamp = datetime.fromtimestamp
TODAY = datetime.now().strftime("%B%d")
try:
    PROMPT = sys.argv[1][:-1].title() + ">"
except IndexError:
    sys.exit("Missing input!")

FILEPATH = path.join(path.expanduser('~'), 'LOGS', sys.argv[1]) + ".json"
CLOSE_ERR = (EOFError, KeyboardInterrupt)

if(__name__=="__main__"):
    if (not path.exists(FILEPATH)):
        if not path.exists(path.dirname(FILEPATH)):
            makedirs(path.dirname(FILEPATH))

    try:
        with open(FILEPATH,'r') as f:
            data = json.load(f)
            try:
                data = data[sys.argv[1]]
            except KeyError:
                data = {}
    except (IOError):    
        with open(FILEPATH,'w') as f:
            json.dump({sys.argv[1]:{}},f)
        data = {}

    if (not(TODAY in data)):
        today_list = []
    else:
        today_list = data[TODAY]

    while True:
        try:
            note = input(PROMPT)
            if (re.fullmatch('(\\x1b\[[ABCD])*',note)):
                continue
            today_list.append(note)

        except CLOSE_ERR:
            sys.exit()
        with open(FILEPATH,'w') as f:
            data.update({TODAY: today_list})
            json.dump({sys.argv[1]:data},f)
            datetime.now().strftime("%B%d")
