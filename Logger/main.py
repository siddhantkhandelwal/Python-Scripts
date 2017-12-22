import sys
from os import path, makedirs
from datetime import datetime

timestamp = datetime.fromtimestamp
TODAY = datetime.now().date()

PROMPT = sys.argv[1][:-1].title() + ">"
FILEPATH = path.join(path.expanduser('~'), 'LOGS', sys.argv[1])
MODE = 'a'

if (not path.exists(FILEPATH)):
    if not path.exists(path.dirname(FILEPATH)):
        makedirs(path.dirname(FILEPATH))
    MODE = 'w'

if(MODE == 'w' or timestamp((path.getmtime(FILEPATH))).date() != TODAY):
    with open(FILEPATH, MODE) as f:
        f.write("\n##" + str(TODAY) + ":\n")
try:
    while True:
        note = raw_input(PROMPT)
        with open(FILEPATH, 'a') as f:
            f.write(note + "\n")
except KeyboardInterrupt:
    sys.exit()
