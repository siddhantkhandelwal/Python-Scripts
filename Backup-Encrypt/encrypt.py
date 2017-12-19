import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5


def crypt(ip_filepath,op_filepath):
    chunk_size = 128*1024
    keys = open('pwd.txt','r').read().split('\n')
    key = MD5.new(keys[0]).hexdigest()[0:16] #hashlib.md5() can also be used
    filesize = os.path.getsize(ip_filepath)

    encryptor = AES.new(key,AES.MODE_CBC, keys[1])
    
    with open(ip_filepath, 'rb') as in_file:
        with open(op_filepath, 'wb') as op_file:
            op_file.write(struct.pack('Q', filesize))
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                op_file.write(encryptor.encrypt(chunk))


if(__name__ == "__main__"):
    paths = [os.path.abspath(path) for path in open('paths.txt','r').read().split()]
    FINALPATH = os.path.abspath('./Backup')
    for path in paths:
        folder_name = os.path.split(path)[1]
        for root, subdirs, files in os.walk(path):
            useful_root = root[len(path)+1:]
            for subdir in subdirs:
                pathlist = os.path.join(FINALPATH,folder_name,useful_root,subdir)
                os.makedirs(pathlist)
            for file in files:
                src = os.path.join(root,file)
                dest = os.path.join(FINALPATH,folder_name,useful_root,file)
                crypt(src,dest)
        print path + " paths complete."
    print "Encryption Successful"