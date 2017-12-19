import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5

keys = open('pwd.txt','r').read().split('\n')
key = MD5.new(keys[0]).hexdigest()[0:16]
chunk_size=128*1024

def decrypt(crypt_path, decrpyt_path=None):
    with open(crypt_path, 'rb') as crypt_file:
        file_size = struct.unpack('Q', crypt_file.read(8))[0]
        # Replace struct.calcsize('Q') by 8
        decryptor = AES.new(key, AES.MODE_CBC, keys[1])

        with open(decrpyt_path, 'wb') as decrypt_file:
            while True:
                chunk = crypt_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                decrypt_file.write(decryptor.decrypt(chunk))

            decrypt_file.truncate(file_size)

if(__name__ == "__main__"):
    CRYPTED_DIR = os.path.abspath('./Backup')
    FINALPATH = os.path.abspath('~/Desktop/Decrypted-Backup')

    folder_name = os.path.split(CRYPTED_DIR)[1]
    for root, subdirs, files in os.walk(CRYPTED_DIR):
        useful_root = root[len(CRYPTED_DIR)+1:]
        for subdir in subdirs:
            pathlist = os.path.join(FINALPATH,folder_name,useful_root,subdir)
            os.makedirs(pathlist)
        for file in files:
            src = os.path.join(root,file)
            dest = os.path.join(FINALPATH,folder_name,useful_root,file)
            decrypt(src,dest)