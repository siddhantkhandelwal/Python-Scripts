#!usr/bin/python

import os
import hashlib
hasher = hashlib.md5()

# Example : /home/PP/Courses/
path = raw_input("Please enter the path of the root directory:")

file_size, size, md5_list = [], [], []

for root, dirt, files in os.walk(path):
    for file in files:
        temp_path = os.path.join(root, file)
        file_size.append([temp_path, os.stat(temp_path).st_size])
        size.append(os.stat(temp_path).st_size)
duplicate_size = [x for x in size if size.count(x) > 1]
duplicates = [x for x in file_size if duplicate_size.count(x[1]) > 0]

for x in range(len(duplicates)):
    file_p = open(duplicates[x][0], 'rb')
    temp_var = hasher.update(file_p.read())
    md5_file = (str(hasher.hexdigest()))
    duplicates[x].append(md5_file)
    md5_list.append(md5_file)

md5_duplicate = [x for x in md5_list if md5_list.count(x) > 1]

final = [x for x in duplicates if md5_duplicate.count(x[2]) > 0]

for x in range(len(duplicates)):
    for y in range(x + 1, len(duplicates)):
        if(duplicates[x][2] == duplicates[y][2]):
            print "1.", duplicates[x][0], "\n2.", duplicates[y][0]
            num = int(
                raw_input("Enter the file number you want to delete (Enter 0 to skip):"))
            if(num == 1):
                os.remove(duplicates[x][0])
                print("File successfully removed")
                break
            elif(num == 2):
                os.remove(duplicates[y][0])
                print("File successfully removed")
