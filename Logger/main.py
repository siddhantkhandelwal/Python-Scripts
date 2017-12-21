import sys
from os import path, makedirs
from datetime import datetime

if(sys.argv[1] != "tasks" and sys.argv[1] != "logs"):
    sys.exit("Invalid argument")

timestamp = datetime.fromtimestamp
TODAY = datetime.now().date()
PROMPT = sys.argv[1][:-1].title() + ">"
FILEPATH = path.join(path.expanduser('~'), 'LOGS', sys.argv[1])

if (not path.exists(FILEPATH)):
    if not path.exists(path.dirname(FILEPATH)):
        makedirs(path.dirname(FILEPATH))
    MODE = 'w'
else:
    MODE = 'a'

if(MODE == 'w' or timestamp((path.getmtime(FILEPATH))).date() != TODAY):
    with open(FILEPATH, MODE) as f:
        f.write("\n##" + str(TODAY) + ":\n")
try:
    while True:
        with open(FILEPATH, 'a') as f:
            f.write(raw_input(PROMPT) + "\n")
except KeyboardInterrupt:
    sys.exit()
