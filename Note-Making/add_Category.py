#! /usr/bin/python
import sys
import os


def addCategory(category):
    NOTES_FOLDER = '.Notes'
    path = os.path.join(os.path.expanduser('~'), NOTES_FOLDER)
    if not (os.path.exists(path)):
        os.makedirs(path)
    filepath = os.path.join(path, category)
    if not os.path.exists(filepath):
        category_file = open(filepath, 'w')
        category_file.close()


if (__name__ == __main__):
    for category in sys.argv:
        addCategory(category)
