# Python Scripts
This repository contains all of my Python scripts made for simplifying tasks.

### Libraries Used:
 - os
 - sys
 - openpyxl
 - hashlib
 - filecmp
 - struct
 - Crypto
 - shutil

### List of Scripts:
1. Duplicate: 
   - It lists all the duplicate files present at a given path.
   - Gives the option to remove/ not remove any of them.
   - Uses 'filecmp' and 'os' libraries to compare files which are of the same size
   - How to use:
      ```bash
      python filecmp.py /path/to/folder
      ```
2. Excel-Attd: 
   - Fills the attendance of all BITS Students(mathced by ID) in an excel sheet.
   - Created to fill the attendance of Students registered in CP Course at BITS Pilani
   - How to use:
      ```bash
      python update.py /path/to/attendance_list /path/to/excel_sheet <Attd Column No.>
      ```
3. auto-backup:
   - Takes backup of all the important data in two formats
     - Copies the data directly, or
     - Encrypts the data using AES Encryption (CBC) and then store it
   - How to use:<br>
     - To take backup(Both Simple and encrypted)
        ```bash
        python auto.py
        ```
     - To take only simple backup
        ```bash
        python backup.py
        ```
     - To take only encrypted backup
        ```bash
        python crypt.py
        ```
     - To decrypt the files encrypted
        ```bash
        python crypt.py 0
        ```
     - Paths for simple backup must be stored in 'backup_paths', each separated by newline
     - Paths for encrypted backup must be stored in 'secure_paths', each separated by newline

### Improvement:
Anyone is welcome to contribute and improve/modify the scripts. <br>
Please open an issue if you find any bugs in any of the scripts.