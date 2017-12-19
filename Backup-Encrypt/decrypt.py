import os
import struct
import sys
from Crypto.Cipher import AES
from Crypto.Hash import MD5

key = MD5.new(sys.argv[1]).hexdigest()[0:16] #hashlib.md5() can also be used
iv = sys.argv[2]
chunk_size=128*1024

def decrypt(crypt_path, decrpyt_path=None):
    with open(crypt_path, 'rb') as crypt_file:
        file_size = struct.unpack('Q', crypt_file.read(8))[0]
        # Replace struct.calcsize('Q') by 8
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(decrpyt_path, 'wb') as decrypt_file:
            while True:
                chunk = crypt_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                decrypt_file.write(decryptor.decrypt(chunk))
            decrypt_file.truncate(file_size)

if(__name__ == "__main__"):
    CRYPTED_DIR = os.path.abspath('../Backup')
    FINALPATH = os.path.abspath(os.path.join(os.path.expanduser('~'),'Desktop/Decrypted-Backup'))

    for root, subdirs, files in os.walk(CRYPTED_DIR):
        useful_root = root[len(CRYPTED_DIR)+1:]
        for subdir in subdirs:
            pathlist = os.path.join(FINALPATH,useful_root,subdir)
            os.makedirs(pathlist)
        for file in files:
            src = os.path.join(root,file)
            dest = os.path.join(FINALPATH,useful_root,file)
            decrypt(src,dest)
    print "Decryption Complete."