#!usr/bin/python
# Pro-Panda
# To find and remove duplicate files in the computer

import sys
import os
import filecmp

path = sys.argv[1]  # Sample Input: /home/PP/media_files/
file_size, size = [], []

for root, dirt, files in os.walk(path):
    for file in files:
        temp_path = os.path.join(root, file)
        file_size.append([os.stat(temp_path).st_size, temp_path])
        size.append(os.stat(temp_path).st_size)

duplicate_size = [x for x in size if size.count(x) > 1]
duplicates = [x for x in file_size if duplicate_size.count(x[0]) > 0]

len_dup = len(duplicates)

x, y = 0, 0
while x < len_dup:
    y = x + 1
    while y < len_dup:
        if(duplicates[x][0] == duplicates[y][0]):
            duplicates[x].append(duplicates[y][1])
            duplicates.pop(y)
            y = y - 1
            len_dup = len_dup - 1
        y = y + 1
    x = x + 1

for x in range(len(duplicates)):
    for y in range(1, len(duplicates[x])):
        print str(y) + '. ' + duplicates[x][y]
    file_no = raw_input("Which file(s) do you want to delete ?")
    if(file_no='0'):
        continue
    file_no = file_no.split(',')
    file_no = [int(r) for r in file_no]
    for j in file_no:
        os.remove(duplicates[x][j])
    print "Files successfully removed/n"
